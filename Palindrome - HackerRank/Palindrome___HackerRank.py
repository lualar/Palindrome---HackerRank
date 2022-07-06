# The function accepts STRING s as parameter.
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the 'palindromeIndex' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def palindromeIndex(s):
    # Write your code here
    sTemp = [None] * len(s)
    if (len(s)==1):  #String with one char alrady a polindrome
        return -1

    s1 = s[::-1]
    
    if(s==s1): #Already a Polindrome
        return -1
    
    Palindrome = {}
    NoPalindrome = {}
    
    for i in range(len(s)):
        ikey = get_key(i, Palindrome)
        if (ikey> -1):
            return ikey
        
        ikey = get_key(i, NoPalindrome)
        if (ikey> -1):
            return -1
            
        #get new string without char on index i
        s1 = s[0:i] + s[i+1:len(s)]
        #print(s," ",s1)
        
        if not (len(sTemp) > 0 and s1 in sTemp):
            s2 = s1[::-1]  #reverse new string
            if (s1 == s2): #it is a polindrome
                Palindrome[s] = i
                return i
            else:
                NoPalindrome[s] = -1
                sTemp [i]=s1
    return -1

def get_key(val, Palindrome):
    for key, value in Palindrome.items():
        if val == value:
            return key
    return -1
    
if __name__ == '__main__':
    fptr = sys.stdout  #open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')
    fptr.close()
