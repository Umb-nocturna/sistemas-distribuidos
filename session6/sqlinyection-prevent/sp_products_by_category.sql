DELIMITER //
CREATE PROCEDURE `sp_products_by_category`(IN category VARCHAR(60))
BEGIN
    SELECT PR.id, PR.name, PR.price 
    FROM products PR
    WHERE PR.category = category AND PR.released = 1
    ORDER BY PR.name ASC;
END //
DELIMITER ;