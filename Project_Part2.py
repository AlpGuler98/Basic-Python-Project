# The example input specified in the project description is used.
# You can enter a different input by manipulating the line below:
input = [[1, 2], [3, 4], [5, 6, 7]]


# A recursive function to reverse the list:
def reverseList(x):
    x.reverse()

    for i in x:
        # If element i is also a list, we should call the recursive function to reverse it:
        if type(i) == list:
            reverseList(i)
    return x


print(reverseList(input))


