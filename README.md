# com_api
Exemplo de plataforma de comunicação implementada em Python (3.9.0) (Django REST Framework)e MySQL 8.0.

Instalando as libs:

pip install requirements.txt

Alterar o modo de criptografia da senha na nova versão do MySQL, porque Django não tem suporte para a nova criptografia.

- Abra o MySQL Command Line Client
- Digite "use mysql;"
- Digite "alter user 'root'@localhost identified with mysql_native_password by 'root';"

Restaurando a base de dados:
mysql -u root -p < /diretório-do-arquivo/labs.sql
	