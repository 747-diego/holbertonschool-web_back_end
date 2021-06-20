-- Add bonus
-- SQL script that creates a stored procedure AddBonus
delimiter //
CREATE PROCEDURE addBonus (user_id INT, project_name CHAR(30), score INT)
BEGIN
    SET @bonus=(SELECT id FROM projects WHERE project_name = name);
    IF @bonus IS NULL THEN
        INSERT INTO projects (name) VALUES(project_name);
    END IF;
    SET @bonus=(SELECT id FROM projects WHERE project_name = name);
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @bonus, score);
END//
delimiter ;
