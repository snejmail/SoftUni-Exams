SELECT
	i.name AS ingredient_name,
	pr.name AS product_name,
	d.name AS distributor_name
FROM 
	ingredients AS i
		JOIN products_ingredients AS pri
			ON i.id = pri.ingredient_id
				JOIN products AS pr
					ON pr.id = pri.product_id 
						JOIN distributors AS d
							ON d.id = i.distributor_id
WHERE
	LOWER(i.name) LIKE '%mustard%'
		AND
	d.country_id = 16
ORDER BY
	product_name;