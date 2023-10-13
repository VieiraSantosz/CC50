Escreva uma consulta SQL para listar os nomes das 5 músicas mais longas, em ordem decrescente de duração.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.

select name, duration_ms from songs order by duration_ms desc limit 5;