FROM python:3
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install --upgrade django
CMD ["python", "app.py"]
