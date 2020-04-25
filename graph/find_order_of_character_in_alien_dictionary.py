"""
PROBLEM STATEMENT
-----------------
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary the task is to complete the function which returns a string denoting the order of characters in the language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order.
Examples:
Input:  Dict[ ] = { "baa", "abcd", "abca", "cab", "cad" }, k = 4
Output: Function returns "bdac"
Here order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input: Dict[] = { "caa", "aaa", "aab" }, k = 3
Output: Function returns "cab"

 

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N and k denoting the size of the dictionary. Then in the next line are sorted space separated values of the alien dictionary.

Output:
For each test case in a new line output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Constraints:
1 <= T <= 1000
1 <= N <= 300
1 <= k <= 26
1 <= Length of words <= 50

Example:
Input:
2
5 4
baa abcd abca cab cad
3 3
caa aaa aab

Output:
1

LOGIC
-----
The idea is to create a graph of characters and then find topological sorting of the created graph.

1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language. For example, if the aplphabet size is 5, then there can be characters in words. Initially there are no edges in graph.

2) Do following for every pair of adjacent words in given sorted array.

    a) Let the current pair of words be word1 and word2.One bt one compare characters of bothw ords and find the first mismatching characters.
    b) Create an edge in g from mismatching character of word1 to that of word2.

3) Print topologicalsorting of the above created graph.

This code doesn't work when the input is not valid. For example {"aba","bba","aaa"} is not valid because first two forms word, we can deduce 'a' should appear before 'b', but from last two words, we can deduce 'b' should appear before 'a' which is not possible. This program can be extended to handle invalid inputs and generate the outputs as "Not valid".

TIME COMPLEXITY
---------------
The first step to create a graph takes O(n+alpha) time where n is the number of given words and alpha is tht number of characters given in alphabet. The second step is topological sorting. There would be alpha vertices and at most n-1 edges in graph. The time complexity of topological sorting is O(V+E) which is O(n+ aplha). So, overall time complexity is O(n + alpha) + O(n + alpha) which is O(n + alpha).

CODE
----
def printOrder(alien_dict, n, k):
    alphabet = ''
    if n == 1:
        for char in alien_dict[0]:
            if not char in alphabet:
                alphabet += char
        return alphabet

    adj_list = {}
    vertex_incoming_degree = {}

    for word in alien_dict:
        for char in word:
            if char not in vertex_incoming_degree:
                vertex_incoming_degree[char] = 0

    for i in range(0, n - 1):
        curr_word = alien_dict[i]
        next_word = alien_dict[i + 1]

        for index in range(0, min(len(curr_word), len(next_word))):
            char1 = curr_word[index]
            char2 = next_word[index]

            if char1 != char2:
                if char1 not in adj_list:
                    adj_list[char1] = set(char2)
                else:
                    adj_list[char1].add(char2)
                break

    for vertex in adj_list:
        for neighbour in adj_list[vertex]:
            if neighbour not in vertex_incoming_degree:
                vertex_incoming_degree[neighbour] = 1
            else:
                vertex_incoming_degree[neighbour] += 1

    visited_vertexes = []

    for v in vertex_incoming_degree:
        if vertex_incoming_degree[v] == 0:
            visited_vertexes.append(v)

    while visited_vertexes:
        curr = visited_vertexes.pop(0)
        alphabet += curr

        if curr in adj_list:
            for neighbour in adj_list[curr]:
                vertex_incoming_degree[neighbour] -= 1

                if vertex_incoming_degree[neighbour] == 0:
                    visited_vertexes.append(neighbour)

    return alphabet
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        
        order = printOrder(alien_dict,n,k)
        
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)
        
        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)


# } Driver Code Ends

"""
