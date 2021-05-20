from app.models import Book, Session


def find_books(search_text):
    try:
        result = []
        sess = Session()
        # books = sess.query(Book).filter(Book.name.contains(search_text)).order_by(Book.name).all()
        # result = [a.to_dict() for a in books]
        # %' or 1=1 or '%
        query = "SELECT * FROM book WHERE name like '%"+search_text+"%'"
        print(query)
        books = sess.execute(query)
        result = [{column: value for column, value in rowproxy.items()} for rowproxy in books]
    except Exception as e:
        result = []
    return result

def create_book(**data):
    try:
        sess = Session()
        book = Book(name=data['name'], author=data['author'], description=data['description'])
        sess.add(book)
        sess.commit()
        result = True
    except Exception:
        result = False
    return result


def get_books():
    try:
        result = []
        sess = Session()
        book = sess.query(Book).order_by(Book.name).all()
        result = [a.to_dict() for a in book]
    except Exception as e:
        result = []
    return result



def update_book(book_id, **data):
    try:
        sess = Session()
        book = sess.query(Book).get(book_id)
        if not book:
            result = False
        else:
            book.name = data['name']
            book.author = data['author']
            book.description = data['description']
            sess.commit()
            result = True
    except Exception as err:
        result = False
    return result


def delete_book(book_id):
    try:
        result = False
        sess = Session()
        book = sess.query(Book).get(book_id)
        if book:
            sess.delete(book)
            sess.commit()
            result = True
    except Exception:
        result = False
    return result

