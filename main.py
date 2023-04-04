from database import Database
from save_json import writeAJson
from model import BookModel

db = Database(database="relatorio5", collection="books")
book_model = BookModel(db)

book1 = book_model.create_book("O lado feio do amor", "Collen  Hoover", 2014, 35.70)
book2 = book_model.create_book("O mundo de Sofia", " Josten Garrder", 2012, 44.90)
book3 = book_model.create_book("A revolução dos bichos", "George Orwell", 2007, 11.50)
book4 = book_model.create_book("Sapiens", "Yuval Noah Harari", 2020, 52.00)

#Realizando a leitura dos livros
read_book = book_model.read_book_by_id(book1)
read_book1 = book_model.read_book_by_id(book2)
read_book2 = book_model.read_book_by_id(book3)
read_book3 = book_model.read_book_by_id(book4)
writeAJson((read_book,read_book1,read_book2, read_book3), "Acervo_de_liivros")

#Realizando a atualizacao de dados de um determinado livro
updatebook = book_model.update_book(book3, "1984", "George Orwell", 2007, 11.50)
updatebook1 = book_model.update_book(book4, "HomoDeus", "Yuval Noah Harari", 2020, 52.00)

#Realizando a exclusao de um livro do Bando de Dados
delete_book = book_model.delete_book(book2)