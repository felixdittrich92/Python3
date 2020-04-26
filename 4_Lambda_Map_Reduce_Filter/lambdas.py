# Lambda Expression: lokales Funktionsobjekt

#           KEYWORD Params (tuple): expression (without return keyword)
lambda_addition = lambda x, y: x + y

print(lambda_addition(1, 2))

my_dict = {'max': [26, 84], 'peter': [30, 90], 'hans': [22, 70]}
# sortiert nach den Elementen an Stelle 1
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

my_list = [[1, 20], [1, 3], [4, 10]]
# sortiert nach den Elementen an Stelle 1
my_list.sort(key=lambda x: x[1])
print(my_list)

# lambda division
lambda_division = lambda x, y: x / y if y != 0 else 0
print(lambda_division(10, 20))