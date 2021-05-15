from schema import Schema, Use, Optional


LOGIN_SCHEMA = Schema({
    'name': Use(str),
    'passwd': Use(str)
})

USER_SCHEMA = Schema({
    'name': Use(str),
    'passwd': Use(str),
    Optional('role'): Use(str),
    Optional('active'): bool
})

UPDATE_SCHEMA = Schema({
    'role': Use(str),
})

BOOK_SCHEMA = Schema({
    'name': Use(str),
    'author': Use(str),
    Optional('description'): Use(str)
})