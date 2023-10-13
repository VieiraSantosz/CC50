Escreva uma consulta SQL para determinar o número de filmes com uma classificação IMDb de 10,0.
*Sua consulta deve gerar uma tabela com uma única coluna e uma única linha (sem incluir o cabeçalho) contendo o número de filmes com uma classificação de 10,0.

select movies.title, ratings.rating from movies
inner join ratings on ratings.movie_id = movies.id
where ratings.rating = 10;