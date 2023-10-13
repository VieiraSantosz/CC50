Escreva uma consulta SQL que liste os nomes de quaisquer músicas que tenham dançabilidade, energia e valência maior que 0,75.
*Sua consulta deve gerar uma tabela com uma única coluna para o nome de cada música.

select name, danceability, energy, valence from songs where danceability > 0.75 and energy > 0.75 and valence > 0.75;