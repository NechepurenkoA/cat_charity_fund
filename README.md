# Проект QRКот (˃ᆺ˂)


## Подробности для чего предназначен проект
Этот проект предназначен для помощи нашим младшим друзьям, любимым питомцам или же просто котикам!
По сути это готовое приложение, к которому осталось прикрутить визуальную составляющую и использовать 
его как полноценное веб или мобильное приложение! (В данный момент, можно считать это частью чего-то глобального!)

## Запуск проекта

Для запуска проекта вам понадобится:

1. Развернуть и активировать виртуальное окружение на Python 3.9
   ```bash
    # Mac and Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # Windows
    py -3.9 -m venv venv
    source venv/Scripts/activate 
   ```
2. Установить зависимости
    ```bash
   pip install -r requirements.txt
   ```
3. Запустить проект с помощью `uvicorn`
    ```bash
   uvicorn app.main:app --reload --port 1111 # аргумент порт можете использовать по желанию
    ```
   
_Использованные технологии и доп. библиотеки: [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://docs.pydantic.dev/latest/),
[SQLAlchemy](https://www.sqlalchemy.org/?ref=), Python 3.9_