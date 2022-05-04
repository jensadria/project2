all_jobs = '''SELECT applications.id, title, company, deadline, applied, board,type_of_work, progress_status, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s'''


job_by_id = '''SELECT applications.id, title, company, deadline, applied, board,type_of_work, progress_status, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s
                AND applications.id = %s'''

add_job = '''
    INSERT INTO applications (progress_id, user_id, title, company, deadline, applied, type_of_work_id, job_board_id, job_link) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
