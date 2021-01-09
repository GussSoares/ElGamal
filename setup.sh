#!/usr/bin/env bash

if ! command -v pyenv &> /dev/null
then
    echo "Parece que o pyenv não está instalado. Instale usando: curl https://pyenv.run | bash"
    exit
fi

PYTHON_VERSION='3.8.1'
PROJECT_NAME='elgamal'
ENV_NAME="env-${PROJECT_NAME}-${PYTHON_VERSION}"

pyenv install 3.8.1
pyenv virtualenv 3.8.1 $ENV_NAME
pyenv local $ENV_NAME

pip install --upgrade pip
pip install -r docs/requirements.txt

echo "Processo finalizado\! \nExecute a aplicação com: python run.py"