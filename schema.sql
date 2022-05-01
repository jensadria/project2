DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS reviews

CREATE TABLE food (
	id serial PRIMARY KEY,
	name varchar(50) NOT NULL,
	image_url text,
	price_in_cents INTEGER NOT NULL
)

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	user_id INT,
	review TEXT,
	rating INT,
	FOREIGN KEY(user_id)
	REFERENCES users(id)
)