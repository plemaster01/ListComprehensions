names = ['pete lemaster', 'dale topley', 'phillip nunez']

# new_list = [ a for b in c if d]

'''names_proper = []
for i in range(len(names)):
    if names[i].startswith('p'):
        name_proper = names[i].title()
        names_proper.append(name_proper)'''

names_proper = [name.title() for name in names if name.startswith('p')]

print(names_proper)

matrix = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h'], ['i', 'j'], ['k','l','m']]
# first for loop is 'main' operation and any for loops after that will run inside of each iteration of the loop
abcs = [char.upper() for list in matrix for char in list]
print(abcs)

numbers = [x for x in range(100)]
squares = [(num, num**3) for num in numbers if num**3 % 6 == 0]
print(squares)

salaries = {'pete lemaster': 50000,
            'dale topley': 180000,
            'phillip nunez': 120000}

adjusted_salaries = {name.upper(): int(salary/1000) for name, salary in salaries.items() if (int(salary/1000) > 100 and name.startswith('p'))}
print(adjusted_salaries)