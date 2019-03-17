FROM python:3.7.2-alpine3.9

RUN pip install pipenv
COPY . /app
WORKDIR /app
RUN pipenv install --dev --system --deploy --ignore-pipfile

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]