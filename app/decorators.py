

from functools import wraps
from flask_login import current_user
from flask import abort



""" decorateur pour interdir l'acces a certaines routes, selon le role del utilisateur """

def role_required(roles):   
    def decorator(f):

        """ wraps pour consever les metadonnés de la function (nom, docstring, metadata ... ) """
        @wraps(f)
        def wrapper(*args, **kwargs):

            """ si  l'utilisateur il est pas connecté, return error http-401 """
            if not current_user.is_authenticated:
                abort(401)  # no log

            """ si le role n'est pas autorisé, return http-403 """
            if current_user.role not in roles:
                abort(403)  # no auth

            """ si tout est ok, on return la function (la route) """
            return f(*args, **kwargs)
        return wrapper
    
    return decorator
