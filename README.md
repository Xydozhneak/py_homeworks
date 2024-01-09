hw: Tasks 
1)Write a program that asks the user to enter a 4-digit number from the keyboard, and then prints the column of digits that makes up the number. For example, the user enters 1234, and the program prints:

1

2

3

4

The problem must be solved using division methods (hint // and % or divmod). The output in a column can be done using 4 print functions.

The user can enter any 4-digit integer. Any 4-digit number is a number consisting of 4 digits, where each digit can be from 0 to 9 inclusive.

Your solution should take this into account! If the user has entered a non-integer number, it's the user's problem, not your app's.

Create solutions based on the assumption that the number is ALWAYS 4 digits.

2)

When prompted by the program, the user enters a 5-digit positive integer. You need to "flip" this number backwards, i.e., to make it a 5-digit number, but with the sequence of digits reversed.

You don't need to check that the user has entered the correct number - just pretend that the user always enters a 5-digit number. That is, the number entered by the user will always consist of 5 digits.

If the user enters a different number, it is the user's problem, not your program's.

Only integers are used.

To solve the problem, you need to use only the data segment that has been passed. That is, you cannot use strings.

Example:

User enters: 12345 - the screen displays: 54321

User entered: 37568 - the screen displays: 86573

3)

The program should perform simple mathematical operations (+, -, *, /). The user is asked to enter numbers and an action on these numbers one by one, and the program calculates and prints the result based on the action.

Check that the divisor is not equal to 0 when dividing!

Example:

Please enter first number: 3

Please enter second number: 5

Please enter action: +

Your result is 8

An example with division by zero:

Please enter first number: 10

Please enter second number: 0

Please enter action: /

You can't divide by 0

4) 
Your program should be able to split one list into two and place them in a new list. That is, the result should be a list of 2 lists.

If the original list has an odd number of items, then the first list must have more items.

If there are no items in the list, then a list with two empty lists should be created.

Important! You need to create a solution that handles 3 cases - the list is empty, the list has an even number of items, and the list has an odd number of items.

Examples:

Was => became.

[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
[1, 2, 3] => [[1, 2], [3]]
[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
[1] => [[1], []]
[] => [[], []]

5) 
Your program must move the last item in the list from the end to the beginning, that is, the last item in the list must become the first. The sequence of other items should not change.

An empty list or a list with one item must remain unchanged.

The number of items in the list can be any number - zero or more!

Examples.

[12, 3, 4, 10] => [10, 12, 3, 4]
[1] => [1]
[] => []
[12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

6)
Write a program that moves all zeros to the end of the list.

Your task is to change the list so that all zeros are at the end of the list.

The order of the non-zero numbers must be preserved!

Example:

[0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
[0] -> [0]
[1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

To check the correctness of your code, use the examples above. You do not need to request data input from the user.

7)

For a list of integers, find the sum of the elements with even indexes [0, 2, 4, etc.], then multiply this sum by the last element of the input array.

Remember that the first element of the array has index 0.

For an empty array, the result is always 0.

Example:

[0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

[1, 3, 5] => 30
[6] => 36
[] => 0

To check the correctness of your code, use the examples above. You do not need to request data input from the user.
