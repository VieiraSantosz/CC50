Escreva uma consulta SQL para listar os nomes de todas as pessoas que dirigiram um filme que recebeu uma classificação de pelo menos 9,0.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada pessoa.
*Se uma pessoa dirigiu mais de um filme que recebeu uma classificação de pelo menos 9,0, eles só devem aparecer em seus resultados uma vez.

select DISTINCT (people.name), movies.title, ratings.rating
from people
inner join directors on directors.person_id = people.id
inner join movies on directors.movie_id = movies.id
inner join ratings on movies.id = ratings.movie_id
where ratings.rating = 9
group by people.name;