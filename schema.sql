DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS status CASCADE;
DROP TABLE IF EXISTS type CASCADE;
DROP TABLE IF EXISTS companies CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS job_board CASCADE;
DROP TABLE IF EXISTS applications CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	password_hash text NOT NULL
);

CREATE TABLE status (
	id SERIAL PRIMARY KEY,
	status varchar(30) NOT NULL
);

CREATE TABLE type (
	id SERIAL PRIMARY KEY,
	type VARCHAR(30) NOT NULL
);

CREATE TABLE companies (
	id SERIAL PRIMARY KEY,
	company_name VARCHAR(255),
	address VARCHAR(255),
	phone TEXT,
	email TEXT
);

CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	email VARCHAR(255),
	phone VARCHAR(30),
	company INTEGER REFERENCES companies(id)
);

CREATE TABLE job_board (
	id SERIAL PRIMARY KEY,
	board TEXT
);

CREATE TABLE applications (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users(id),
	title TEXT NOT NULL,
	company INTEGER REFERENCES companies(id),
	deadline DATE,
	applied DATE,
	type INTEGER REFERENCES type(id),
	job_board INTEGER REFERENCES job_board(id)
);