all_jobs = '''SELECT applications.id, title, company, deadline, applied, board,type_of_work, progress_status, job_link, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s
                ORDER BY progress_id DESC
                '''


job_by_id = '''SELECT applications.id, title, company, deadline, applied, board,type_of_work, progress_status, job_link, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s
                AND applications.id = %s'''

add_job = '''
    INSERT INTO applications (progress_id, user_id, title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

edit_job = '''
    UPDATE applications SET progress_id = %s, title = %s,company = %s,deadline = %s,applied = %s,type_of_work_id = %s,job_board_id =  %s,job_link = %s WHERE id = %s
'''

delete_job = '''
    DELETE FROM applications WHERE id = %s
'''

add_file = '''
    INSERT INTO files (job_id, file_name, url_address) VALUES (%s, %s, %s)
'''

get_files_by_id = '''
    SELECT * FROM files WHERE job_id = %s
'''
