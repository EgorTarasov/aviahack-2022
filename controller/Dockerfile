FROM python:3.10
RUN mkdir /computation
ADD . /computation
WORKDIR /computation
RUN pip install -r requirements.txt
CMD ["python", "computation.py"]