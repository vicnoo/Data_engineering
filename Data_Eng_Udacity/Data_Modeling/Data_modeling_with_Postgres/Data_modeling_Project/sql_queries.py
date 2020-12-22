# Fact Table

# songplays - records in log data associated with song plays i.e. records with page NextSong
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

# Dimension Tables

# users - users in the app
# user_id, first_name, last_name, gender, level
# songs - songs in music database
# song_id, title, artist_id, year, duration
# artists - artists in music database
# artist_id, name, location, latitude, longitude
# time - timestamps of records in songplays broken down into specific units
# start_time, hour, day, week, month, year, weekday

# DROP TABLES
#Fact table
songplays_table_drop = "DROP TABLE IF EXISTS songplays"
# Dimmension tables
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplays_table_create = ("""
                         CREATE TABLE IF NOT EXISTS songplays
                         (songplays_id int PRIMARY KEY,
                          start_time date REFERENCES time(start_time),
                          user_id int NOT NULL REFERENCES users(user_id),
                          level text,
                          song_id text REFERENCES songs(song_id),
                          artist_id text REFERENCES artists(artist_id),
                          session_id int,
                          location text,
                          user_agent text)
                        """)

users_table_create = ("""
                      CREATE TABLE IF NOT EXISTS users
                      (user_id int PRIMARY KEY,
                       first_name text NOT NULL,
                       last_name text NOT NULL,
                       gender text,
                       level text)
                      """)

songs_table_create = ("""
                      CREATE TABLE IF NOT EXISTS songs
                      (song_id text PRIMARY KEY,
                       title text NOT NULL,
                       artist_id texT NOT NULL REFERENCES artists(artist_id),
                       year int,
                       duration float NOT NULL)
                      """)

artists_table_create = ("""
                        CREATE TABLE IF NOT EXISTS artists
                        (artist_id text PRIMARY KEY,
                         name text NOT NULL,
                         location text,
                         latitude float,
                         longitude float)
                        """)

time_table_create = ("""
                     CREATE TABLE IF NOT EXISTS time
                     (start_time date PRIMARY KEY,
                      hour int,
                      day int,
                      week int,
                      month int,
                      year int,
                      weekday text)
                     """)

# INSERT RECORDS 

songplays_table_insert = ("""
                         INSERT INTO songplays
                         (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                         ON CONFLICT (songplay_id) DO NOTHING;
                         """)

users_table_insert = ("""
                      INSERT INTO users
                      (user_id, first_name, last_name, gender, level)
                      VALUES (%s, %s, %s, %s, %s)
                      ON CONFLICT (user_id) DO NOTHING;
                      """)

songs_table_insert = ("""
                      INSERT INTO songs
                      (song_id, title, artist_id, year, duration)
                      VALUES (%s, %s, %s, %s, %s)
                      ON CONFLICT (song_id) DO NOTHING;
                      """)

artists_table_insert = ("""
                        INSERT INTO artists
                        (artist_id, name, location, latitude, longitude)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (artist_id) DO NOTHING;
                        """)

time_table_insert = ("""
                     INSERT INTO time
                     (start_time, hour, day, week, month, year, weekday)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)
                     ON CONFLICT (start_time) DO NOTHING;
                     """)

# FIND SONGS

song_select = ("""
               SELECT song_id, artists.artist_id, 
               FROM songs JOIN artists ON songs.artist_id = artists.artist_id
               WHERE songs.title = %s
               AND artist.name = %s
               AND songs.duration = %s
               """)

# QUERY LIST
create_table_queries = [users_table_create, artists_table_create, songs_table_create, time_table_create, songplays_table_create]
drop_table_queries = [users_table_drop, artists_table_drop, songs_table_drop, time_table_drop, songplays_table_drop]