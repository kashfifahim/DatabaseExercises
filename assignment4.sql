/* Chapter 3, Slide 52: List all departments along with the number of instructors in each department */
select dept_name,
             ( select count(*)
                from instructor
                where department.dept_name = instructor.dept_name)
             as num_instructors
from department;


/* Chapter 3, Slide 14: Find the department names of all instructors, and remove duplicates */
select distinct dept_name
from instructor;


/* Chapter 3, Slide 24, List in alphabetic order the names of all instructors */
select distinct name
from instructor
order by name;

/* Chapter 3, Slide 22, Find the names of all instructors whose name includes the substring “dar” */
select name
from instructor
where name like '%dar%';

/* Chapter 3, Slide 19, Find the names of all instructors who have taught some course and the course_id */
select name, course_id
from instructor , teaches
where instructor.ID = teaches.ID;

/* Chapter 3, Slide 19, Find the department names of all instructors, and remove duplicates */
select name, course_id
from instructor , teaches
where instructor.ID = teaches.ID and instructor. dept_name = 'Art';

/* Chapter 3, Slide 20, Find the names of all instructors who have a higher salary than some instructor in 'Comp. Sci'*/
select distinct T.name
from instructor as T, instructor as S
where T.salary > S.salary and S.dept_name = 'Comp. Sci.';

/* Chapter 3, Slide 14, Find the department names of all instructors, and remove duplicates */
select distinct dept_name
from instructor;

/* Chapter 3, Slide 14, The keyword all specifies that duplicates should not be removed. */
select all dept_name
from instructor;

/* Chapter 3, Slide 16, The select clause can contain arithmetic expressions */
select ID, name, salary/12
from instructor;

/* Chapter 3, Slide 17, To find all instructors in Comp. Sci. dept */
select name
from instructor
where dept_name = 'Comp. Sci.';

/* Chapter 3, Slide 17, To find all instructors in Comp. Sci. dept with salary > 80000 */
select name
from instructor
where dept_name = 'Comp. Sci.' and salary > 80000;

/* Homework query #1: Retrieve all courses with 'a', 'e', 'i' in that order in their names */
SELECT title
FROM course
WHERE title REGEXP 'a.*e.*i';

/* Homework query #2: Retrieve all courses with 'a', 'e', 'i' in any order in their names */
select title
from course
where title like '%a%' and title like '%e%' and title like '%i%';

/* Homework query #3: Retrieve names of students who failed a course and the course name */
select student.name, course.title
from student, takes, course
where student.ID = takes.ID and takes.course_id = course.course_id and takes.grade = 'F';

/* Homework query #4: Retrieve percentage of A grades compared to all courses */
select (count(case when grade = 'A' then 1 end) / count(*)) * 100 as Percent_A
from takes;

/* Homework query #5: Retrieve names and numbers of courses without prerequisites */
select title, course_id
from course
where course_id not in (select distinct course_id from prereq);

/* Homework query #6: Retrieve names of students and their advisors, if any */
select student.name, advisor.name as advisor_name
from student
left join advisor on student.ID = advisor.s_id;