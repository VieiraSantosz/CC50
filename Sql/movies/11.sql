Escreva uma consulta SQL para listar os títulos dos cinco filmes com melhor classificação (em ordem) que Chadwick Boseman estrelou, começando com os de maior classificação.
*Sua consulta deve gerar uma tabela com uma única coluna para o título de cada filme.
*Você pode presumir que há apenas uma pessoa no banco de dados com o nome Chadwick Boseman.

select people.name, movies.title, ratings.rating from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
inner join ratings on ratings.movie_id = movies.id
where people.name = 'Chadwick Boseman'
order by ratings.rating desc
limit 5;