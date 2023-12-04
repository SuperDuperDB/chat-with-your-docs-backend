FROM python:3.10-bullseye

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "app:app", "--forwarded-allow-ips='*'", "--host", "0.0.0.0", "--port", "8080"]