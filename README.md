# Django

## Initial Setup

### Install python

Install `python` using `pyenv`.

### Package manager

Install `pdm`

```shell
pdm init
pdm add django
pdm update
```

### Create project

```shell
pdm run django-admin startproject mysite .
```

### Run server

```shell
pdm run manage.py runserver
```

### Add strict typing

```shell
pdm add --dev django-stubs
pdm add --dev pyright
pdm add --dev pylance
```

### Add formatter and linter

```shell
pdm add --dev ruff
````
- https://docs.astral.sh/ruff/

```shell
pdm run ruff format
pdm run ruff check
```

### Add pre-commit

```shell
pdm add --dev pre-commit
pre-commit install
pre-commit sample-config > .pre-commit-config.yaml
```

Add `ruff` to `.pre-commit-config.yaml`: https://github.com/astral-sh/ruff-pre-commit

## Models and Migrations

```shell
pdm run manage.py makemigrations polls
```

```shell
pdm run manage.py sqlmigrate polls 0001
```

```shell
pdm run manage.py check
```

```shell
pdm run manage.py migrate
```
## Shell and Admin

```shell
pdm run manage.py shell
```

```shell
pdm run manage.py createsuperuser
```
