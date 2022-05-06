INSERT INTO CITIES VALUES 
    (1, "Seattle", "WA", 98101),
    (2, "Seattle", "WA", 98102),
    (3, "Kirkland", "WA", 98083),
    (4, "Woodinville", "WA", 98072),
    (5, "Redmond", "WA", 98073),
    (6, "Sammamish", "WA", 98074),
    (7, "Bellevue", "WA", 98006),
    (8, "Bothell", "WA", 98011),
    (9, "Edmonds", "WA", 98026),
    (10, "Issaquh", "WA", 98027);

INSERT INTO USERS VALUES 
    (1, "Jane", "Austen", "jane.austen@gmail.com", 9068923672, '2022-05-06 08:30:01', 1),
    (2, "Mary", "Fanny", "marylovescats@yahoo.com", 3064520670, '2022-05-06 07:37:01', 2),
    (3, "Dirk", "Willistenshmith", "dwillistenshmith@gmail.com", 3062224492, '2022-05-06 10:14:12', 2),
    (4, "Tree", "Kardashian", "kardashianstreehug@gmail.com", 4251234672, '2022-05-06 03:59:31', 7),
    (5, "Peace", "Hipper", "hiphippeace@yahoo.com", 4257776243, '2022-05-06 08:30:01', 7),
    (6, "John", "Doe", "johnnyboidoe@hotmail.com", 4258358361, '2022-05-06 08:30:01', 7),
    (7, "Karl", "Markson", "karljuniormarkson@gmail.com", 1150009888, '2022-05-06 08:30:01', 4),
    (8, "Ming", "Kim", "mingquiankim.austen@yahoo.com", 1158113678, '2022-05-06 08:30:01', 4),
    (9, "Buster", "Rottwieler", "rottwielerbuster@gmail.com", 3069922463, '2022-05-06 08:30:01', 2),
    (10, "Shawn", "Mendes", "shawnkmendes@gmail.com", 3063063066, '2022-05-06 08:30:01', 2),
    (11, "Camilla", "CabelLo", "cabellocamillajane@gmail.com", 4253322000, '2022-05-06 08:30:01', 3),
    (12, "Taylor", "Swift", "tayswift@gmail.com", 4252379844, '2022-05-06 18:03:00', 7)
    (13, "Taylor", "Lautner", "lautner.taylor@aol.com", 4255221983, '2022-05-06 12:10:24', 7)
    (14, "Lila Reddy", "Chandra", "lila123reddy@aol.com", 4250927320, '2022-05-06 09:32:41', 7);

INSERT INTO THEATERS VALUES
    (1, "Cinemark", 1),
    (2, "Cinemark Bellevue", 3),
    (3, "Linocoln Memorial Theater", 3),
    (4, "Regal", 3),
    (5, "Neptune Theaters", 3);

INSERT INTO FOODBEVERAGES VALUES 
    (1, "Butter Popcorn (Small)", 4.99, 5),
    (2, "Butter Popcorn (Medium)", 8.99, 5),
    (3, "Butter Popcorn (Large)", 13.99, 5),
    (4, "Caramel Popcorn (Small)", 5.99, 5),
    (5, "Butter Popcorn (Medium)", 9.99, 5),
    (6, "Butter Popcorn (Large)", 14.99, 5),
    (7, "Fountain Drink (Small)", 2.99, 5),
    (8, "Fountain Drink (Medium)", 3.99, 5),
    (9, "Fountain Drink (Large)", 4.99, 5),
    (10, "Dasani Water Bottle", 1.99, 5);

INSERT INTO THEATER_ROOMS VALUES
    (1, "Screen Room A1", 5, 50),
    (2, "Screen Room A2", 5, 50),
    (3, "Screen Room A3", 5, 50),
    (4, "Screen Room B", 5, 100),
    (5, "Screen Room C", 5, 150),
    (6, "Screen Room D", 5, 100),
    (7, "Screen Room E", 5, 40);

INSERT INTO THEATER_SEATS VALUES
    (1, 2, "A", 1, "Regular"),
    (2, 2, "A", 2, "Regular"),
    (3, 2, "A", 3, "Regular"),
    (4, 2, "B", 8, "Regular"),
    (5, 2, "B", 9, "Regular"),
    (6, 2, "B", 10, "Regular"),
    (7, 2, "C", 1, "Regular"),
    (8, 2, "C", 6, "Premium"),
    (9, 2, "C", 7, "Premium"),
    (10, 2, "D", 1, "Premium"),
    (11, 2, "D", 2, "Premium"),
    (12, 2, "D", 3, "Premium"),
    (13, 2, "E", 4, "Delux"),
    (14, 2, "E", 5, "Delux"),
    (15, 2, "E", 6, "Delux");

