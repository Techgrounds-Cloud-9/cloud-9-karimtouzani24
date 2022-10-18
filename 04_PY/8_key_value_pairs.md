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

https://www.pythonforbeginners.com/basics/append-dictionary-to-csv-file-in-python


### Overcome challenges
Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

The part of appending to csv file took me a bit to accomplish. After searching the internet, I found the solultion.

### Results
![loop dictionary and print key value pair](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/ab0bf18f784ccfa64207902a7c4a21e0f50cd47a/00_includes/PY/result_KeyPair1.png)  
Loop dictionary and print key value pair.  

![the code to append from input dictionary to csv file](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/111dd363f4c7fc5fac8a3ea9a1e53026d8b204ec/00_includes/PY/result_keyvalue2a.png)  
The code used to append user input in a dictionary to csv file.  

![the result, the input is added to the csv file.](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/111dd363f4c7fc5fac8a3ea9a1e53026d8b204ec/00_includes/PY/result_keyvalue2b.png)  
The result, the input is added to the csv file. 
