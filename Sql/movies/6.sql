Escreva uma consulta SQL para determinar a avaliação média de todos os filmes lançados em 2012.
*Sua consulta deve gerar uma tabela com uma única coluna e uma única linha (sem incluir o cabeçalho) contendo a classificação média.

select avg(ratings.rating) from movies
inner join ratings on ratings.movie_id = movies.id
where movies.year = 2012;