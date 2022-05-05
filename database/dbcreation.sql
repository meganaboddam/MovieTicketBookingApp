Table USERS {
  user_id int PK
  first_name varchar
  second_name varchar
  email email
  phone phone
  created_at timestamp
  city_code int [ref: > CITIES.city_code]
}

Table CITIES {
  city_code int PK
  city_name varchar
  state_name varchar
  zip_code int
}

Table THEATERS {
  theater_id int PK
  theater_name varchar
  city_code int [ref: > CITIES.city_code]
}

Table FOODBEVERAGES {
  food_id int PK
  food_name varchar
  food_price double
  theater_id int [ref: > THEATERS.theater_id]
}

Table THEATER_ROOMS {
  room_id int PK
  room_name varchar
  theater_id int [ref: > THEATERS.theater_id]
  total_seats int
}

Table THEATER_SEATS {
  seat_id int PK
  room_id int [ref: > THEATER_ROOMS.room_id]
  seat_row varchar
  seat_number int
  seat_type varchar
}

Table SEATS_FOR_SHOW {
  show_seat_id int PK
  available boolean
  price double
  seat_id int [ref: > THEATER_SEATS.seat_id]
  show_id int [ref: > SHOWS.show_id]
  booking_id int [ref: > BOOKINGS.booking_id]
}

Table FOOD_FOR_BOOKING {
  food_id int PK [ref: > FOODBEVERAGES.food_id]
  quantity int
  cost double
  pickup datetime
  booking_id int [ref: > BOOKINGS.booking_id]
}

Table BOOKINGS {
  booking_id int PK
  time_stamp datetime
  number_of_seats int
  total_cost double
  booking_complete boolean
  user_id int [ref: > USERS.user_id]
  show_id int [ref: > SHOWS.show_id]
}

Table SHOWS {
  show_id int PK
  start_time datetime
  end_time datetime
  available_seats int
  theater_room_id int [ref: > THEATER_ROOMS.room_id]
  movie_id int [ref: > MOVIES.movie_id]
}

Table MOVIES {
  movie_id int PK
  name varchar
  description varchar
  image varbinary
  trailer varbinary
  genre varchar
  audience_rating_level varchar
  language varchar
  duration timestamp
  imdb_rating double
  rotten_tomatoes_rating int
}


