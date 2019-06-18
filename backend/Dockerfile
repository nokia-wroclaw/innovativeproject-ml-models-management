FROM python:3.7.2-alpine3.9

RUN pip install pipenv
COPY . /app
WORKDIR /app

RUN apk add bash postgresql-dev gcc python3-dev musl-dev
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000
CMD [ "./development.sh" ]