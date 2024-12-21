FROM python

WORKDIR /app

ARG PORT=8000
ENV PORT=$PORT
EXPOSE $PORT

COPY requirements.txt .
COPY /app .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]