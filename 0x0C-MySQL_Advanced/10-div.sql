-- Safe divide
-- SQL script that creates a function SafeDiv
CREATE FUNCTION SafeDiv
(INT a, INT b)
IF b == 0 THEN
return 0
ELSE IF
return a / b
