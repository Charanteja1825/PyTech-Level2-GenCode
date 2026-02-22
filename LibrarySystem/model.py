class Book:
    def __init__(self, book_id, title, issued=False):
        self.book_id = book_id
        self.title = title
        self.issued = issued

    def to_string(self):
        return f"{self.book_id},{self.title},{self.issued}\n"


def load_books():
    books = []
    try:
        with open("data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    bid, title, issued = parts
                    books.append(Book(bid, title, issued == "True"))
    except FileNotFoundError:
        pass
    return books


def save_all_books(books):
    with open("data.txt", "w") as f:
        for book in books:
            f.write(book.to_string())