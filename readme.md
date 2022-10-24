# REST API ShDrive

Это приложение для распределение нагрузки автобусов в аэропорту Шереметьево.
Оно использует микросервисную архитектуру, позьволяющую распределять обязаности между сервисами.
В качестве основных сервисов сейчас предоставленны:

- Rest api сервер, для комуникации контролера и фронтэнда
- Фронтэнд реализованный на TS с ипользованием React для взаимодейтсвия оператора и водителя с системой.
- Основной контролер для составления задач для водителей, на основе расписания и данных от оператора

Реализация Rest api приложения расположена в директории `app`  
Для запуска приложения требуется создать `.env` файл с параметроми:

`DATABASE_URL="<dbdriver>://<username>:<pswd>@<host>:<port>/<database_name>"`

Запускать приложение рекомендуется с помошью docker compose.

## Run the app

    $ docker compose up --build -d

# REST API

The REST API to the example app is described below.

## Bus endpoints

### Get bus status

`GET /bus/bus_counter`

### Response

```json
 {
     "busy": int,
     "free": int,
 }
```

## Get free bus

### Request

`Get /bus/free`

### Response

```json
[
  {
    "point": 850,
    "id": 2,
    "state": true,
    "capacity": 50
  },
  {
    "point": 947,
    "id": 4,
    "state": true,
    "capacity": 50
  }
]
```
