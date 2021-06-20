-- Safe divide
-- SQL script that creates a function SafeDiv
DELIMITER //
CREATE FUNCTION SafeDiv (numone INT, numtwo INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF numtwo = 0 THEN
        RETURN 0;
    END IF;
    RETURN numone / numtwo;
END//
DELIMITER ;
