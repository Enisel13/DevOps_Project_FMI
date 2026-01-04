FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ ./src

EXPOSE 5001

CMD ["python", "src/app.py"]
