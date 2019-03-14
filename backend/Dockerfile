FROM python:3.7.2-alpine3.9

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install --dev --system --deploy --ignore-pipfile

ENV FLASK_APP app.py
ENV FLASK_ENV development

EXPOSE 5000
CMD ["flask", "run"]