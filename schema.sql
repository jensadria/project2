DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS job_status CASCADE;
DROP TABLE IF EXISTS types_of_work CASCADE;
--DROP TABLE IF EXISTS companies CASCADE;
--DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS job_board CASCADE;
DROP TABLE IF EXISTS applications CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	password_hash text NOT NULL
);

CREATE TABLE progress (
	id SERIAL PRIMARY KEY,
	progress_status varchar(30) NOT NULL
);

CREATE TABLE types_of_work (
	id SERIAL PRIMARY KEY,
	type_of_work VARCHAR(30) NOT NULL
);

--CREATE TABLE companies (
--	id SERIAL PRIMARY KEY,
--	name VARCHAR(255),
--	address VARCHAR(255),
--	phone TEXT,
--	email TEXT
--);

--CREATE TABLE contacts (
--	id SERIAL PRIMARY KEY,
--	first_name VARCHAR(255),
--	last_name VARCHAR(255),
--	email VARCHAR(255),
--	phone VARCHAR(30),
--	company_id INTEGER REFERENCES companies(id)
--);

CREATE TABLE job_board (
	id SERIAL PRIMARY KEY,
	board TEXT
);

CREATE TABLE files (
	id SERIAL PRIMARY KEY,
	job_id REFERENCES applications(id),
	file_name TEXT,
	url_address TEXT NOT  
)

CREATE TABLE applications (
	id SERIAL PRIMARY KEY,
	progress_id INTEGER REFERENCES progress(id),
	user_id INTEGER REFERENCES users(id),
	title TEXT NOT NULL,
	company TEXT,
	deadline DATE,
	applied DATE,
	type_of_work_id INTEGER REFERENCES types_of_work(id),
	job_board_id INTEGER REFERENCES job_board(id),
	job_link TEXT
);