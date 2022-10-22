FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "80", "--reload" ]