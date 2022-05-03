all_jobs = '''SELECT applications.id, title, companies.name, deadline, applied, board,type_of_work, progress_status, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN companies ON company_id = companies.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s'''


job_by_id = '''SELECT applications.id, title, companies.name, deadline, applied, board,type_of_work, progress_status, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN companies ON company_id = companies.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s
                AND applications.id = %s'''
