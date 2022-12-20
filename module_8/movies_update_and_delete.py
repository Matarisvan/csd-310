import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Mysql21",
    "host": "127.0.0.1",
    "port": "3006",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...\n")

    cursor = db.cursor()
    
    # ref function
    def show_films(cursor, title):
        cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
        films = cursor.fetchall()
        print("\n -- {} --".format (title))
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))
    
    # calling the first function
    show_films(cursor, "DISPLAYING FILMS")    
    
    # insert new film
    def insert_film(cursor):
        cursor.execute("insert into film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES('Ice Age', '2002', '81', 'Chris Wedge', '1', '2');")
    insert_film(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # update film alien
    def update_film(cursor):
        cursor.execute("update film set genre_id = 1 where film_name = 'Alien';")
    update_film(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # delete film gladiator
    def delete_film(cursor):
        cursor.execute("delete from film where film_name = 'Gladiator';")
    delete_film(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")    


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    db.close()

