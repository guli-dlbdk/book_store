from app.models import User, Session
from hashlib import sha512


def create_user(**data):
    try:
        # password = sha512(data['passwd'].encode('utf-8')).hexdigest()
        password=data['passwd']
        sess = Session()
        user = User(name=data['name'], password=password,
                    active=True,role=data['role'])
        sess.add(user)
        sess.commit()
        user_id = user.id
        result = True
    except Exception:
        user_id = None
        result = False
    return result, user_id


def get_users():
    try:
        result = []
        sess = Session()
        user = sess.query(User).order_by(User.name).all()
        result = [a.to_dict() for a in user]
    except Exception as e:
        result = []
    return result

    

def get_user(user_id):
    try:
        sess = Session()
        user = sess.query(User).get(user_id)
        if not user:
            result = []
        else:
            result = [user.to_dict()]
    except Exception as e:
        result = []
    return result


def update_user(user_id, **data):
    try:
        sess = Session()
        print('****', data['role'])
        # password = sha512(data['password'].encode('utf-8')).hexdigest()
        user = sess.query(User).get(user_id)
        if not user:
            result = False
        else:
            user.role = data['role']
            # user.passwd = password
            # user.active = data['active']
            sess.commit()
            result = True
    except Exception as err:
        result = False
    return result


def delete_user(user_id):
    try:
        result = False
        sess = Session()
        user = sess.query(User).get(user_id)
        if user:
            sess.delete(user)
            sess.commit()
            result = True
    except Exception:
        result = False
    return result


def authentication(data):
    try:
        sess = Session()
        # password = sha512(data['passwd'].encode('utf-8')).hexdigest()
        password = data['passwd']
        user = sess.query(User).filter(
            User.name == data['name'],
            User.password == password).first()
        if not user:
            result = {'status': False,
                      'data': []}
        else:
            result = {'status': True,
                      'data': [user.to_dict()]}

    except Exception as e:
        result = {'status': False,
                  'message': str(e)}

    return result