#functions intermediate
"""
make functions that do stuff and things.
function 1: update values in dictionaries and lists
function 2: iterate through a list of dictionaries
function 3: get values from a list of dictionaries
function 4: iterate through a dictionary with list values
"""

x = [ [5,2,3], [10,8,9] ] 

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def updateValues():
    x[1][0] = 15
    # students[0].get("last_name") = 'Bryant' #doesn't work
    for s in students:
        for d in s:
            if s.get(d) == 'Jordan':
                s.update({d: "Bryant"})
    sports_directory.get("soccer")[0] = 'Andres'
    # z[0].get("y") = 30 #doesn't work
    for a in z:
        if a.get('y'):
            a.update({'y': 30})
    print(x)
    print(students)
    print(sports_directory)
    print(z)

def iterateDictionary(students):
    for item in students:
        print("first_name -",item.get("first_name")+",","last_name -", item.get("last_name"))

def iterateDictionary2(key_name,some_list):
    values_of_key = [a_dict[key_name] for a_dict in some_list]
    print(values_of_key)

def printInfo(some_dict):
    print(len(some_dict.get('locations')),"locations")
    for item in some_dict.get('locations'):
        print(item)
    print(len(some_dict.get('instructors')),"instructors")
    for item in some_dict.get('instructors'):
        print(item)

updateValues()
iterateDictionary(students)
iterateDictionary2('first_name',students)
printInfo(dojo)