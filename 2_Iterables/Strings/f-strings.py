# Code im String ausführen - function String

user_table = {1: 'Hans Meier', 2: "Max Mustermann"}

def get_user_name(user_id):
    if user_id in user_table:
        return user_table[user_id]

user_id = 2
string = f"Hello my name is {get_user_name(user_id)}"
print(string)

list1 = [1, 2, 3]
print(f"text...{list1[1]}...text")
