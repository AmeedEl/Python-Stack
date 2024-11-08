x = [ [5,2,3], [10,8,9] ]

x[1][0] = 15
print(x)
print("\n")

students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'}
]

for student in students:
    students[0]['last_name'] = "Bryant"
    print(student)
print("\n")

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'football' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['football'][0] = 'Andres'
print(sports_directory)
print("\n")

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)
print("\n")

# With BONUS
def iterateDictionary(info):
    for dictionary in info:
        result = []
        for key, value in dictionary.items():
#            print(f"{key} - {value}")
             result.append(f"{key}: {value}")
        print(" - ".join(result))

students = [
    {'firstname': 'Michael', 'lastname': 'Jordan'},
    {'firstname': 'John', 'lastname': 'Rosales'},
    {'firstname': 'Mark', 'lastname': 'Guillen'},
    {'firstname': 'KB', 'lastname': 'Tonel'}
]

iterateDictionary(students)
print("\n")


def iterateDictionary2(info, students):
    values = [dictionary.get(info) for dictionary in students]
    print(", ".join(values))

# def iterateDictionary2(info, students):
#     for dictionary in students:
#         print(dictionary.get(info))

students = [
    {'firstname': 'Michael', 'lastname': 'Jordan'},
    {'firstname': 'John', 'lastname': 'Rosales'},
    {'firstname': 'Mark', 'lastname': 'Guillen'},
    {'firstname': 'KB', 'lastname': 'Tonel'}
]

print("- ", end="")
iterateDictionary2('firstname', students)

print("- ", end="")
iterateDictionary2('lastname', students)
print("\n")


def printInfo(dictionary):
    for key, values in dictionary.items():
        print(f"{len(values)} {key.upper()}")

        for value in values:
            print(value)
        print()

dojo = {
    'locations': ['San jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)