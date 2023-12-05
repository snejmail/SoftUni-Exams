SELECT
	d.name AS distributor_name,
	i.name AS ingredient_name,
	pr.name AS product_name,
	AVG(f.rate) AS average_rate
FROM
	ingredients AS i
		JOIN products_ingredients AS pri
			ON i.id = pri.ingredient_id
				JOIN products AS pr
					ON pr.id = pri.product_id 
						JOIN distributors AS d
							ON d.id = i.distributor_id
								JOIN feedbacks AS f
									ON f.product_id = pr.id
GROUP BY
	d.name, i.name, pr.name
HAVING
	AVG(f.rate) BETWEEN 5 AND 8
ORDER BY
	distributor_name, ingredient_name, product_name;