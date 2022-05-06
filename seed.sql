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
	'Jens', 'jens@jens.com', '$2b$12$y0VEEmnjAFmiMGlCP6JkNufyfCjIl18qIAWgsjOqik2wBhr/pKWIK'
);
INSERT INTO users(name, email, password_hash) VALUES (
	'lionel', 'lionel@gmail.com', '$2b$12$y0VEEmnjAFmiMGlCP6JkNufyfCjIl18qIAWgsjOqik2wBhr/pKWIK'
);

INSERT INTO applications(user_id, progress_id,  title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,1, 'Junior Software Developers', 'The Ruby Group', '2022-6-6', '2022-5-1',1,1, 'https://www.seek.com.au/job/56826404?type=standard#sol=e901b9fa851570c45007ee6168556eb52d6afe08');
INSERT INTO applications(user_id, progress_id,  title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,1, 'Full-Stack Software Developer', 'Motium', '2022-6-6', '2022-5-1',1,1, 'https://www.seek.com.au/job/56823079?type=standout#sol=4e61dedc1c25d34e1885ede5c454d7621b6c91d6');
INSERT INTO applications(user_id, progress_id,  title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,6, 'Software Engineer', 'Commonwealth Bank', '2022-6-6', '2022-5-1',1,1, 'https://www.linkedin.com/jobs/view/3027626073/?refId=59437229-9e59-4bef-8f92-be3cb0ddf4f7');
INSERT INTO applications(user_id, progress_id,  title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
			VALUES (1,3, 'Mobile App Developer', 'BlueSky Digital Labs', NULL, '2022-4-20',1,3, '');
