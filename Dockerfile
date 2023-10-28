FROM python:3.8.12-slim

WORKDIR /api/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /api/

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"] 