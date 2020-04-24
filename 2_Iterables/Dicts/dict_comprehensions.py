# key: value
dict1 = {x: x**2 for x in range(10)}
print(dict1)

# nur gerade
dict2 = {x: x**2 for x in range(10) if x % 2 == 0}
print(dict2)

# wenn > 5 quadrieren ansonsten hoch 1/2
dict3 = {x: x**2 if x > 5 else x**(1/2) for x in range(10) if x % 2 == 0}
print(dict3)

friends = ['hans', 'peter', 'max']
friend_keys = ['firstname', 'lastname', 'birthday']

"""
my_friend_dict = {
                'hans': {'firstname': None, 'lastname': None, 'birthday': None}, 
                'peter': {'firstname': None, 'lastname': None, 'birthday': None}, 
                'max': {'firstname': None, 'lastname': None, 'birthday': None}
                }
print(my_friend_dict)
"""

# als Dict Comprehension
my_friend_dict2 = {friend_name: {key: None for key in friend_keys} for friend_name in friends}
print(my_friend_dict2)