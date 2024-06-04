# Apache Airflow com Docker Compose

Este repositório contém a configuração necessária para executar o Apache Airflow usando Docker Compose. Ele inclui um arquivo `docker-compose.yaml` que configura o ambiente do Airflow com PostgreSQL como banco de dados e uma DAG de exemplo com cinco tarefas.

## Requisitos

- Docker
- Docker Compose
- Python3

## Passos para Configuração

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/airflow-docker-compose.git

cd airflow-docker-compose
```

### 2. Gere uma chave Fernet

```python
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```
Modifique o arquivo Docker-compose.yaml

```python
environment:
    AIRFLOW__CORE__FERNET_KEY: 'SUA_CHAVE_FERNET_GERADA_AQUI'
```

### 3. Inicialize o ambiente e os serviços do Airflow

Execute o comando abaixo para inicializar o banco de dados e criar o usuário admin:

```
docker-compose up airflow-init
```

Após a inicialização, inicie todos os serviços do Airflow:

```
docker-compose up -d
```

### 4. Acesse a interface do Airflow

Abra o navegador e acesse http://localhost:8080. O nome de usuário padrão é **admin** e a senha padrão é **admin**.

### 5. Criando uma nova DAG

Para criar uma nova DAG, siga os passos abaixo:

Crie um novo arquivo Python no diretório dags. Por exemplo, new_dag.py.

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html

Depois de criar, reinicie os serviços do Airflow para carregar a nova DAG:

```
docker-compose restart webserver scheduler
```