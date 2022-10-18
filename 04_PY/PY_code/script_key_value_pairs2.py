import csv
myfile = open('exercise_8.csv', 'r+')
print(myfile.read())

employee_info = ["First name", "Last name", "Job title", "Company"]
my_dictionary = {
    "First name": "",
    "Last name": "",
    "Job title": "",
    "Company": "",
}

my_dictionary["First name"] = input("Please enter your First name: ")
my_dictionary["Last name"] = input("Please enter your Last name: ")
my_dictionary["Job title"] = input("Please enter your Job title: ")
my_dictionary["Company"] = input("Please enter the Company name: ")

print(my_dictionary)

writer = csv.writer(myfile)
writer.writerow(my_dictionary.values())
myfile.close()
myfile = open('exercise_8.csv', 'r')
print(myfile.read())