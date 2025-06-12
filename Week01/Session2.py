# Problem 1
def transpose(matrix):
    m = len(matrix)       
    n = len(matrix[0])     

    trpMatrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            trpMatrix[j][i] = matrix[i][j]

    return trpMatrix

# Problem 2
def reverse_list(lst):
    L =0
    R = len(lst)-1
    
    while L < R:
        lst[L] ,lst[R] = lst[R],lst[L]
        L +=1
        R-=1
    return lst
        
# Problem 3

def remove_dupes(items):

    L =0
    
    while L < len(items)-1 :
        if items[L] == items[L+1]:
            items.pop(L)
        else:
            L+=1
    return items


#Problem 4

def sort_by_parity(nums):

    even = []
    odd = []
    for num in nums:
        if num %2 ==0:
            even.append(num)
        else:
            odd.append(num)
       
    return even + odd

#Problem 5
def most_honey(height):
        L =0
        R = len(height)-1
        max_area =0
        while L < R:
            width = R - L
            min_height = min(height[L], height[R])
            area = width * min_height
            max_area = max(max_area, area)

            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return max_area

        
# Problem 6

def merge_intervals(intervals):
        pass

# ---------------------------------------------------------#

#Problem Set Version 2

# Problem 1

def add_matrices(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix1[0])
    resMatrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(matrix1)):
        for j in range (len(matrix1)):
            resMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return resMatrix

#Problem 2 
def is_palindrome(s):
    L =0
    R = len(s)-1
    while L in range(len(s)-1):
        if s[L] == s[R]:
            L+=1 
            R-=1
            return True
        else:
            return False
    
# Problem 3 

#Problem 4
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
# Problem 5 
def three_sum(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j and i !=k and nums[i] + nums[j] + nums[k] == 0:
                    return [i,j,k]
    return

# ------------------- Test Cases -------------------
# Advanced Problem Set Version  Test Cases 1


#Problem 1 Test Case
if __name__ == "__main__":


    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)
print(transpose(matrix))

#Problem 2 Test Case

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

#Problem 3 Test Case


#Problem 4 Test Case
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

#Problem 5 Test Case
nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))

#Problem 5 Test Case

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))


# Problem 6 Test Case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

#-------------------------------------------------#
#Advanced Problem Set Version 2

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(add_matrices(matrix1, matrix2))


s = "madam"
print(is_palindrome(s))

s = "madamweb"
print(is_palindrome(s))

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

nums = [0, 1, 1]
print(three_sum(nums))