Create Table CITIES (
  city_code int Primary Key,
  city_name varchar,
  state_name varchar,
  zip_code int
);

Create Table USERS (
  user_id int Primary Key,
  first_name varchar,
  second_name varchar,
  email varchar,
  phone int,
  created_at timestamp,
  city_code int ForeignKey References CITIES(city_code) 
);

Create Table THEATERS (
  theater_id int Primary Key,
  theater_name varchar,
  city_code int ForeignKey References CITIES(city_code)
);

Create Table FOODBEVERAGES (
  food_id int Primary Key,
  food_name varchar,
  food_price double,
  theater_id int ForeignKey References THEATERS(theater_id)
);

Create Table THEATER_ROOMS (
  room_id int Primary Key,
  room_name varchar,
  theater_id int ForeignKey References THEATERS(theater_id),
  total_seats int
);

Create Table THEATER_SEATS (
  seat_id int Primary Key,
  room_id int ForeignKey References THEATER_ROOMS(room_id),
  seat_row varchar,
  seat_number int,
  seat_type varchar
);

Create Table SEATS_FOR_SHOW (
  show_seat_id int Primary Key,
  available boolean,
  price double,
  seat_id int ForeignKey References THEATER_SEATS(seat_id),
  show_id int ForeignKey References SHOWS(show_id),
  booking_id int ForeignKey References BOOKINGS(booking_id)
);

Create Table FOOD_FOR_BOOKING (
  food_id int Primary Key ForeignKey References FOODBEVERAGES(food_id),
  quantity int,
  cost double,
  pickup datetime,
  booking_id int ForeignKey References BOOKINGS(booking_id)
);

Create Table BOOKINGS (
  booking_id int Primary Key,
  time_stamp datetime,
  number_of_seats int,
  total_cost double,
  booking_complete boolean,
  user_id int ForeignKey References USERS(user_id),
  show_id int ForeignKey References SHOWS(show_id)
);

Create Table SHOWS (
  show_id int Primary Key,
  start_time datetime,
  end_time datetime,
  available_seats int,
  theater_room_id int ForeignKey References THEATER_ROOMS(room_id),
  movie_id int ForeignKey References MOVIES(movie_id)
);

Create Table MOVIES (
  movie_id int Primary Key,
  name varchar,
  description varchar,
  image varbinary,
  trailer varbinary,
  genre varchar,
  audience_rating_level varchar,
  language varchar,
  duration timestamp,
  imdb_rating double,
  rotten_tomatoes_rating int
);


