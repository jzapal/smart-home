FROM python3

RUN apt-get update
COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app/
RUN pip install -r requirements.txt

CMD ['python', 'api_main.py']