INSERT INTO CITIES VALUES 
    (1, "Seattle", "WA", 98101),
    (3, "Kirkland", "WA", 98083),
    (5, "Redmond", "WA", 98073);

INSERT INTO USERS VALUES 
    (1, "Jane", "Austen", "jane.austen@gmail.com", 9068923672, '2022-05-06 08:30:01', 1),
    (2, "Mary", "Fanny", "marylovescats@yahoo.com", 3064520670, '2022-05-06 07:37:01', 3),
    (3, "Dirk", "Willistenshmith", "dwillistenshmith@gmail.com", 3062224492, '2022-05-06 10:14:12', 3),
    (4, "Tree", "Kardashian", "kardashianstreehug@gmail.com", 4251234672, '2022-05-06 03:59:31', 5);

INSERT INTO THEATERS VALUES
    (1, "Cinemark", 1),
    (2, "Cinemark", 3),
    (3, "Lincoln Memorial Theater", 1),
    (4, "Regal", 1),
    (5, "Neptune Theaters", 5);

INSERT INTO FOODBEVERAGES VALUES 
    (1, "Butter Popcorn (Small)", 5.00, 2),
    (2, "Butter Popcorn (Medium)", 10.00, 2),
    (3, "Butter Popcorn (Large)", 15.00, 2);

INSERT INTO THEATER_ROOMS VALUES
    (1, "Screen Room A", 2, 50),
    (2, "Screen Room B", 2, 100),
    (2, "Screen Room C", 2, 150);

INSERT INTO THEATER_SEATS VALUES
    (1, 2, "A", 1, "Regular"),
    (5, 2, "B", 9, "Regular"),
    (12, 2, "D", 3, "Premium"),
    (13, 2, "E", 4, "Delux");

-- show_seat_id, available (1-true, 0-false), price, 
-- seat_id, show_id, booking_id (0-no booking yet)
INSERT INTO SEATS_FOR_SHOW VALUES 
    (1, 1, 15.00, 1, 1, 0),
    (2, 1, 15.00, 5, 1, 0),
    (3, 1, 20.00, 12, 1, 0),
    (4, 1, 25.00, 13, 1, 0);

-- show_id, date, start_time, end_time, available_seats,
-- theater_room_id, movie_id 
INSERT INTO SHOWS VALUES 
    (1, '2022-06-01', '12:30:00', '14:20:00', 3, 1, 1),
    (2, '2022-06-01', '15:45:00', '17:35:00', 3, 1, 1),
    (3, '2022-06-01', '20:00:00', '21:50:00', 3, 1, 1),
    (4, '2022-06-02', '12:30:00', '14:20:00', 3, 1, 1),
    (5, '2022-06-03', '12:30:00', '14:20:00', 3, 1, 1)
    (6, '2022-06-01', '12:30:00', '15:29:00', 3, 3, 2),
    (7, '2022-06-02', '12:30:00', '15:29:00', 3, 3, 2),
    (8, '2022-06-03', '12:30:00', '15:29:00', 3, 3, 2);

INSERT INTO MOVIES VALUES 
    (1, "Top Gun: Maverick", 
    "After more than 30 years of service as one of the Navy's top aviators, Pete Maverick Mitchell is 
    where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank 
    that would ground him. Training a detachment of graduates for a special assignment, Maverick must 
    confront the ghosts of his past and his deepest fears, culminating in a mission that demands the 
    ultimate sacrifice from those who choose to fly it.",
    "image", "trailer", "Action", "PG-13", "English", '01:50:00', 7, 80),
    (2, "Pushpa: The Rise - Part 1", 
    "Violence erupts between red sandalwood smugglers and the police charged with bringing down their 
    organisation in the Seshachalam forests of South India.",
    "image", "trailer", "Adventure/Romance", "NC-17", "Telugu", '02:59:00', 9, 75);

