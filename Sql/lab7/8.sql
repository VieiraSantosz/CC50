Escreva uma consulta SQL que lista os nomes das músicas que apresentam “feat.” (participação) de outros artistas.
*Músicas que apresentam outros artistas incluirão “feat.” no nome da música.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.

select name from songs where name like '%feat%';