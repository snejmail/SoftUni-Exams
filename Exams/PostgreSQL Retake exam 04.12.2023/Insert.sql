CREATE TABLE gift_recipients(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	country_id INT,
	gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO gift_recipients(id, name, country_id)
SELECT
	id,
	CONCAT_WS(' ', c.first_name, c.last_name) AS name,
	c.country_id
FROM
	customers AS c;
	
UPDATE gift_recipients
SET gift_sent = TRUE
FROM customers AS c
WHERE c.country_id IN (7, 8, 14, 17, 26)
	AND
	c.country_id = gift_recipients.country_id
;
	
