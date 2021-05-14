from schema import Schema, Use, Optional


LOGIN_SCHEMA = Schema({
    'name': Use(str),
    'passwd': Use(str)
})

USER_SCHEMA = Schema({
    'name': Use(str),
    'passwd': Use(str),
    Optional('active'): bool
})