-- Email validation to sent
-- SQL script that creates a trigger that resets the attribute valid_email
DELIMITER $$
CREATE TRIGGER 
validATTR
BEFORE UPDATE 
ON users FOR EACH ROW
IF OLD.email <> NEW.email THEN
SET NEW.valid_email = 0;
END IF;
DELIMITER;
