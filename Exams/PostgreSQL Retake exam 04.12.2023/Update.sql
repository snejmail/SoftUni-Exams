UPDATE products
SET price = price * 1.10
WHERE id IN (
    SELECT pr.id
    FROM products AS pr
    	JOIN feedbacks AS f 
			ON pr.id = f.product_id
    WHERE f.rate > 8
);