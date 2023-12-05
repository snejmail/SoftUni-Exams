CREATE OR REPLACE PROCEDURE
	sp_customer_country_name(
		IN customer_name VARCHAR(50),
		OUT country_name VARCHAR(50)
	) AS $$
	
BEGIN
	SELECT
		co.name INTO country_name
		FROM
			countries AS co
				JOIN customers AS cu
					ON cu.country_id = co.id
	WHERE
		CONCAT_WS(' ', cu.first_name, cu.last_name) = customer_name;
END;

$$ LANGUAGE plpgsql;