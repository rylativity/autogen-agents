FROM python:3.12

SHELL [ "/bin/bash", "-c" ]

ENV PYTHONDONTWRITEBYTECODE=true \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \ 
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
ENV CHROMEDRIVER_PATH="/usr/bin/chromedriver"

RUN apt-get -y update && apt-get -y install \
        curl \
        build-essential \
        software-properties-common \
        chromium-driver && \
        # Install poetry
        curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /workspace

COPY poetry.lock pyproject.toml ./

# COPY requirements.txt .
RUN --mount=type=cache,target=~/.cache/pypoetry \
    # pip install -r requirements.txt
    poetry install && \
    # Playwright needed for MultimodalWebSurfer Agent
    poetry run playwright install --with-deps

CMD ["poetry", "run", "jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--NotebookApp.token=''", "--NotebookApp.password=''", "--no-browser", "--allow-root"]