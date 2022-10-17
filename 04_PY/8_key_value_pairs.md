# Subject
Key-value pairs

## Key terminology
dictionaries:  
- Dictionaries are used to store data values in key:value pairs.  

- A dictionary is a collection which is ordered, changeable and do not allow duplicates.  

- Dictionaries are written with curly brackets, and have keys and values

## Exercise
Exercise 1:  

- Create a new script.  

- Create a dictionary with the following keys and values:  

Key - Value  
First name - Casper  
Last name - Velzen  
Job title - Lead Learning Coach  
Company - TechGrounds  

- Loop over the dictionary and print every key-value pair in the terminal.  

Exercise 2:  

- Create a new script.  

- Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary.  

- Write the information to a csv file (comma-separated values). The data should not be overwritten when you run the script multiple times.


### Sources
https://www.w3schools.com/python/python_dictionaries.asp  

https://www.w3schools.com/python/python_dictionaries_loop.asp  


### Overcome challenges
Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

### Results
![loop dictionary and print key value pair](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/ab0bf18f784ccfa64207902a7c4a21e0f50cd47a/00_includes/PY/result_KeyPair1.png)  
Loop dictionary and print key value pair.  

