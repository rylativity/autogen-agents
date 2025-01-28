FROM python:3.12

SHELL [ "/bin/bash", "-c" ]

ENV PYTHONDONTWRITEBYTECODE=true \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \ 
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get -y update && apt-get -y install \
        curl \
        build-essential \
        software-properties-common && \
        # Install poetry
        curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY poetry.lock pyproject.toml ./

# COPY requirements.txt .
RUN --mount=type=cache,target=~/.cache/pypoetry \
    # pip install -r requirements.txt
    poetry install

COPY main.py .
ENTRYPOINT ["poetry", "run", "python3", "main.py" ]

# ENTRYPOINT ["litellm", "--model", "ollama/llama3:instruct" ]
