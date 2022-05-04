INSERT INTO progress(progress_status) VALUES('wishlist');
INSERT INTO progress(progress_status) VALUES('applied');
INSERT INTO progress(progress_status) VALUES('interview');
INSERT INTO progress(progress_status) VALUES('offer');
INSERT INTO progress(progress_status) VALUES('rejected');
INSERT INTO progress(progress_status) VALUES('closed');


INSERT INTO types_of_work(type_of_work) VALUES ('On-Site');
INSERT INTO types_of_work(type_of_work) VALUES ('Remote');
INSERT INTO types_of_work(type_of_work) VALUES ('Hybrid');

INSERT INTO job_board(board) VALUES ('LinkedIn');
INSERT INTO job_board(board) VALUES ('SEEK');
INSERT INTO job_board(board) VALUES ('Indeed');

INSERT INTO users(name, email, password_hash) VALUES (
	'Jens', 'yencey@gmail.com', '$2b$12$y0VEEmnjAFmiMGlCP6JkNufyfCjIl18qIAWgsjOqik2wBhr/pKWIK'
);
INSERT INTO users(name, email, password_hash) VALUES (
	'lionel', 'lionel@gmail.com', '$2b$12$y0VEEmnjAFmiMGlCP6JkNufyfCjIl18qIAWgsjOqik2wBhr/pKWIK'
);

--INSERT INTO companies (name, phone, email) VALUES ('RAC', '9430 6514', 'jobs@rac.com.au');
--INSERT INTO companies (name, phone, email) VALUES ('Canva', '9430 1234', 'melanie@canva.com.au');
--INSERT INTO companies (name, phone, email) VALUES ('Microsoft', '9430 5678', 'bill@microsoft.com.au');

INSERT INTO applications(user_id, progress_id,  title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,1, 'Software Engineer', 'RAC', '2022-10-1', '2022-5-1',1,1, 'https://www.google.com');
INSERT INTO applications(user_id, progress_id, title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,1, 'Web Developer', 'Canva', '2022-9-5', '2022-5-5',2,2, 'https://www.canva.com');
INSERT INTO applications(user_id, progress_id, title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (2,3, 'Azure DevOps Engineer', 'Microsoft', '2022-5-5', '2022-5-10',2,3, 'https://www.microsoft.com');