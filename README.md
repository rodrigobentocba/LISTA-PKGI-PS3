# Zabbix com Docker Compose - Rodrigo Bento

O setup do sistema Zabbix no Docker Composer foi implementado no Ubuntu 16.04 LTS;
O arquivo docker-compose.yml foi configurado de forma que o Docker crie 3 containers: zabbix-server, zabbix-frontend e mysql. Foram utilizadas as imagens oficiais do Zabbix e do MySQL em seus respectivos repositórios.

Ao executar o comando docker-compose up, o Docker irá subir automaticamente os containers do Zabbix e do MySQL. Após a execução do comando, o Zabbix já estará conectado ao banco de dados MySQL.

Como instalar o servidor Zabbix no Docker Compose:

1 - Criar a pasta zabbix-docker-compose na pasta home;

2 - Copiar o arquivo "docker-compose.yml" para a pasta "zabbix-docker-compose";

3 - Criar uma Network do tipo Bridge com o nome de network-zabbix-docker com o comando "docker network create --driver bridge network-zabbix" e  com o endereço de rede 10.1.1.0/24. Depois use o comando "docker network ls" para listar as redes ativas no sistema. Para descobrir se o servidor Zabbix está associado a rede "network-zabbix" execute o comando "docker network inspect";

4 - Executar o seguinte comando: "docker-compose up -d" na pasta "zabbix-docker-compose", onde esta localizado o arquivo docker-compose.yml para subir os containers;

As questões 2 e 3 não foram implementadas pois acredito que será feito no teste prático presencial em data a ser definida.

Obrigado!
