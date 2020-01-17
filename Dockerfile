FROM python:3.7-alpine
RUN apk add --no-cache git \
    build-base \
    postgresql \
    postgresql-dev \
    libpq \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev
RUN mkdir -p /opt/project
WORKDIR /opt/project
ADD requirements.txt /opt/project
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install ipython
RUN pip install coverage
RUN pip install django-discover-runner
ADD . /opt/project
ENV POSTGRES_DB carteras
ENV POSTGRES_PASSWORD secret123
ENV POSTGRES_USER carteras
ENV POSTGRES_HOST 172.17.0.1
ENV POSTGRES_PORT 5437