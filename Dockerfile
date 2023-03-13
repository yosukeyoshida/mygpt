FROM python:3.11

WORKDIR /root/work/
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2
COPY pyproject.toml .
COPY poetry.lock .
ENV PATH $PATH:/root/.local/bin
RUN poetry config virtualenvs.create false && poetry install
