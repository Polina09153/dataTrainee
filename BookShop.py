import csv
import mysql.connector
from faker import Faker



def generate_book_data(num_books=100):
    fake = Faker()
    book_data = []
    for _ in range(num_books):
        title = fake.sentence(nb_words=3, variable_nb_words=True)[:-1]
        author = f"{fake.first_name()} {fake.last_name()}"
        genre = fake.random_element(['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Romance', 'Mystery', 'Thriller'])
        rating = round(fake.pyfloat(left_digits=1, right_digits=1, positive=True), 1)
        review = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
        book_data.append([title, author, genre, rating, review])
    return book_data

book_data = generate_book_data(100)

with open('books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'author', 'genre', 'rating', 'review'])
    writer.writerows(book_data)

host = "localhost"
user = "root"
password = "#######"
database = "BOOKSHOP"
db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = db.cursor()

with open('books.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("SELECT id_author FROM author WHERE name_author = %s", (row['author'],))
        author_id = cursor.fetchone()
        if not author_id:
            cursor.execute("INSERT INTO author (name_author) VALUES (%s)", (row['author'],))
            author_id = cursor.lastrowid
        else:
            author_id = author_id[0]

        cursor.execute("SELECT id_genre FROM genre WHERE name_genre = %s", (row['genre'],))
        genre_id = cursor.fetchone()
        if not genre_id:
            cursor.execute("INSERT INTO genre (name_genre) VALUES (%s)", (row['genre'],))
            genre_id = cursor.lastrowid
        else:
            genre_id = genre_id[0]

        cursor.execute("INSERT INTO book (title, id_author, id_genre, rating, review) VALUES (%s, %s, %s, %s, %s)",
                       (row['title'], author_id, genre_id, row['rating'], row['review']))

db.commit()

cursor.execute("SELECT title, rating FROM book ORDER BY rating DESC LIMIT 10")
popular_books = cursor.fetchall()
print("10 most popular books:")
for book in popular_books:
    print(f"{book[0]} - Rating: {book[1]}")


cursor.execute("SELECT genre.name_genre, COUNT(*) AS count FROM book JOIN genre ON book.id_genre = genre.id_genre GROUP BY genre.name_genre  ORDER BY count DESC LIMIT 10")
popular_genres = cursor.fetchall()
print("\n10 most popular genres:")
for genre, count in popular_genres:
    print(f"{genre}: {count}")



db.close()
