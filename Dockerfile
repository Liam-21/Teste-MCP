FROM python:3.14.3

WORKDIR /app

COPY requirements.txt* ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python",  "server.py"]