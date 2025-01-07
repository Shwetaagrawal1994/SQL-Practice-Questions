-- Create data base for saving tables
CREATE DATABASE DB_21dec;
use DB_21dec;

-- Create tables
-- TABLE 1 - Student (named as std)
CREATE TABLE std (
    STUDENT_ID INT PRIMARY KEY,           -- Unique identifier for each student
    FIRST_NAME VARCHAR(50) NOT NULL,      -- First name of the student
    LAST_NAME VARCHAR(50) NOT NULL,       -- Last name of the student
    GPA DECIMAL(4, 2) NOT NULL,           -- GPA of the student, with up to 4 digits (2 after the decimal)
    ENROLLMENT_DATE DATETIME,             -- Date and time of enrollment
    MAJOR VARCHAR(100),                   -- Major field of study
    DEPARTMENT VARCHAR(100),              -- Department field of student
    GENDER VARCHAR(100)
);

INSERT INTO std (STUDENT_ID, FIRST_NAME, LAST_NAME, GPA, ENROLLMENT_DATE, MAJOR, DEPARTMENT, GENDER)
VALUES
    (201, 'Toprak', 'Shemzi', 8.79, '2021-10-01 09:30:00', 'Computer Science', 'Sci', 'Male'),
    (202, 'Tuba', 'Ezesha', 8.44, '2019-05-01 08:30:00', 'Mathematics', 'Maths', 'Female'),
    (203, 'Omer', 'ceyik', 5.60, '2020-08-01 10:00:00', 'Biology', 'Sci', 'Male'),
    (204, 'Omer', 'Khang', 9.20, '2022-03-01 12:45:00', 'Chemistry', 'Sci', 'Male'),
    (205, 'Eleni', 'Tebta', 7.85, '2024-12-10 08:30:00', 'Physics', 'Sci', 'Female'),
    (206, 'Orhan', 'Wasim', 9.78, '2021-01-01 09:24:00', 'History', 'Art', 'Male'),
    (210, 'Ada', 'Khemiz', 9.78, '2021-01-01 09:24:00', 'Economics', 'Art', 'Female'),
    (207, 'Ayca', 'Khatabor', 9.81, '2022-12-01 02:30:00', 'English', 'Lit', 'Female'),
    (208, 'Cem', 'Murathan', 7.00, NULL, 'Mathematics', 'Maths', 'Male'),
    (209, 'Sevgi', 'Tasim', 7.50, '2024-12-15 06:30:00', NULL, 'Art', 'Female'),
    (211, 'Leyla', 'Kathmu', 6.50, '2024-12-15 06:30:00', 'Economics', 'NULL', 'Female');
    
-- TABLE 2 - Scolarship (named as scholar)
CREATE TABLE scholar (
    STUDENT_REF_ID INT NOT NULL,               -- References STUDENT_ID from std table
    SCHOLARSHIP_AMOUNT DECIMAL(10, 2) NOT NULL,-- Scholarship amount
    SCHOLARSHIP_DATE DATETIME NOT NULL,        -- Date the scholarship was granted
    SCHOLARSHIP_TYPE VARCHAR(100) 
);

INSERT INTO scholar (STUDENT_REF_ID, SCHOLARSHIP_AMOUNT, SCHOLARSHIP_DATE, SCHOLARSHIP_TYPE)
VALUES
    (201, 5000, '2021-10-15 00:00:00', 'Full'),
    (202, 4500, '2022-08-18 00:00:00', NULL),
    (203, 3000, '2022-01-25 00:00:00', NULL),
    (230, 3000, '2022-01-25 00:00:00', 'Full'),
    (210, 4000, '2021-10-15 00:00:00', 'Half');

-- TABLE 3 - Students (named as std_dup)
CREATE TABLE std_dup (
    STUDENT_ID INT PRIMARY KEY,           -- Unique identifier for each student
    FIRST_NAME VARCHAR(50) NOT NULL,      -- First name of the student
    LAST_NAME VARCHAR(50) NOT NULL,       -- Last name of the student
    GPA DECIMAL(4, 2) NOT NULL,           -- GPA of the student, with up to 4 digits (2 after the decimal)
    ENROLLMENT_DATE DATETIME,             -- Date and time of enrollment
    MAJOR VARCHAR(100),                   -- Major field of study
    DEPARTMENT VARCHAR(100),               -- Department field of student
	GENDER VARCHAR(100)
);

INSERT INTO std_dup (STUDENT_ID, FIRST_NAME, LAST_NAME, GPA, ENROLLMENT_DATE, MAJOR, DEPARTMENT, GENDER)
VALUES
    (251, 'Eleni', 'Ratik', 8.79, '2021-10-01 09:30:00', 'Computer Science', 'Sci', 'Female'),
    (252, 'Toprak', 'cleik', 8.44, '2019-05-01 08:30:00', 'Mathematics', 'Maths', 'Male'),
    (207, 'Ayca', 'Khatabor', 9.81, '2022-12-01 02:30:00', 'English', 'Lit', 'Female');

-- TABLE 4 - project details (named as project_details)
CREATE TABLE project_details (
    ProjectDetailID INT PRIMARY KEY,
    StudentID INT,
    ProjectName VARCHAR(50)
);

INSERT INTO project_details (ProjectDetailID, StudentID, ProjectName) VALUES
(1, 201, 'Task Track'),
(2, 201, 'CLP'),
(3, 201, 'Survey Managment'),
(4, 202, 'HR Managment'),
(5, 203, 'Task Track'),
(6, 203, 'GRS'),
(7, 230, 'DDS'),
(8, 204, 'HR Managment'),
(9, 206, 'GL Managment'),
(10, 208, 'DDS');

-- 1. Write a SQL query to fetch "FIRST_NAME" from the Student table in upper case and use ALIAS name as STUDENT_NAME.
select upper(FIRST_NAME) from std;

-- 2. Write a SQL query to fetch unique values of MAJOR Subjects from Student table.
-- *** Method 1
select major from std group by major;
-- *** Method 2
select distinct (major) from std group by major;

-- 3. Write a SQL query to print the first 3 characters of FIRST_NAME from Student table.
select substring(FIRST_NAME, 1, 3) from std;
-- NOTE :: except first 2 characters,  all the characters are printed
select substring(FIRST_NAME, 3) from std; 

-- 4. Write a SQL query to find the position of alphabet ('a') int the first name column 'Shivansh' from Student table.
select instr(FIRST_NAME, 'a') from std where FIRST_NAME = 'shivansh';

-- 5. Write a SQL query that fetches the unique values of MAJOR Subjects from Student table and print its length.
select distinct major, length(major) from std;

-- 6. Write a SQL query to print FIRST_NAME from the Student table after replacing 'a' with 'A'.
select replace(FIRST_NAME, 'a', 'A') from std; 
-- NOTE :: it replaces all the ocurences

-- 7. Write a SQL query to print the FIRST_NAME and LAST_NAME from Student table into single column COMPLETE_NAME
-- or Write a SQL query to retrieve Student's first name and last name in a single string
select concat(FIRST_NAME, ' ', LAST_NAME) as COMPLETE_NAME from std;

-- 8. Write a SQL query to print all Student details from Student table order by FIRST_NAME Ascending and MAJOR Subject descending .
select * from std order by FIRST_NAME, major desc;

-- 9. Write a SQL query to print details of the Students with the FIRST_NAME as 'Prem' and 'Shivansh' from Student table.
select * from std where FIRST_NAME in ('Prem', 'Shivansh'); 
-- NOTE :: 1.  if one name is not present then output will not be produced
--         2. '=' and 'in' have a difference. '=' is used with only 1 value and for multiple values use 'in'

-- 10. Write a SQL query to print details of the Students excluding FIRST_NAME as 'Prem' and 'Shivansh' from Student table.
select * from std where FIRST_NAME not in ('Prem', 'Shivansh'); 

-- 11. Write a SQL query to print details of the Students whose FIRST_NAME ends with 'a'.
select FIRST_NAME from std where FIRST_NAME like '%a';

-- 12. Write an SQL query to print details of the Students whose FIRST_NAME ends with ‘a’ and contains six alphabets.
select FIRST_NAME from std where FIRST_NAME like '_____a';

-- 13. Write an SQL query to print details of the Students whose GPA lies between 9.00 and 9.99.
select * from std where gpa between 9 and 9.99; 

-- 14. Write an SQL query to fetch the count of Students having Major Subject ‘Computer Science’.
select major, count(*) from std group by major having major = "Computer Science";
select major, count(major) from std group by major having major = "Computer Science"; 
-- NOTE :: output from both query is same

-- 15. Write an SQL query to fetch Students full names with GPA >= 8.5 and <= 9.5.
select * from std where gpa between 8.5 and 9.5;

-- 16. Write an SQL query to fetch the no. of Students for each MAJOR subject in the descending order.
select major, count(*) as n_std from std group by major order by n_std desc;

-- 17. Display the details of students who have received scholarships, including their names, scholarship amounts, & scholarship dates.
select t1.*, t2.* from std t1 join scholar t2 on t1.STUDENT_ID = t2.STUDENT_REF_ID;

-- 18. Write an SQL query to show only odd rows from Student table.
select *,row_number() over() as sno from std where sno = 2; 
-- NOTE :: this query will not work as where clause works before select clause
WITH NumberedRows AS (SELECT *, ROW_NUMBER() OVER (ORDER BY STUDENT_ID) AS RowNum FROM std)
SELECT * FROM NumberedRows WHERE RowNum % 2 = 1; 
-- NOTE :: Filtered odd-numbered rows but first line will not work individually

-- 19. Write an SQL query to show only even rows from Student table.
WITH NumberedRows AS (SELECT *, ROW_NUMBER() OVER (ORDER BY STUDENT_ID) AS RowNum FROM std)
SELECT * FROM NumberedRows WHERE RowNum % 2 = 0; 

/* 20. List all students and their scholarship amounts if they have received any. If a student has not received a scholarship, 
display NULL for the scholarship details.*/
select t1.*, t2.SCHOLARSHIP_AMOUNT, t2.SCHOLARSHIP_DATE from std t1 left join scholar t2 on t1.STUDENT_ID = t2.STUDENT_REF_ID;

-- 21. Write an SQL query to show the top n (say 5) records of Student table order by descending GPA.
-- *** Method 1 - using Limit
select * from std order by GPA desc limit 5;
-- *** Method 2 - using row_number + without duplicates
with std_upd as (select *, row_number() over(order by GPA desc) as r_no from std)
select * from std_upd where r_no <= 5;
-- *** Method 3 - using dense_rank + with duplicates
with std_upd as (select *, dense_rank() over(order by GPA desc) as r_no from std)
select distinct(r_no) from std_upd where r_no <= 5;
-- *** Method 4 - using subquery
SELECT * FROM ( SELECT *, ROW_NUMBER() OVER (order by GPA desc) AS r_no FROM std ) subquery WHERE r_no <= 5; 
-- *** Method 5 - using self join
SELECT s1.* FROM std AS s1 WHERE 5 >= (SELECT COUNT(DISTINCT s2.GPA) FROM std AS s2 WHERE s2.GPA > s1.GPA
) ORDER BY s1.GPA DESC;

-- 22. Write an SQL query to determine the nth (say n=3) highest GPA from a table
-- *** Method 1 - using Limit
select * from std order by GPA desc limit 2,1;
-- NOTE :: 4 represents number of rows to skip and 1 represents number of rows to show
-- *** Method 2 - using row_number + without duplicates
with std_upd as (select *, row_number() over(order by GPA desc) as r_no from std)
select * from std_upd where r_no = 3;
-- *** Method 3 - using dense_rank + with duplicates
with std_upd as (select *, dense_rank() over(order by GPA desc) as r_no from std)
select distinct(r_no) from std_upd where r_no = 3;
-- *** Method 4 - using subquery
select max(GPA) from std where GPA < (select max(GPA) from std where GPA < (select max(GPA) from std));
-- NOTE :: this will only give the max GPA but not other information of the student with the third highest GPA
select * from std where GPA = (select max(GPA) from std where GPA < (select max(GPA) from std where GPA < (select max(GPA) from std)));
-- NOTE :: this will all other information of the student with the third highest GPA
-- *** Method 5 - using self join
SELECT s1.* FROM std AS s1 WHERE 3 = (SELECT COUNT(DISTINCT s2.GPA) FROM std AS s2 WHERE s2.GPA > s1.GPA
) ORDER BY s1.GPA DESC;
-- *** Method 6 - but can be use only for second highest
select * from std where GPA = (select max(GPA) from std where GPA not in (select max(GPA) from std));

-- 23. Write an SQL query to fetch the list of Students with the same GPA.
-- *** Method 1 - Without using self join
SELECT s1.* FROM std s1, std s2 WHERE s1.GPA = s2.GPA AND s1.STUDENT_ID != s2.STUDENT_ID;
-- *** Method 2 - using self join
SELECT t1.*  FROM std t1 JOIN std t2 ON t1.GPA = t2.GPA WHERE t1.STUDENT_ID != t2.STUDENT_ID;
-- *** Method 3 - using group by
SELECT * FROM std WHERE GPA IN (SELECT GPA FROM std GROUP BY GPA HAVING COUNT(*) > 1);


-- 24. Write an SQL query to show one row twice in results from a table
select * from std union all select * from std order by STUDENT_ID;
-- NOTE :: order by will keep both enteries together

-- 25. Write an SQL query to list STUDENT_ID who does not get Scholarship
select * from std where STUDENT_ID not in (select STUDENT_REF_ID from scholar);

-- 26. Write an SQL query to fetch the first 50% records from a table
select * from std limit (select FLOOR(count(*)/2) from std) ;
/* NOTE :: The issue in above query arises because MySQL does not support subqueries directly within the LIMIT clause. To address 
this,you need to calculate the limit value first, either using a variable or a Common Table Expression (CTE) */
WITH RankedRecords AS (SELECT *, ROW_NUMBER() OVER (ORDER BY STUDENT_ID) AS RowNum FROM std)
select * FROM RankedRecords WHERE RowNum <= (SELECT FLOOR(COUNT(*) / 2) FROM std);

-- 27. Write an SQL query to fetch the MAJOR subject that have less than 4 people in it
select MAJOR, COUNT(MAJOR) AS MAJOR_COUNT FROM std GROUP BY MAJOR HAVING COUNT(MAJOR) < 4;

-- 28. Write an SQL query to show the last record from a table
select * from (select *, ROW_NUMBER() OVER () AS RowNum FROM std) subq order by RowNum desc limit 1;

-- 29. Write an SQL query to fetch the first row of a table
select * from (select *, ROW_NUMBER() OVER () AS RowNum FROM std) subq order by RowNum limit 1;

-- 30. Write an SQL query to fetch the last five records from a table
select * from (select *, ROW_NUMBER() OVER () AS RowNum FROM std) subq order by RowNum desc limit 5;

-- 31. Write an SQL query to fetch the details of Students who have the highest GPA
select * from std where GPA = (select max(GPA) from std);

-- 32. Write an SQL query to show the current date and time
select current_date(); -- NOTE :: It returns only cuurent date 
select now(); -- NOTE :: It returns only cuurent date and time
select CURRENT_TIMESTAMP; -- NOTE :: It returns only cuurent date and time

/* 33. Write a query to create a new table which consists of data and structure copied from the other table (say Student) or clone the 
table named Student */
create table new_std as select * from std;
select * from new_std;

-- 34. Write an SQL query to update the GPA of all the students in 'Computer Science' MAJOR subject to 7.5
update std set GPA = 7.5 where major = 'Computer Science';

-- 35. Write an SQL query to find the number of students in each major who have a GPA greater than 7.5
select MAJOR, COUNT(STUDENT_ID) FROM std where GPA > 3.5 GROUP BY MAJOR;
select MAJOR, COUNT(STUDENT_ID) FROM std GROUP BY MAJOR having GPA > 3.5;
/* NOTE :: The query you provided has a logical error because the HAVING clause refers to the column GPA, which is not aggregated 
or part of the GROUP BY result In MySQL, you cannot use non-aggregated columns in the HAVING clause unless they are part of the 
GROUP BY expression or wrapped in an aggregate function.*/

-- 36. Write an SQL query to find the students who have the same GPA as 'Prem Chopra'
select * from std WHERE GPA = (select GPA from std where FIRST_NAME = 'Prem' and LAST_NAME = 'Chopra');
/* NOTE :: This query will return Prem chopra as well as any other student with the same GPA. If no other student has the same GPA 
the details of only prem chopra will be returned */

-- 37. : SQL query to count the number of students where the enrollment date is NULL in the student table
select * from std WHERE enrollment_date is null;

-- 38. Create a query to categorize students into 'High', 'Medium', and 'Low' GPA ranges in the student table
-- or Write a query to display students grouped by their GPA brackets (e.g., >9, 7 to 9 and < 7)
select student_id, first_name, GPA, case when GPA > 9 then 'High GPA' when GPA between 7 and 9 then 'Medium GPA' else 'Low GPA' end as 
GPA_category from std;

-- 39. Write a query to fetch students enrolled in the last 30 days from the student table
-- *** Method 1 - using DATE_SUB
select  * FROM std WHERE DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= enrollment_date;
-- *** Method 2 - using DATEDIFF
SELECT *, DATEDIFF(curdate(), enrollment_date) FROM std where DATEDIFF(curdate(), enrollment_date) <= 30 ;
/* NOTE :: The query you provided will throw an error because you cannot directly use an alias (Total_days) defined in the SELECT 
clause inside the WHERE clause. The WHERE clause is evaluated before the SELECT clause, so the alias Total_days is not yet available. 
Therefore, updated query is given below */
SELECT *, DATEDIFF(curdate(), enrollment_date) AS Total_days FROM std where DATEDIFF(curdate(), enrollment_date) <= 30 ;
-- *** Method 3 - using TIMESTAMPDIFF
SELECT  *, TIMESTAMPDIFF(MONTH, enrollment_date, CURDATE()) AS MonthsDifference FROM std where 
TIMESTAMPDIFF(MONTH, enrollment_date, CURDATE()) = 0;

-- 40. Update the GPA of all students with the history major by 10% in the students table
update std set GPA = GPA*1.1 where major = "History";

-- 41. Write a query to find each student's rank based on GPA within their department
select *, dense_rank() over(partition by DEPARTMENT order by GPA) as ranks from std;
-- NOTE :: Student with NULL department is also given rank by the above query. All NULL are clubbed together in 1 category

-- 42. Format enrollment_date  field in the students table as 'YYYY-MM-DD'. eg -  2013/02/15"
select *, DATE_FORMAT(enrollment_date, '%Y-%m-%d') AS FormattedDate from std;

-- 43. Format enrollment_date  field in the students table as 'DD Mon YYYY'. eg - "15 Feb 2013"
select *, DATE_FORMAT(enrollment_date, '%d %b %Y') AS FormattedDate from std;

-- 44. Retrieve time from the enrollment_date field in the students table
select *, TIME(enrollment_date) AS TimeOnly from std;

-- 44. Retrieve year from the enrollment_date field in the students table
select *, YEAR(enrollment_date) AS years from std;
-- NOTE :: Month can be retrieved using month()

-- 45. Identify duplicate entries in the students table based on product major, and department
-- NOTE :: if based on is not specified then it means find duplicates based on all columns so write all column nmes in below queries
-- *** Method 1 - using group and having
select major, department, COUNT(*) AS DuplicateCount from std GROUP BY major, department HAVING COUNT(*) > 1;
-- *** Method 1 - using row_number()
select *, ROW_NUMBER() OVER(PARTITION BY major, department) AS counts from std;
-- NOTE :: above query will give the count and in order to retrieve the non duplicate rows use below query
select * from( SELECT *, ROW_NUMBER() OVER(PARTITION BY major, department ) AS counts from std) subq WHERE counts = 1;

-- 46. Delete duplicate entries in the students table based on product major, and department
WITH new_std AS (SELECT *,ROW_NUMBER() OVER (PARTITION BY major, department ORDER BY student_id) AS row_num FROM std)
DELETE FROM std WHERE student_id IN (SELECT student_id FROM new_std WHERE row_num > 1);
-- NOTE :: With thr group by method we cannot delete the duplicates as it gives the count of all occurence only

-- 47. SQl query to get the common records from two tables
-- *** Method 1 - using intersect (This might not be present in all sql version)
select * from std intersect select * from std_dup;
-- *** Method 2 - using join
SELECT std_dup.* FROM std INNER JOIN std_dup  ON std.student_id = std_dup.student_id;

-- 48. write a query to find all students who joined in the year 2020
select *, year(enrollment_date) from std where year(enrollment_date) = 2020;

-- 49. Write a query to fetch employees having the highest salary in each department
select * from std where GPA in (select max(GPA)  from std group by department);

-- 50. Write a query to fetch the first and last record from a table
-- *** Method 1 - using CTE
with std_up as (select *, row_number() over() as r_no from std)
select * from std_up where r_no = 1 union select * from std_up where r_no = (select max(r_no) from std_up);
-- *** Method 1 - using subquery
select * FROM (SELECT *, ROW_NUMBER() OVER() AS r_no FROM std) AS std_up WHERE r_no = 1 OR r_no = (SELECT MAX(r_no) 
FROM (SELECT ROW_NUMBER() OVER() AS r_no FROM std) AS temp);

-- 51. Write a query to find the total number of departments in the students table 
select count(distinct department) from std;
-- NOTE :: this includes NULL as one of the department
select count(distinct department) from std where department IS NOT NULL;

-- 52. Write a query to find the department with the lowest average GPA
select department, avg(GPA) from std group by department order by avg(GPA) limit 1;

-- 53. Write a query to delete all students from a department in one query
DELETE FROM std WHERE department IS NULL;

-- 54. Write a query to display all students who have been in the college for more than 2 years
select *, TIMESTAMPDIFF(YEAR, enrollment_date, CURDATE()) as yr_diff from std where TIMESTAMPDIFF(YEAR, enrollment_date, CURDATE()) > 2;

-- 55. write a query to remove all records from duplicate students table but keep the table structure
TRUNCATE TABLE std_dup;
select * from std_dup;

-- 56.  write a query to get the current month’s name
SELECT MONTHNAME(CURDATE()); 

-- 57. write a query to check if a table is empty
select CASE WHEN EXISTS (SELECT 1 FROM std) THEN 'Not Empty' ELSE 'Empty' END;

-- 58. write a query to find the second highest GPA for each department
select * from (select *, row_number() over (partition by department order by GPA) as seq from std) subq where seq = 2;

-- 59. Write a query to fetch students whose GPA is a multiple of 2
select * FROM std where GPA % 2 = 0;

-- 60. Write a query to update GPA of students based on their department
SET SQL_SAFE_UPDATES = 0;
UPDATE std SET GPA = CASE WHEN department = 'art' THEN GPA * 1.10 WHEN department = 'sci' THEN GPA * 1.05 ELSE GPA END ;
SET SQL_SAFE_UPDATES = 1;
/* NOTE :: The MySQL Error 1175 occurs in MySQL Workbench when you attempt to execute an UPDATE or DELETE query without a WHERE 
clause or with a non-restrictive condition. This behavior is a safety feature to prevent accidental updates or deletions of the 
entire table */

-- 61. Write a query to retreieve students details whose first names start and end with the same letter
select * FROM std WHERE LEFT(FIRST_NAME, 1) = RIGHT(FIRST_NAME, 1);

-- 62. Write a query to count the number of students whose first names start and end with the same letter
select count(*) FROM std WHERE LEFT(FIRST_NAME, 1) = RIGHT(FIRST_NAME, 1);

-- 63. Write a query to get students who belong to departments with less than 3 students
SELECT * FROM std WHERE department IN (SELECT department FROM std GROUP BY department HAVING COUNT(*) < 3);

-- 64. write a query to find students with the same first name
SELECT * FROM std WHERE first_name IN (SELECT first_name FROM std GROUP BY first_name HAVING COUNT(*) > 1);

-- 65. Write a query to list all students with more than 3 years of enrollment in each department
select *, TIMESTAMPDIFF(YEAR, enrollment_date, CURDATE()) as yr_diff from std where TIMESTAMPDIFF(YEAR, enrollment_date, CURDATE()) > 3;

-- 66. list all students details in departments that have not enrolled anyone in the past 2 years
SELECT * FROM std WHERE department IN (SELECT department FROM std GROUP BY department HAVING MAX(enrollment_date) < ADDDATE(CURDATE(), INTERVAL -2 YEAR));

-- 67. Write a query to find all students who scored more than the average GPA of their department
SELECT * FROM std e WHERE GPA > (SELECT AVG(GPA) FROM std WHERE std = e.std);

SELECT * FROM std WHERE GPA > (SELECT AVG(GPA) FROM std group by department);

-- 68. Write a query to find students whose GPA is in the top 10%
-- *** Method 1 - using subquery
SELECT * FROM std WHERE GPA >= (SELECT MAX(GPA) * 0.90 FROM std ); 
-- NOTE :: Above query calculates the threshold for the top 10% of salaries as 90% of the maximum salary (MAX(salary) * 0.90)
-- *** Method 2 - using CTE
WITH ranked_GPA AS (SELECT *,PERCENT_RANK() OVER (ORDER BY GPA DESC) AS percentile_rank FROM std)
SELECT * FROM ranked_GPA WHERE percentile_rank <= 0.10;

-- 69. Write a query to find the average GPA of the top 5 highest GPA students in each department
SELECT department, AVG(GPA) as aveg_gpa FROM (SELECT department, GPA,DENSE_RANK() OVER (PARTITION BY department ORDER BY GPA
DESC) AS ranks FROM std) AS ranked_std WHERE ranks <= 5 GROUP BY department;

-- 70. Write a query to calculate the percentage of employees in each department
SELECT department,(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM std)) AS percentage FROM std GROUP BY department;

-- 71. Query to add a new column name - email which contains email of the students
-- *** Method 1 - using update
ALTER TABLE std ADD COLUMN email VARCHAR(255);
SET SQL_SAFE_UPDATES = 0;
/* NOTE :: The MySQL Error 1175 occurs because the SQL_SAFE_UPDATES mode is enabled in MySQL Workbench. This mode prevents updates 
or deletes that do not include a WHERE clause or a condition involving indexed columns. Since the UPDATE query provided doesn't 
have a restrictive condition (like a WHERE clause), MySQL Workbench is throwing the error.*/
UPDATE std SET email = CONCAT(first_name, '_', last_name, '@gmail.com');
SET SQL_SAFE_UPDATES = 1;
select * FROM std;
-- *** Method 2 - using update + where
UPDATE std SET email = CONCAT(first_name, '_', last_name, '@gmail.com') WHERE first_name IS NOT NULL OR last_name IS NOT NULL;

-- 72. Write a query to find all students whose email contains the domain '@gmail.com'
select * FROM std WHERE email LIKE '%@gmail.com';

-- 73. Write a query to display the day of the week for each students
select *, DAYNAME(enrollment_date) AS day_of_week FROM std;

-- 74. Write a query to display the highest, lowest, and average GPA for each department
select department, MAX(GPA) AS highest_GPA, MIN(GPA) AS lowest_GPA, AVG(GPA) AS avg_GPA FROM std GROUP BY department;

-- 75. Write a query to show columns names of the table
SHOW COLUMNS FROM std; 

-- 76. Get all students details from students table whose "first_name" contains 'a'
SELECT * FROM std WHERE first_name like '%a%';

-- 77. Get all students detail from students table whose "first_name" start with any single character between 'a-p'
-- *** Method 1 - using like
SELECT * FROM std WHERE first_name like '[a-p]%';
/* NOTE :: MySQL does not directly support character ranges like [a-p] in LIKE clauses. For such ranges, you must use a regular 
expression with the REGEXP operator. Therefore use below query */
SELECT * FROM std WHERE first_name REGEXP '^[a-p]';
-- *** Method 2 - using between
SELECT * FROM std WHERE first_name between 'A' AND 'P';
-- *** Method 3 - using between and substr
SELECT * FROM std WHERE  SUBSTR(first_name, 1, 1) BETWEEN 'a' AND 'p';

-- 78. Get all students detail from students table whose "first_name" not start with any single character between 'a-p'
-- *** Method 1 - using like
SELECT * FROM std WHERE first_name like '[^a-p]%';
SELECT * FROM std WHERE first_name not like '[a-p]%';
/* NOTE :: Same explantion as above for like not working */
SELECT * FROM std WHERE first_name not REGEXP '^[a-p]';
SELECT * FROM std WHERE first_name REGEXP '^[a-p]';
-- *** Method 2 - using not between
SELECT * FROM std WHERE first_name not between 'A' AND 'P';
SELECT * FROM std WHERE first_name REGEXP '^[a-p]';
-- *** Method 3 - using between
SELECT * FROM std WHERE first_name between 'q' AND 'z';
-- *** Method 4 - using between and substr
SELECT * FROM std WHERE  SUBSTR(first_name, 1, 1) not BETWEEN 'a' AND 'p';

-- 79. Get all students detail from students table whose "Gender" end with 'le'and contain 4 letters
SELECT * FROM std WHERE Gender like '__le'; 
-- NOTE :: 1. The Underscore(_) Wildcard Character represents any single character
--         2. There are two "_"

-- 80. Get all students detail from students table whose "first_name" start with 'A' and contain 2 letters
SELECT * FROM std WHERE first_name like 'A__'; -- there are two "_"

-- 81. Get all students detail from students table whose "first_name" containing '%'. ex:-"Vik%as"
SELECT * FROM std WHERE first_name like '%[%]%';

-- 82. Get UTC date
/* UTC stands for Coordinated Universal Time. It is the primary time standard used worldwide to regulate clocks and time. 
UTC does not observe daylight saving time, making it consistent across the year. It is the same everywhere on Earth and 
is independent of time zones */
SELECT UTC_DATE() AS UTCDate;
SELECT UTC_TIMESTAMP() AS UTCTime; 
-- NOTE :: Above query gives utc date and time

-- 83. Get all students detail from students table after removing white spaces from right side
SELECT *, RTRIM(first_name) AS firstname FROM std;
-- NOTE :: If have to remove whitespaces from left side use LTRIM() and for both side use TRIM()

-- 84. Get all students detail from students table where "first_name" is prifixed with "Hello"
SELECT *, concat('Hello ', first_name) FROM std;
-- NOTE :: Dont use 'Hello ' + first_name in mysql

/* 85. Get all students detail from students and scholarship table for all students if scholarship is not assigned then display 
"-No scholarship Assigned" */
SELECT a.*, COALESCE(b.SCHOLARSHIP_TYPE, '-No scholarship Assigned') FROM std a LEFT OUTER JOIN scholar b
ON a.STUDENT_ID = b.STUDENT_REF_ID;

-- 86. Write a query to find out the project name which is not assigned to any students
SELECT a.*, b.first_name FROM project_details a left OUTER JOIN std b ON a.StudentID = b.STUDENT_ID WHERE first_name IS NULL; 

-- 87. Write down the query to fetch all students & Project detail who has been assigned more than one project
Select a.*, b.* from std a INNER JOIN project_details b ON a.STUDENT_ID = b.StudentID WHERE StudentID IN (SELECT EmployeeDetailID 
FROM [ProjectDetail] GROUP BYEmployeeDetailID HAVING COUNT(*) >1 );

-- 88. Write down the query to fetch ProjectName on which more than one employee are working along with EmployeeName
Select P.ProjectName, E.FName from ProjectDetails P INNER JOIN EmployeeDetails E
on p.EmployeId = E.Id where P.ProjectName in(select ProjectName from ProjectDetailsgr
oup by ProjectName having COUNT(1)>1)

-- page 22 start - safar page

SHOW COLUMNS FROM std; 

use DB_21dec;
select * from std;
DESCRIBE std;










