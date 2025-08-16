'''
 Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''
#sol:-
numbers = list(range(1,11))

first_five = numbers[:5]

reversed_list = first_five[::-1]

print("Original List:",numbers)
print("Extracted first Five element :", first_five)
print("Reversed extracted element:", reversed_list)