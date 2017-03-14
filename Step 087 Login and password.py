login = 100500
password = 424242


def auth(user_login, user_password):
    if user_login == login:
        return 'Login success' if user_password == password else 'Wrong password'
    return 'No user with login %d found' % l


l, p = map(int, input().split())
print(auth(l, p))
