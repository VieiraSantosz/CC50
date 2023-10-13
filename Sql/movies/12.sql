Escreva uma consulta SQL para listar os títulos de todos os filmes em que Johnny Depp e Helena Bonham Carter estrelaram juntos.
*Sua consulta deve gerar uma tabela com uma única coluna para o título de cada filme.
*Você pode presumir que há apenas uma pessoa no banco de dados com o nome Johnny Depp.
*Você pode presumir que há apenas uma pessoa no banco de dados com o nome Helena Bonham Carter.

select movies.title from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
where people.name = 'Johnny Depp' and movies.title in (select movies.title from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
where people.name = 'Helena Bonham Carter');