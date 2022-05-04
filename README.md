# api_yamdb
## Описание:
Это API проекта yamdb, позволяющего хранить отзывы пользователей на различные произведения

## Как запустить:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/dthursdays/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Список доступных команд:
Подробное описание всех эндпоинтов можно найти по адресу http://127.0.0.1:8000/redoc/ после запуска проекта на локальном сервере

## Технологии:

- python 3.9.7
- django 3.0.0
- django rest framework 3.12.4
- django-filter 21.1
- pyJWT 2.1.0

## Над проектом работали:

### Никита Сологуб, Никита Синицын, Антон Малков
