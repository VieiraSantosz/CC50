Escreva uma consulta SQL para listar todos os filmes lançados em 2010 e suas classificações, em ordem decrescente por classificação.
Para filmes com a mesma classificação, ordene-os em ordem alfabética por título.
*Sua consulta deve gerar uma tabela com duas colunas, uma para o título de cada filme e outra para a classificação de cada filme.
*Filmes sem classificação não devem ser incluídos no resultado.

select movies.title, ratings.rating from movies
inner join ratings on ratings.movie_id = movies.id
where movies.year = 2010 order by ratings.rating desc;

