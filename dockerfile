FROM python:3.10
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8002:8000
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]