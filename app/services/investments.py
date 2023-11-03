from datetime import datetime as dt

from sqlalchemy import select

from app.models import Donation, CharityProject
from app.core.db import AsyncSession


async def close_dono_or_proj(
        to_close: Donation or CharityProject
) -> None:
    """Фун-ия для закрытия доната или проэкта сбора"""
    to_close.fully_invested = True
    to_close.close_date = dt.now()


async def investment_addition(
        proj: CharityProject,
        dono: Donation,
        to_add: int
) -> None:
    """Фун-ия 'распределитель'"""
    proj.invested_amount += to_add
    dono.invested_amount += to_add


async def add_dono_to_proj(
        dono: Donation,
        proj: CharityProject
):
    """Фун-ия для распределения средств"""
    proj_dif = proj.full_amount - proj.invested_amount  # разность между уже собранными деньгами и целью
    dono_dif = dono.full_amount - dono.invested_amount  # разность между уже отданными деньгами и оставшимися

    if proj_dif >= dono_dif:
        await investment_addition(proj, dono, dono_dif)

    if proj_dif < dono_dif:
        await investment_addition(proj, dono, proj_dif)

    if proj.invested_amount == proj.full_amount:
        await close_dono_or_proj(proj)

    if dono.invested_amount == dono.full_amount:
        await close_dono_or_proj(dono)

    return proj


async def invest(session: AsyncSession) -> None:
    """Main фун-ия инвестирования"""
    projects_query = await session.scalars(
        select(CharityProject).where(CharityProject.fully_invested == False)
    )
    donations_query = await session.scalars(
        select(Donation).where(Donation.fully_invested == False)
    )
    uninvested_projs = projects_query.all()
    uninvested_donos = donations_query.all()
    for proj in uninvested_projs:
        for dono in uninvested_donos:
            proj = await add_dono_to_proj(dono, proj)
            if proj.invested_amount == proj.full_amount:
                break
    await session.commit()
