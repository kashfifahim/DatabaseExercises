drop table if exists math_shape2d;
/* 2a. Create a new table shape2d with columns: shape_id, shape_name, perimeter_formula, area_formula */
CREATE TABLE math_shape2d(
	shape_id INT NOT NULL AUTO_INCREMENT primary key,
    shape_name varchar(30),
    perimeter_formula varchar(30),
    area_formula varchar(30)
);

/* 2b.  Insert rows into the shape2d table, at least one of which should involve π. */
insert into math_shape2d(shape_name, perimeter_formula, area_formula)
values('Rectangle', '2 * Length + 2 * Width', 'Length * Width');

INSERT INTO math_shape2d (shape_name, perimeter_formula, area_formula)
VALUES ('Triangle', 'Length + Length + Length', '(Base * Height) / 2');

insert into math_shape2d(shape_name, perimeter_formula, area_formula)
values('Square', 'Length * 4', 'Length * Length');

insert into math_shape2d(shape_name, perimeter_formula, area_formula)
values('Circle', '2 * π * Radius', 'π * Radius * Radius');

insert into math_shape2d(shape_name, perimeter_formula, area_formula)
values('Ellipse', 'π * (Semi-major + Semi-minor)', 'π * Semi-minor');

insert into math_shape2d(shape_name, perimeter_formula, area_formula)
values('Parallelogram', '2 * (Side1 + Side2)', 'Base * Height');

select * from math_shape2d;

drop table if exists math_shape3d;
/* [3a] Create a new table shape3d with columns: shape_id, shape_name, area_formula, volume_formula */
CREATE TABLE math_shape3d(
shape_id INT NOT NULL AUTO_INCREMENT primary key,
shape_name VARCHAR(30),
area_formula varchar(30),
volume_formula varchar(30));

/* [3b] Insert two rows into the shape3d table, at least one of which should involve π. */
insert into math_shape3d(shape_name, area_formula, volume_formula)
values('Cuboid', '2 * (lb + bh + hl)', 'l*b*h'),
('Sphere', '4 * π * r * r', '(4/3) * π * r * r * r'),
('Hemisphere', '3 * π * r * r', '(2/3) * π * r * r * r'),
('Cylinder', '(2πrh) + (2πrr)', 'πrrh');

/* [Check] Show all rows */
select * from math_shape2d;

/* [Check] Show all rows */
select * from math_shape3d;

DROP FUNCTION IF EXISTS math_area_circle;
/* [4a] Create a MySQL function area_circle(radius) that computes the area of a circle of given radius */
CREATE FUNCTION math_area_circle(radius INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    SET @area = 3.14 * radius * radius##
    RETURN @area##
END;

/* TESTING AREA OF CIRCLE FUNCTION -- WORKED */
SELECT math_area_circle(2) from dual;

DROP FUNCTION IF EXISTS volume_sphere;
/* [4b] Create a MySQL function volume_sphere(radius) that computes the volume of a sphere of given radius */
CREATE FUNCTION math_volume_sphere(radius DOUBLE)
RETURNS DOUBLE
DETERMINISTIC
BEGIN
    SET @volume = (4.0/3.0) * 3.14159265359 * radius * radius * radius##
    RETURN @volume##
END;

/* TESTING VOLUME OF CIRCLE FUNCTION -- WORKED */
SELECT math_volume_sphere(2) from dual;

drop table if exists math_circle;
/* [5a] Create a table circle with columns circle_id, total_points, circle_points, pi_estimate */
CREATE TABLE math_circle (
    circle_id INT AUTO_INCREMENT PRIMARY KEY,
    total_points INT,
    circle_points INT,
    pi_estimate DOUBLE
);

drop table if exists math_point;
/* [5b] Create a table point with columns point_id, circle_id, x, y. */
CREATE TABLE math_point (
    point_id INT AUTO_INCREMENT PRIMARY KEY,
    circle_id INT,
    x DOUBLE,
    y DOUBLE,
    FOREIGN KEY (circle_id) REFERENCES circle(circle_id)
);

/* Test 5b */
SELECT * FROM math_point;

/* [5c] Create a stored procedure random_points(n) that generates n random points (x, y) where both x and y are in the interval (-1, 1). The MySQL function rand() returns a random number between 0 and 1. To get a random number in (-1, 1), use 2 * rand() - 1. SET @x =  2 * rand() - 1 and SET @y = 2 * rand() - 1. Then insert those as a row in table point. */
CREATE PROCEDURE math_generate_points(num_points INT, circle_id INT)
BEGIN
SET @n = 0##
find_points: LOOP
IF @n > num_points THEN LEAVE find_points##
END IF##
SET @x=2*rand()-1##
SET @y=2*rand()-1##
INSERT INTO point(circle_id, x, y) VALUES(circle_id, @x, @y)##
SET @n = @n + 1##
END LOOP find_points##


/* Test random_points */
SELECT math_generate_points(2, 2) from dual;






