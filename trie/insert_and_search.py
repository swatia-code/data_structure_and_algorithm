'''
PROBLEM STATEMENT
-----------------
Implement insert and search functionality of trie.
'''

'''
class TrieNode: 
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
'''
def _get_node():
    return TrieNode()
    
def _get_index(char):
    return ord(char) - ord('a')

def insert(root,key):
    '''
    root: root of trie tree
    key:  key to be inserted
    '''
    #code here
    head = root
    
    for ele in key:
        index = _get_index(ele)
        if not head.children[index]:
            head.children[index] = _get_node()
        head = head.children[index]
    head.isEndOfWord = True

def search(root, key):
    '''
    root:       root of trie tree
    key:        key to be searched
    Returns:    true if key presents in trie, else false
    '''
    #code here
    head = root
    for ele in key:
        index = _get_index(ele)
        if not head.children[index]:
            return False
        head = head.children[index]
        
    return head != None and head.isEndOfWord
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        if search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends
