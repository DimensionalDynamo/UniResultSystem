create DATABASE if not exists university_results;
use university_results;
create table if not exists grade_master(
    grade_id int AUTO_INCREMENT PRIMARY KEY,
    min_marks int,
    max_marks int,
    grade VARCHAR(2),
    grade_point int
);

create table if not exists batches (
    batch_id int AUTO_INCREMENT PRIMARY KEY,
    batch_name VARCHAR(50) NOT NULL,
    start_year int,
    end_year int
);

CREATE table if not exists students (
    student_id int auto_increment primary key,
    roll_no varchar(20) UNIQUE not null,
    enrollment_no varchar(20) UNIQUE not null,
    abc_id varchar(20),
    name varchar(100) not null,
    father_name varchar(100),
    mother_name varchar(100),
    dob DATE,
    gender VARCHAR(10),
    category VARCHAR(50),
    batch_id int,
    Foreign Key (batch_id) REFERENCES batches(batch_id)
);

create table if not exists subjects (
    subject_id int AUTO_INCREMENT PRIMARY KEY,
    semester varchar(10),
    subject_code VARCHAR(20),
    subject_name VARCHAR(100),
    subject_type VARCHAR(10),
    credits int,
    max_ca_marks int DEFAULT 20,
    max_eose_marks int DEFAULT 80
);

create table if not exists marks (
    mark_id int AUTO_INCREMENT PRIMARY KEY,
    student_id int,
    subject_id int,
    ca_marks int DEFAULT 0,
    eose_marks int DEFAULT 0,
    total_marks int generated always as (ca_marks + eose_marks) stored,
    grade_point int,
    credit_point int,
    Foreign Key (student_id) REFERENCES students(student_id),
    Foreign Key (subject_id) REFERENCES subjects(subject_id)
);
