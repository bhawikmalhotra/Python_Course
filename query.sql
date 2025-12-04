CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);

INSERT INTO students (name, age, grade) VALUES
('Aarav', 16, '10th'),
('Riya', 15, '9th'),
('Kabir', 17, '11th'),
('Neha', 14, '8th'),
('Arjun', 18, '12th');

SELECT * FROM students;

SHOW databases;