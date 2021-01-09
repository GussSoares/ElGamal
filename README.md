# ElGamal

## Depedências
1. Instalar o docker [aqui](https://docs.docker.com/engine/install/ubuntu/).
2. Instalaro docker-compose [aqui](https://docs.docker.com/compose/install/).

## Execução
#### Para a primeira execução, execute:
```sh
sudo docker-compose up --build
```

#### Para as demais execuções, execute:
```sh
sudo docker-compose up
```

#### Para finalizar os containers:
```sh
sudo docker-compose down -v
```

## Alteração das mensagens
Para alterar as mensagens, acesse os arquivo ***docker-compose.yaml*** e altere a frase do cliente escolhido na variável de ambiente **MESSAGE**.
