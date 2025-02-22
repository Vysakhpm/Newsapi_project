FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev

RUN pip install --no-cache-dir streamlit sqlalchemy pandas textblob psycopg2-binary 

COPY . .

EXPOSE 8051

CMD ["streamlit", "run", "app.py", "--server.port=8051", "--server.enableCORS=false"]



