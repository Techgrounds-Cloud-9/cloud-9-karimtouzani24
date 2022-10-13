# Subject
Loops

## Key terminology
Loops:  
- can be used when you want to run a block of code multiple times.  

2 types of loops:  
- while loop  
- for loop  

while loop:  
- runs while a condition is true.
- if the condition never changes, it will be an infinite loop. Press crtl-c or cmd + c to force quit.  

for loop:  
- runs for a predetermined number of iterations.  
- the number can be hard coded using range() function or dynamically assigned, using a variable, the size of a list  
or the number of lines in a document.  
- you can also create an infinite for loop, also press ctrl-c or cmd + c to force quit.  

The range() function:  
returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

## Exercise  
Exercise 1:  

- Create a new script.  

- Create a variable x and give it the value 0.  

- Use a while loop to print the value of x in every iteration of the loop. After printing, the value of x should increase by 1. The loop should run as long as x is smaller than or equal to 10.  

Exercise 2:  

- Create a new script.  

- Copy the code below into your script.  

 for i in range(10):
    # do something here  

- Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined.  

- Add a variable x with value 5 at the top of your script.  

- Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.


### Sources
https://www.w3schools.com/python/python_while_loops.asp  

https://www.w3schools.com/python/python_for_loops.asp

### Overcome challenges
If range(10) is used, the range starts from 0 to 9.

### Results  
![result exercise 1](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/ed64b9020d5c02179704f8324b6c8d24a504bacf/00_includes/PY/result_loops1.png)  
The while loop.  

![range 10 means from 0 to 9](https://github.com/Techgrounds-Cloud-9/cloud-9-karimtouzani24/blob/bb3a9eba8c9afe59958e35c16cb16b79e712e7f6/00_includes/PY/result_loops2a.png)  
The range starts at 0 to 9.
