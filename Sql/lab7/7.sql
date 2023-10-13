Escreva uma consulta SQL que retorne a energia média das músicas de Drake.
*Sua consulta deve gerar uma tabela com uma única coluna e uma única linha contendo a energia média.
*Você não deve fazer suposições sobre qual é o artist_id de Drake.

select avg (energy) from songs where artist_id in (select id from artists where name = 'Drake');