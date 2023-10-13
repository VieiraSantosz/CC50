Escreva uma consulta SQL para listar os nomes de todas as pessoas que estrelaram um filme no qual Kevin Bacon também estrelou.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada pessoa.
*Pode haver várias pessoas chamadas Kevin Bacon no banco de dados. Certifique-se de selecionar apenas Kevin Bacon nascido em 1958.
*O próprio Kevin Bacon não deve ser incluído na lista resultante.

select distinct (people.name) from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
where movies.title in (select movies.title from people
inner join stars on stars.person_id = people.id
inner join movies on movies.id = stars.movie_id
where people.name = 'Kevin Bacon' and people.birth = 1958) and people.name != 'Kevin Bacon';