
SELECT
	pr.name AS product_name,
	ROUND(AVG(pr.price), 2) AS average_price,
	COUNT(f.id) AS total_feedbacks
FROM 
	products AS pr
		JOIN feedbacks AS f
			ON pr.id = f.product_id
WHERE
	pr.price > 15
GROUP BY
	pr.name
HAVING
	COUNT(f.id) > 1
ORDER BY
	total_feedbacks, average_price DESC;