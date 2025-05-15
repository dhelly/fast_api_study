Executar o projeto

```bash
uv run uvicorn main:app --port 8000 --reload

# Dependências para autenticação
# a versão especifica do bcryp é para remover o erro version = _bcrypt.__about__.__version__
uv add passlib bcrypt==4.0.1

# Processar uploads de arquivos em aplicações web
uv add python-multipart

# jwt
uv add "python-jose[cryptography]"

# gerar uma chave no terminal
openssl rand -hex 32

# Dependência para trabalhar com Banco de dados Postgres
uv add psycopg2-binary

# Dependência para trabalhar com Banco de dados Mysql
uv add pymsql
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@localhost:3306/TodoApplicationDatabase'

# Migration
uv add alembic

# apos instalado executar o init na estrutura do projeto com o nome do ambiente - escolhemos "alembic"
alembic init alembic
```

### Configurações do Alembic 

1) Arquivo `alembic.ini`

alterar a variável `sqlalchemy.url` e inserir a string de conexão para o respectivo banco de dados

2) Arquivo `env.py`

- importe os `models`

```python
import app.models as models
```

- Alterar o código
```python
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
```
para

```python
fileConfig(config.config_file_name)
```

- Alterar para reconhecer os metadados
```python
target_metadata = None
```
para

```python
target_metadata = models.Base.metadata

```
3) criando a primeira revisão
```python
alembic revision revision -m "Create phone number for user column" 
```
- adicionando o código de criação da coluna telefone

```python
def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
```
- executar até esse ponto

```bash
# alembic upgrade <Revision id>
alembic upgrade 9d6bb04efb9d
```
- atualizamos o model para refletir a nova coluna

- desfazendo a migração
```bash
alembic downgrade -1  
```

- implementando o downgrade de telefone
```python
def downgrade() -> None:
    op.drop_column('users', 'phone_number')
```
- executamos novamente 
```bash
# alembic upgrade <Revision id>
alembic upgrade 9d6bb04efb9d
```

### Testes com pytest

1 - Criar um diretório Teste

2 - Criar o arquivo `__init__.py`

3 - Criar o `test_example.py`

4 - Instalar o pytest

```bash
uv add pytest
```

5 - Crie um teste

6 - Execute o pytest

```bash
uv run pytest
```

Observação:

Pytest não consegue testar assincronimos por padrão. Será necessário instalar um biblioteca.

```bash
uv add pytest-asyncio
```
## Fullstack Application

dependências

```bash
uv add alembic fastapi passlib bcrypt==4.0.1 "python-jose[cryptography]" psycopg2-binary pytest pytest-asyncio python-multipart sqlalchemy
```


```bash
uv add aiofiles
```

```bash
uv add jinja2
```