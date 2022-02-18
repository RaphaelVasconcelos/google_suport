# Risk Actions

## Table of Content

- **[How to](#how-to)**
- **[Make Commands](#make-commands)**
- **[Python Version](#python-version)**

----

## How to

- Run this command the first time you run the project:
  - `make init`

- Add libraries:
  - `make add-deps libs="lib_name_1==version ...lib_name_[n]==version"`
  - `make lock-deps`
  - `make run`

- Remove libraries:
  - `make rm-deps libs="lib_name_1 ...lib_name_[n]"`
  - `make lock-deps`

- Add dev libraries:
  - `make add-dev-deps libs="lib_name_1==version ...lib_name_[n]==version"`
  - `make lock-deps`
  - `make run`

- Remove dev libraries:
  - `make rm-dev-deps libs="lib_name_1 ...lib_name_[n]"`
  - `make lock-deps`

- Build and run:
  - `make run` ➞ Run application

## Make Commands

| Command           | Description                                                      |
| ---------------   | ---------------------------------------------------------------- |
| `init`            | Installs python dependencies and create `poetry` container       |
| `install-deps`    | Installs python dependencies to run the project                  |
| `poetry-create`   | Creates `poetry` container and sets the time limit (Default: 1h) |
| `poetry-export`   | Exports the project's dependencies to "requirements.txt"         |
| `lock-deps`       | Locks project dependencies                                       |
| `add-deps`        | Add project dependencies                                         |
| `rm-deps`         | Remove project dependencies                                      |
| `add-dev-deps`    | Add project dev dependencies                                     |
| `rm-dev-deps`     | Remove project dev dependencies                                  |
| `build`           | Builds Docker image                                              |
| `run`             | Run the project                                                  |
| `build-container` | ...                                                              |
| `run-container`   | ...                                                              |


## Python Version

To run the project you should use [`pyenv`](https://github.com/pyenv/pyenv#installation) to install `python 3.10.0`


## Instalar o pyenv e virtualenvwrapper

### dependências do pyenv
sudo apt install gcc make

### instalar o pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
cd ~/.pyenv && src/configure && make -C src

### abrir o .profile
code ~/.profile

### colar no início do arquivo, antes de qualquer comando que já exista nele:
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

### Encerrar a sessão do ubuntu e fazer login

### dependências para compilar e instalar o python
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

### instalar a ultima versão do python
pyenv install 3.10.0

### configurar versão 3.10.0 como global
pyenv global 3.10.0

### instalar virtualenv e virtualenvwrapper na versão 3.10.0 do Python
pip install virtualenv virtualenvwrapper

### instalar pyenv-virtualenvwrapper
git clone https://github.com/pyenv/pyenv-virtualenvwrapper.git $(pyenv root)/plugins/pyenv-virtualenvwrapper

### abrir o .bashrc
code ~/.bashrc

### colar em algum lugar:
\# virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=$HOME/.pyenv/versions/3.10.0/bin/python
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source $HOME/.pyenv/versions/3.10.0/bin/virtualenvwrapper.sh

export PYENV_ROOT="$HOME/.pyenv"

### pyenv-virtualenvwrapper
### To get virtualenvwrapper to create a virtual environment using pyvenv instead of virtualenv
export PYENV_VIRTUALENVWRAPPER_PREFER_PYVENV="true"

### initialize pyenv
eval "$(pyenv init -)"
### initialize pyenv virtualenvwrapper
pyenv virtualenvwrapper_lazy

### executar o source no .bashrc
source ~/.bashrc

### Para testar, abra o terminal e execute:

### criar um ambiente
mkvirtualenv teste

### sair do ambiente
deactivate

### apagar o ambiente
rmvirtualenv teste
