# C-style approach:This approach requires prior knowledge of total number of iterations.
# A C-style way of accessing list elements
# cars = ["Aston", "Audi", "McLaren"]
# i = 0
# while i < len(cars):
#     print(cars[i])
#     i += 1

"""
Important Points:

This style of looping is rarely used by python programmers.
This 4-step approach creates no compactness with single-view looping construct.
This is also prone to errors in large-scale programs or designs.
There is no C-Style for loop in Python, i.e., a loop like for (int i=0; i<n; i++)
"""

# --------------------------------------------
# Use of for-in (or for each) style:
# cars = ["Aston", "Audi", "McLaren"]
# for x in cars:
#     print(x)

# Indexing using Range function:
# Accessing items using indexes and for-in

# cars = ["Aston", "Audi", "McLaren"]
# for i in range(len(cars)):
#     print(cars[i])

# --------------------------------------------

"""
Enumerate:
Enumerate is built-in python function that takes input as iterator, 
list etc and returns a tuple containing index and data at that index in the iterator sequence. 
For example, enumerate(cars), 
returns a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on."""

# Accessing items using enumerate()
# cars = ["Aston", "Audi", "McLaren "]
# for i, x in enumerate(cars):
#     print(x)

# or

# Accessing items and indexes enumerate()
# cars = ["Aston", "Audi", "McLaren "]
# for x in enumerate(cars):
#     print(x[0], x[1])

# Enumerate takes parameter start which is default set to zero.
# We can change this parameter to any value we like. In the below code we have used start as 1.
cars = ["Aston", "Audi", "McLaren "]
for x in enumerate(cars, start=1):
    print(x[0], x[1])
