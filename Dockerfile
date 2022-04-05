FROM python:3.9

WORKDIR /flask-app
COPY requirements.txt /flask-app/

RUN pip install -r requirements.txt

COPY . /flask-app/

CMD ["python", "run.py"]
