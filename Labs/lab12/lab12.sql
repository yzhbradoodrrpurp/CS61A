CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

CREATE TABLE sharing AS
  with remove_exclusive as (
    select hall from finals
    group by hall having count(*) > 1
  )
    select course, count(*) as shared from
    finals where hall in (select hall from remove_exclusive)
    group by course;

CREATE TABLE pairs AS
  select a.room || ' and ' || b.room || ' together have ' ||  (a.seats + b.seats) || ' seats' as rooms
    from sizes as a, sizes as b
    where a.seats + b.seats >= 1000 and a.room < b.room
    order by a.seats + b.seats desc;

CREATE TABLE big AS
  SELECT course from finals join sizes on hall = room
    group by course having sum(seats) >= 1000;

CREATE TABLE remaining AS
  SELECT course, (sum(seats) - max(seats)) as remaining from
    finals join sizes on hall = room
    group by course;

