import os
# abspath nutzen, da es für das Betriebssystem die entsprechenden Seperatoren verwendet

print("----------Pfad betriebssystemunabhängig angeben----------")

project_path = os.path.abspath(r'C:\Users\felix\Desktop\Python3')
file_path = os.path.join(project_path, r"other\data.txt")
print(file_path)

print("----------Open Files----------")

# with schließt File automatisch
with open(file_path, "r", encoding='utf8') as f:
    content = f.readlines()

print(f, type(f))

print(content)
for idx, line in enumerate(content):
    content[idx] = line.replace("\n", "")
print(content)

print("----------User Input----------")

user_input = input("Please enter your age: ")
print(user_input, type(user_input))
user_age = int(user_input)
print(user_age, type(user_age))