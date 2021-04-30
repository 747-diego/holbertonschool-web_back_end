-- Add bonus
-- SQL script that creates a stored procedure AddBonus
DELIMITER $$
CREATE PROCEDURE AddBonus 
(IN user_id INT, project_name VARCHAR(255), 
score INT)

IF NOT EXISTS (
    SELECT *
    FROM projects
    WHERE NAME = project_name)
    THEN
    INSERT INTO projects(NAME) VALUES(project_name);


INSERT INTO studentError(user_id, score,  project_id)
        VALUES(user_id, score,
        (SELECT id from projects
        WHERE NAME = project_name)
        );
DELIMITER;
