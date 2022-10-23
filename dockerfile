FROM python:3.10
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install fastapi
CMD ["python", "main.py"]