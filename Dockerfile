FROM python:3.10

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --no-modify-path && \
    ln -s $HOME/.poetry/bin/poetry /usr/local/bin/poetry

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry config virtualenvs.in-project true
RUN poetry install

COPY . .


CMD poetry run gunicorn aidanaBackend.wsgi:application --workers=3 -b :8080
