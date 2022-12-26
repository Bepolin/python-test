class User:

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return 'User:' + self.name

    def say_hello(self):
        return 'My name is ' + self.name

user = User('maro', 5)
print(user)
print(str(user))
print(user.say_hello())

