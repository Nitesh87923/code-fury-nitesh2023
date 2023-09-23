from sqlalchemy import create_engine, text
import os

db_connection_string =("mysql+pymysql://4l54pxih3z06xu20ihjr:pscale_pw_FhGkdQ5zTlxeN0MQ82nBTnAnyZwoitFcnEvmvZsfHr9@aws.connect.psdb.cloud/code_fury?charset=utf8mb4")

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
  





    


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])