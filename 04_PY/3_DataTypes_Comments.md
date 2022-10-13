# Subject
Data types and comments.

## Key terminology
Boolean:  
- A binary state that is True or False.  

string:  
- an array of characters
- using double or single quotes.  

int:  
- a whole number.
- can be postive or negative.  

float:  
- is a decimal number.  

comments:  
- are lines that do not get processed as code. To comment you use # at the start of the line. 

## Exercise  
Exercise 1  
- Create a new script.  

- Copy the code below into your script.
a = 'int'  
b = 7  
c = False  
d = "18.5"  

- Determine the data types of all four variables (a, b, c, d) using a built in function.  

- Make a new variable x and give it the value b + d. Print the value of x. This will raise an error. Fix it so that print(x) prints a float.  

- Write a comment above every line of code that tells the reader what is going on in your script.  
  
Exercise 2:  
- Create a new script.  

- Use the input() function to get input from the user. Store that input in a variable.  

- Find out what data type the output of input() is. See if it is different for different kinds of input (numbers, words, etc.).


### Sources
https://appdividend.com/2022/03/19/how-to-check-data-type-in-python/#:~:text=To%20check%20the%20data%20type,Python%20returns%20the%20data%20type.  

https://www.freecodecamp.org/news/python-print-type-of-variable-how-to-get-var-type/  

https://www.w3schools.com/python/python_user_input.asp

### Overcome challenges
The type() function is a valuable built-in function of Python with which you can get the data type of a variable.  

The input() function gives a string as output.

### Results  
![result exercise 1](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/f79a3ba46276d71c7f5361bcdd2d4bd21febe15c/00_includes/PY/result_datatype1.png)  
Result exercise 1.  
  
![result exercise 2](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/8d461884c4e2f1409706dff408155286c57413e8/00_includes/PY/result_datatype2.png)  
The output of input() function is always a string.