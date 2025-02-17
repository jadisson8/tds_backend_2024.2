FROM python:3.11.6-slim-bullseye

WORKDIR /home/app

COPY ./requirements.txt .

RUN python -m venv venv

ENV PATH="/home/app/venv/bin:${PATH}"

RUN . venv/bin/activate && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
