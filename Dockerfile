FROM python:3.10

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --no-modify-path && \
    ln -s $HOME/.poetry/bin/poetry /usr/local/bin/poetry

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install

COPY . .

CMD ["poetry run gunicorn --workers=3 aidanaBackend.wsgi:application -b 80"]
