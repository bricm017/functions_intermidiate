# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print(z)
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30

#2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for x in range(len(some_list)):
            print(f"first_name - {students[x]['first_name']}, last_name - {students[x]['last_name']}")
iterateDictionary(students)

#3.Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(str,some_list):
    for x in some_list:
        for k,v in x.items():
            print(k,v)

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

#4.Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k in some_dict:
        print(len(some_dict[k]), k)
        for v in some_dict[k]:
            print(v)
printInfo(dojo)

