FROM python:3.10
RUN mkdir /init
ADD . /init
WORKDIR /init
RUN pip install -r requirements.txt
CMD ["python", "excel_to_bd.py"]