Escreva uma consulta SQL para listar os títulos e anos de lançamento de todos os filmes de Harry Potter, em ordem cronológica.
*Sua consulta deve gerar uma tabela com duas colunas, uma para o título de cada filme e outra para o ano de lançamento de cada filme.
*Você pode presumir que o título de todos os filmes de Harry Potter começará com as palavras “Harry Potter” e que se o título
de um filme começar com as palavras “Harry Potter”, é um filme de Harry Potter.

select title, year from movies where title like "harry potter%" order by year asc;