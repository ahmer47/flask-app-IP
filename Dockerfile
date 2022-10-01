FROM python:3.10.4-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]