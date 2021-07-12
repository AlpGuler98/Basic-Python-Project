# The example input specified in the project description is used.
# You can enter a different input by manipulating the line below:
input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

# An empty list to create the 'flattened list':
L = []

# A recursive function to flatten the list:
def flatten(x):
    for i in x:

        # If element i is not a list, we can directly append it to L.
        if type(i) != list:
            L.append(i)

        # If element i is also a list, we should call the recursive function:
        else:
            flatten(i)
    return L


print(flatten(input))
