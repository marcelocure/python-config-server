from python:2.7.15-stretch

RUN mkdir -p /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5050

CMD python src/api.py
