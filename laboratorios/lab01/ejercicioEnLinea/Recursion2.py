# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:58:34 2021

@author: Andres and Juank
"""

#%%
def split53(array, aux= 0, mult3= 0, mult5= 0):
   if aux == len(array):                                         # c0
      return mult3 == mult5                                      # c1
   else:                                                         # c2
      if array[aux]%3 == 0:                                      # c4
         return split53(array, aux+1, mult3+array[aux], mult5)   #T(n) = c5 + T(n-1)
      elif array[aux]%5 == 0:                                    # c6
         return split53(array, aux+1, mult3, mult5+array[aux])   #T(n) = c7 + T(n-1)
      else:                                                      # c8
         return split53(array, aux+1, mult3+array[aux], mult5) or split53(array, aux+1, mult3, mult5+array[aux]) 
                                                                 #T(n) = c9 + T(n-1) + T(n-1)

print(split53([5, 5, 3, 3]))

#%%
def splitArray(array, aux= 0, a= 0, b= 0):
   if aux == len(array):                        # c0
      return a == b                             # c1
   else:                                        # c2
       return splitArray(array, aux+1, a+array[aux], b) or splitArray(array, aux+1, a, b+array[aux]) 
                                                #T(n) = c3 + T(n-1) + T(n-1)

print(splitArray([10, 3, 10, 3]))

#%%
def splitOdd10(array, aux= 0, mult10= 0, multnt2= 0):
   if aux == len(array):                                                # c0
      return mult10 == multnt2                                          # c1
   else:                                                                # c2
      if array[aux]%10 == 0:                                            # c3
         return splitOdd10(array, aux+1, mult10+array[aux], multnt2)    # T(n) = c4 + T(n-1)
      elif array[aux]%2 != 0:                                           # c5
         return splitOdd10(array, aux+1, mult10, multnt2+array[aux])    # T(n) = c6 + T(n-1)
      else:                                                             # c7
         return splitOdd10(array, aux+1, mult10+array[aux], multnt2) or splitOdd10(array, aux+1, mult10, multnt2+array[aux]) 
                                                                        # T(n) = c8 + T(n-1) + T(n-1)

print(splitOdd10([10, 3, 10, 3, 14]))

#%%
def GroupSum5(nums, target, start=0):
    if start >= len(nums):                                      # c0
        if target == 0:                                         # c1
            return True                                         # c2
        else:                                                   # c3
            return False                                        # c4

    if nums[start]%5 == 0:                                      # c5
        return GroupSum5(nums, target-nums[start], start + 1)   # T(n) = c6 + T(n-1)
    
    if nums[start-1]%5 == 0 and nums[start] == 1:               # c7
        return GroupSum5(nums, target, start + 1)               # T(n) = c8 + T(n-1)
    
      
    return GroupSum5(nums, target, start + 1) or GroupSum5(nums, target-nums[start], start + 1)
                                                                # T(n) = c9 + T(n-1) + T(n-1)

print(GroupSum5([10,7,1,1],12))

#%%
def GroupSum6(nums, target, start=0):
    if start >= len(nums):                                          # c0
        if target == 0:                                             # c1
            return True                                             # c2
        else:                                                       # c3
            return False                                            # c4

    if nums[start] == 6:                                            # c5
        return GroupSum6(nums, target-nums[start], start + 1)       # T(n) = c6 + T(n-1)
      
    return GroupSum6(nums, target, start + 1) or GroupSum6(nums, target-nums[start], start + 1)
                                                                    # T(n) = c7 + T(n-1) + T(n-1)
print(GroupSum6([10,7,6,6],12))
