
my_name = "ddHansi Vordorf"
print(my_name, type(my_name))

print("----------Groß/Klein/Split/Strip/ersetzen/etc.----------")

# erste Buchstabe groß Rest klein
print(my_name.capitalize())
# alles klein
print(my_name.lower())
# alles groß
print(my_name.upper())

# beim Leerzeichen splitten -> Liste
word_list = my_name.split(' ')
print(word_list)

# alle d am Anfang entfernen
my_name_modified = my_name.strip('d')
print(my_name_modified)

my_name = 'Peter Peterson'
# überprüfen erste Wort
print(my_name.startswith('Peter'))
# überprüfen letzte Wort
print(my_name.endswith('Peterson'))

if my_name.startswith('Peter'):
    # ersetzen
    my_name = my_name.replace('Peter', 'Magnus')

print(my_name)

print("----------Zusammenfügen----------")
friend_names = ['Jan', 'Peter', 'Dennis']

output_str = ' '.join(friend_names)
print(output_str)