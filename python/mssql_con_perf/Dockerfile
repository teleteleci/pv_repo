FROM python:3.6.7-alpine3.7

ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "create_conn.py"]
