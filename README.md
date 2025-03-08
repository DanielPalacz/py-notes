Hello in My Py Notes!

Www accessibility:
https://danielpalacz.github.io/py-notes/

Py-Notes project moved to be Programming Notes project where Python Notes is one of root.

# Poetry:
```
poetry env list
poetry env remove [poetry-env]

poetry lock
poetry install
poetry update
poetry env list
poetry env activate
eval $(poetry env activate)

poetry env info

poetry install --no-root (only dependencies)

poetry shell
poetry self add poetry-plugin-shell



macOS:
curl -sSL https://install.python-poetry.org | python3 -
brew install poetry

Na Windows:

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicP) | python -
poetry --version


Ubuntu / new project:
curl -sSL https://install.python-poetry.org | python3 -
poetry init
poetry add $(cat requirements.txt)
```
