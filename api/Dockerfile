FROM python:3.10

WORKDIR /api

RUN pip install pipenv

COPY Pipfile.lock Pipfile.lock

RUN pipenv sync

EXPOSE 8000

COPY . /api

CMD ./run.sh
