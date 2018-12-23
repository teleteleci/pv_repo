FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
ADD requirements.txt /app/
ADD my_project/ /app/
WORKDIR /app/my_project/
RUN pip install -r /app/requirements.txt
