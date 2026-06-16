-- ultima aula de Quinta-feira dia 11

SELECT * 
FROM professores
WHERE nome = 'Mateus';


SELECT
FROM professores
WHERE id_professor = 4;


UPDATE professores
SET telefone = '(63)98888-1111'
WHERE id_professor = 1; 


UPDATE professores
SET especialidade = 'Matematica'
WHERE id_professor = 4;


DELETE FROM alunos
WHERE id_aluno = 12;