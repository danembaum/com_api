# com_api
Exemplo de plataforma de comunicação implementada em Python (3.9.0) (Django REST Framework)e MySQL 8.0.

Funcionalidades:

Agendamento e cancelamento do envio de mensagens, cadastro de Destinatários e de plataformas para envio

Instalando as libs:

`pip install requirements.txt`

ATENÇÃO:

Usuários do Windows não conseguirão instalar o `mysqlclient 1.4.6` via pip, sendo necessário instalar via arquivo whl. 

-Download em https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

Alterar o modo de criptografia da senha na nova versão do MySQL, porque Django não tem suporte para a nova criptografia.

- Abra o MySQL Command Line Client
- Digite `use mysql;`
- Digite `alter user 'seu_usuario'@localhost identified with mysql_native_password by 'root';`

Restaurando a base de dados:
`mysql -u root -p < /diretório-do-arquivo/labs.sql`

Rodando a aplicação:
- Abra o arquivo `settings.py` dentro de `communication_api`, procure `DATABASES` e edite os campos `USER`, `PASSWORD` e `PORT` do mesmo modo em que foi realizado durante a instalação do MySQL 
- Abra um prompt e vá até o diretório clonado (com_api)
- Digite `python manage.py runserver`
- Abra o browser, para verificar todos os agendamentos e/ou agendar envio de mensagens, digite `localhost:8000/agendamentoMensagem`. Para cadastrar um agendamento, preencha os dados e clique em `POST`
- Para consultar um agendamento em específico e/ou realizar o cancelamento do agendamento (Excluir), digite `localhost:8000/agendamentoMensagem/<id>` e clique na opção `DELETE`