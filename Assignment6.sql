/* Create a table grade_points (grade, points) that maps letter grades to number grades. */

CREATE TABLE grade_points(
	grade VARCHAR(2),
    points DECIMAL(2,1),
    PRIMARY KEY (grade),
    CONSTRAINT chk_points CHECK (points >= 0.0 AND points <= 4.0)
);

/* Populate the table with the respective grades and their point values */
INSERT INTO grade_points (grade, points) VALUES
('A', 4.0),
('A-', 3.7),
('B+', 3.3),
('B', 3.0),
('B-', 2.7),
('C+', 2.3),
('C', 2.0),
('C-', 1.7),
('D+', 1.3),
('D', 1.0),
('D-', 0.7),
('F', 0.0);

/* Add a foreign key from the grade column in the existing takes table to the new grade_points table. */
ALTER TABLE takes
ADD FOREIGN KEY (grade) REFERENCES grade_points(grade);

/* Create a view v_takes_points that returns the data in takes table along with the numeric equivalent of the grade. */
CREATE VIEW v_takes_points AS
SELECT t.*, gp.points
FROM takes t
JOIN grade_points gp ON t.grade = gp.grade;

/* Return all the columns from the takes table along with the corresponding numeric points for each grade */
SELECT * FROM v_takes_points;



/* Compute the total number of grade points (credits * grade points) earned by student X (00128) */
SELECT
    COALESCE(SUM(c.credits * gp.points), 0) AS total_grade_points
FROM
    takes t
LEFT JOIN
    course c ON t.course_id = c.course_id
LEFT JOIN
    grade_points gp ON t.grade = gp.grade
WHERE
    t.ID = '00128';

/* Compute the GPA - i.e. total grade points / total credits -  for the same student in the previous question.
 */
 SELECT
    COALESCE(SUM(c.credits * gp.points), 0) / NULLIF(SUM(c.credits), 0) AS GPA
FROM
    takes t
LEFT JOIN
    course c ON t.course_id = c.course_id
LEFT JOIN
    grade_points gp ON t.grade = gp.grade
WHERE
    t.ID = '00128';



/* Find the GPA of all students, i.e. not just for one student at a time. */
SELECT
    t.ID,
    COALESCE(SUM(c.credits * gp.points), 0) AS total_grade_points,
    COALESCE(SUM(c.credits), 0) AS total_credits,
    CASE
        WHEN SUM(c.credits) > 0 THEN SUM(c.credits * gp.points) / SUM(c.credits)
        ELSE 0
    END AS gpa
FROM
    takes t
LEFT JOIN
    course c ON t.course_id = c.course_id
LEFT JOIN
    grade_points gp ON t.grade = gp.grade
GROUP BY
    t.ID;

/* Create a view v_student_gpa (id, gpa) that gives a dynamic version of the information in the previous question.*/
CREATE VIEW v_student_gpa AS
SELECT
    t.ID AS id,
    CASE
        WHEN SUM(c.credits) > 0 THEN SUM(c.credits * gp.points) / SUM(c.credits)
        ELSE 0
    END AS gpa
FROM
    takes t
LEFT JOIN
    course c ON t.course_id = c.course_id
LEFT JOIN
    grade_points gp ON t.grade = gp.grade
GROUP BY
    t.ID;

/* Display the student IDs and their corresponding GPAs */
SELECT * FROM v_student_gpa;