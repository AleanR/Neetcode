#Thought Process: A hashmap can be used here to be able to see if the same amount of the letters are in both arrays. Can also sort the arrays and check from least to greatest of the ASCII value if they have the same characters throughout the array and then one iteration to check if they are the same, if same return false, else return true.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

