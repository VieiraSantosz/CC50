Escreva uma consulta SQL que lista os nomes das músicas de Post Malone.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.
*Você não deve fazer suposições sobre qual é o artist_id de Post Malone.

select name from songs where artist_id in (select id from artists where name = 'Post Malone');