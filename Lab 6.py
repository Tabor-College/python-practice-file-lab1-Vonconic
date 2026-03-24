# PART 1: What is an Algorithm

# Steps to make a sandwich
# 1. Get two slices of bread
# 2. Put A piece of ham between them
# 3. Sandwich compelete

# I guess the steps are clear enough for a computer. Seems pretty straight foward to me.

# If a step is missing it won't be a sandwich

# Someone can probably follow these steps. Unless they are stupid.

# PART 2: Step Counting

numbers = [5, 3, 8, 2, 9]
target = 9

for num in numbers:
    if num == target:
        print("Found")

# This loop will run 5 times because 9 is the last number in the list
# If the target is the first element the loop will run once
# If the target is not present nothing will happen

# No I cannot explain the difference betwee best and worst case.

# PART 3: Nested Work

numbers_2 = [1, 2, 3, 4]

for i in numbers_2:
    for j in numbers_2:
        print(i, j)

# The print will run 9 times
# When the list grows the loop will run an exponential amount of time
# Because if there is 4 numbers the loop will run 4 times per number for a total of 16 times

# PART 4: Memory Usage 

# I would say the code in part 3 stores more data
# I'm not sure why storing data is important.
# No I don't know when extra memory is used

# PART 5: Thinking Before Coding

# The basic out line of what I want the code to do
# You think it out before you code so that you have a clear idea of what your are trying to accomplish
# Yes I can explain my logic in plain english

# PART 6: Two Ways to Solve a Problem

# I do not know what methods we are talking about
# I guess the nested loop uses more memory
# Because one is probably better than the other

# PART 7: Preduct the Output

numbers_3 = [2, 4, 6]

count = 0

for num in numbers_3:
    count += 1

print(count)

# The output will be 3
# This loop will run three times
# I didn't make a prediction but I guess yes

# PART 8: Find the Mistake

numbers_4 = [3, 2, 5, 4]

max_val = 0

for num in numbers_4:
    if num > max_val:
        max_val = num

print(f"The highest number is {max_val}")

# It doesn't account for negative numbers
# If all the numbers are negative it outputs 0
# You could fix this by maybe running a second check to see if the number is less than zero
# Im not sure it will work I just don't feel like trouble shooting it

# PART 9: Reduce the Work

# Not sure what these questions mean when they say which version

# PART 10: Build Your Own Algorithm

# What algorithm am I supposed to be making?
# I don't really know how to do this yet.

# PART 11: Real-Life Connection

# What is a catalog system?
# No idea how to answer these questions

# PART 12: Challenge

numbers_5 = [2, 8, 1, 10, 4]
count_2 = 0

# Count numbers greater than 5

for num in numbers_5:
    if num > 5:
        count_2 += 1
    
print(f"There are {count} numbers greater than five")

# PART 13: Reflection

# A Alogrithm is a set of code created to accomplish as specific task
# I do not know what "more work" means in a program
# I learned to process through the logic and understand the goal before coding


    

        



