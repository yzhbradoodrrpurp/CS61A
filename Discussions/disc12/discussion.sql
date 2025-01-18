/*
The pizzas table contains the names, opening, and closing hours
of great pizza places in Berkeley. The meals table contains typical
meal times (for college students). A pizza place is open for a
meal if the meal time is at or within the open and close times.
*/

CREATE TABLE pizzas AS
  SELECT 'Artichoke' AS name, 12 AS open, 15 AS close UNION
  SELECT 'La Vals'         , 11        , 22          UNION
  SELECT 'Sliver'           , 11        , 20          UNION
  SELECT 'Cheeseboard'      , 16        , 23          UNION
  SELECT 'Emilias'         , 13        , 18;

CREATE TABLE meals AS
  SELECT 'breakfast' AS meal, 11 AS time UNION
  SELECT 'lunch'            , 13         UNION
  SELECT 'dinner'           , 19         UNION
  SELECT 'snack'            , 22;


-- Pizza places that open before 1pm in alphabetical order
create table opening as
    select name from pizzas where open < 13
    order by name desc;


/*
You're planning to study at a pizza place from the moment it opens until 14 o'clock (2pm).
Create a table study with two columns, the name of each pizza place and the duration
of the study session you would have if you studied there (the difference between
when it opens and 14 o'clock). For pizza places that are not open before 2pm,
the duration should be zero. Order the rows by decreasing duration.
*/

create table study as
    select name, max(14 - open, 0) as duration from pizzas
    order by duration desc;


create table late as
    select name || ' closes at ' || close as status
    from pizzas, meals where meal = 'snack' and close >= time;


create table double as
    select a.meal as first, b.meal as second, name
    from meals as a, meals as b, pizzas
    where b.time - a.time > 6 and a.time >= pizzas.open and b.time < pizzas.close;
