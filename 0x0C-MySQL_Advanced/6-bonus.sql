-- Add bonus
-- SQL script that creates a stored procedure AddBonus
delimiter //
CREATE PROCEDURE addBonus (user_id INT, project_name CHAR(30), score INT)
BEGIN
    SET @p_id=(SELECT id FROM projects WHERE project_name = name);
    IF @p_id IS NULL THEN
        INSERT INTO projects (name) VALUES(project_name);
    END IF;
    SET @p_id=(SELECT id FROM projects WHERE project_name = name);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @p_id, score);
END//
delimiter ;
