"""PROBLEM STATEMENT
-----------------
Given a string consisting of spaces,\t,\n and lower case  alphabets.Your task is to count the number of words where spaces,\t and \n work as separators.

Input:
The first line of input contains an integer T denoting the number of test cases.Each test case consist of a string.

Output:
Print the number of words present in the string.

Constraints:
1<=T<=100

Example:
Input:
2
abc\t\ndef   ghi
one   two   three  \t  four
Output:
3
4

LOGIC
-----
Iterate through the string and check if the chahracter is " " or '\'. If '\'is there check the next character and increment number of word count accordingly.

CODE
----"""

test_cases = int(input())
for i in range(test_cases):
    input_string = input()
    count_words = 0
    counter = 0
    j = 0
    while(j<len(input_string)):
        if(input_string[j]>='a' and input_string[j]<='z'):
            counter = counter+1
            j = j+1
        elif(ord(input_string[j])==92):
            if(j==len(input_string)):
                counter = counter+1
            elif(j+1<len(input_string) and input_string[j+1]=='n' or input_string[j+1]=='t'):
                if(counter>0):
                    count_words = count_words+1
                    counter = 0
                j = j+2
            else:
                counter = counter+1
                j = j+1
        else:
            if(counter>0):
                count_words = count_words+1
                counter = 0
                j = j+1
            else:
                j = j+1
    if(counter>0):
        count_words = count_words+1
    print(count_words)
