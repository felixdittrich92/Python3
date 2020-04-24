from collections import namedtuple

User = namedtuple('User', ['firstname', 'lastname', 'birthday'])
user_peter = User(firstname='Peter',lastname='Heinrich', birthday='30.01.1980')
print(user_peter)

print(user_peter.firstname)
print(user_peter.lastname)
print(user_peter.birthday)