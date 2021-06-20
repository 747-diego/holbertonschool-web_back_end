-- Average Score
-- SQL script that creates a stored procedure 

CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
SET @name=(SELECT name FROM users WHERE user_id=id);
SET @avg=(SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id);
UPDATE users SET average_score = @avg WHERE name = @name;
END
