class Data_Base:
    def __init__(self):
        self.data = {}

    def add_user(self, user_name, password):
        self.data[user_name] = password

class User:

    def __init__(self, user_name, password, password_confirm):
        self.user_name = user_name
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
     database = Data_Base()
     user = User(input('Введите имя: '), input('Введите пароль: '), input('Подтверждения пароля: '))
