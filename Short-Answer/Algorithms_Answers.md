#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
The run time of a is O(n). Since the while loop is a loop the size
of n will dictate the number of operations proportional to the size of the input.

b)
The run time of B) is O(n log n). As n increases the run time increases slightly slower rate.

c)
The run time of c is O(n) in this case since the recursive call only is recurssing and taking 1 away from bunnies if it were used in fibonacci it would be O(2^n) but this is simply returning 2 minus the size of n in a fashion similar to a loop.

## Exercise II

In this case I'm going to assume that the question is asking me to write a function with an algorithm that helps a user throw as many eggs as possible with out breaking eggs. This function will take in n which is the number of stories in the building and \*args which will consist of a series of numbers. These series of numbers will determine what floor the egg will be thrown off of. Initially I would instantiate a broken_egg variable and assign it a value of zero the same with thrown_eggs. I will enter a for loop which will take n and set n as the range of the for loop. The i in this for loop will determine the level of the building that is being assigned a value (e.x - 0, 1, 2, 3, 4, etc) using the string ascii_lower module out side of the scope of this function i will import string and assign alphabets to string.ascii_lower which will hold all of the values in the alphabet. Back in the for loop I will assign a variable called story_floor and assign a dictionary as it's value. In the value, the key will be assigned to f'floor{i}' and the alphabet at the index of i in alphabets will be the value of the dictionar and that for loop will end giving us a dictionary of level compared to its floor letter.
we will loop through the args passed & Next we will set conditional statements to check if the value of the dictionary for the index arg passed in is higher than f by checking the value of story_floor[f'{floor{i}}'] ensuring that it's value is f or higher.If so we will print a statement making the user aware that if they throw eggs off level f or higher the eggs will break... we will increment broken and thrown eggs at this point and if the level thrown is less than f we will print a statement reading Since you threw an egg off of floor {arg} it did not break and we will increment thrown eggs. Lastly, we will return the count of thrown and broken eggs.

When written this code should represent a Space/Time complexity with a runtime of O(n). Since, there are 2 successive loops in this function call the run time before dropping constants is O(2n) we drop the 2 for a run time of O(n).
