INSERT INTO status(status) VALUES('wishlist');
INSERT INTO status(status) VALUES('applied');
INSERT INTO status(status) VALUES('interview');
INSERT INTO status(status) VALUES('offer');
INSERT INTO status(status) VALUES('rejected');
INSERT INTO status(status) VALUES('closed');


INSERT INTO type(type) VALUES ('On-Site');
INSERT INTO type(type) VALUES ('Remote');
INSERT INTO type(type) VALUES ('Hybrid');

INSERT INTO job_board(board) VALUES ('LinkedIn');
INSERT INTO job_board(board) VALUES ('SEEK');
INSERT INTO job_board(board) VALUES ('Indeed');

INSERT INTO users(name, email, password_hash) VALUES (
	'Jens', 'yencey@gmail.com', '$2b$12$y0VEEmnjAFmiMGlCP6JkNufyfCjIl18qIAWgsjOqik2wBhr/pKWIK'
);

INSERT INTO companies (company_name, phone, email) VALUES ('RAC', '9430 6514', 'jobs@rac.com.au');

INSERT INTO applications(user_id, title, company, deadline, applied, type, job_board) VALUES (1, 'Software Engineer', 1, '2022-10-1', '2022-5-1', 1,1);