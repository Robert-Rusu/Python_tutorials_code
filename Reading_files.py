#read
# open("employees.txt", "r")

#read and write
# open("employees.txt", "r+")

#write
# open("employees.txt", "w")

#append (at the end of the file)
# open("employees.txt", "a")

employee_file = open("employees.txt", "r")

# print(employee_file.readable()) -verificare
# print(employee_file.read()) - citeste tot fisierul

# print(employee_file.readline()) #citeste prima linie
# print(employee_file.readline()) #citeste a 2-a linie daca s-a citit prima deja

# print(employee_file.readlines()) # citeste toate liniile si le pune intr-un rand

# print(employee_file.readlines()[1]) #citeste randul 2
for employee in employee_file.readlines():
    print(employee)


employee_file.close()