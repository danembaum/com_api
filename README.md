# com_api
Exemplo de plataforma de comunicação implementada em Python (3.9.0) (Django REST Framework)e MySQL 8.0.

Funcionalidades:

Agendamento e cancelamento do envio de mensagens, cadastro de Destinatários e de plataformas para envio.

`Recomenda-se criar um ambiente virtual Python.`

Instalando as libs:

`pip install -r requirements.txt`

ATENÇÃO:


Usuários do Windows podem não conseguir instalar o `mysqlclient 1.4.6` via pip, sendo necessário instalar via arquivo whl. 

-Download em https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient

Download do MySQL:
- https://dev.mysql.com/downloads/installer/


Alterar o modo de criptografia da senha na nova versão do MySQL, porque Django não tem suporte para a nova criptografia.

- Abra o MySQL Command Line Client (No Ubuntu, `/etc/init.d/mysql start`)
- Digite `use mysql;`
- Digite `alter user 'seu_usuario'@localhost identified with mysql_native_password by 'sua_senha';` (Ubuntu: `UPDATE mysql.user SET plugin = 'mysql_native_password' WHERE user = 'root'`;
Restaurando a base de dados:
`mysql -u root -p < /diretório-do-arquivo/labs.sql`


Rodando a aplicação:
- Abra o arquivo `settings.py` dentro de `communication_api`, procure `DATABASES` e edite os campos `USER`, `PASSWORD` e `PORT` do mesmo modo em que foi realizado durante a instalação do MySQL 
- Abra um prompt e vá até o diretório clonado (com_api)
- Digite `python manage.py runserver`
- Abra o browser, para verificar todos os agendamentos e/ou agendar envio de mensagens, digite `localhost:8000/agendamentoMensagem`. Para cadastrar um agendamento, preencha os dados e clique em `POST`
- Ao cadastrar um agendamento, mantenha a tecla `Ctrl` pressionada e clique em mais de um destinatário se desejar enviar a mesma mensagem para vários destinatários
- Para consultar um agendamento em específico e/ou realizar o cancelamento do agendamento (Excluir), digite `localhost:8000/agendamentoMensagem/<id>` e clique na opção `DELETE`

Para a realização dos testes, abra um prompt e digite `pytest`
- Após a execução dos testes, os resultados estarão disponíveis para visualização em HTML no diretório htmlcov (criado após a execução do teste)