-- Buy buy buy
-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER 
subItem
AFTER INSERT ON orders 
FOR EACH ROW 
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
