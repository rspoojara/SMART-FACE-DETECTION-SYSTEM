import sqlite3
import registration_temp as reg

con = sqlite3.connect("project.db")

cr = con.cursor()
create_add_user_table_query = "create table add_user(email_value varchar(30) primary key, employee_id integer, name_value varchar(20), mobileNo_value integer, dateOfBirth_value date, gender_value tinyint, bloodGroup_value tinyint, department_value tinyint);"
# cr.execute(create_add_user_table_query)

insert_add_user_table_query = f"insert into add_user(email_value, employee_id, name_value, mobileNo_value, dateOfBirth_value, gender_value, bloodGroup_value, department_value) values({reg.email_value},{reg.employeeId_value},{reg.name_value},{reg.mobileNo_value},{reg.dateOfBirth_value},{reg.gender_value},{reg.bloogGroup_value},{reg.department_value});"

cr.execute(insert_add_user_table_query)
con.commit()
con.close()