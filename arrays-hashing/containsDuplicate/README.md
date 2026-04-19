Problem: Given an integer array "nums", return true if any value appears more than once in the array, otherwise return false.

Ex 1:
    Input: nums = [1,2,3,3]
    Output: true

Ex 2:
    Input: nums =[1,2,3,4]
    Output: false

First look at it seems like a brute force method of iteratively going through the array with a nested for loop will give a correct solution.
There is a problem with the time complexity however as a nested for loop tends to have a O(n^2) time complexity. The brute force solution I have implemented to no suprise has a O(n^2) time complexity and a O(1) space complexity (Where n is the number of elements inside the nums array).

Now to move on to a more time efficient method. The idea is to first sort the array such that the array will be sorted and duplicates will be next to each other, allowing us to only iterate once.

