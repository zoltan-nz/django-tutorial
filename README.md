# Django

## Log

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

### Add strict typing

```shell
pdm add mypy
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
