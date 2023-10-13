Escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram Toy Story.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada pessoa.
*Você pode presumir que há apenas um filme no banco de dados com o título Toy Story.

select people.name, movies.title from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
where movies.title like "toy story%";