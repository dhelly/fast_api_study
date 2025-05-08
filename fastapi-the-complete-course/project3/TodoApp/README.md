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

```