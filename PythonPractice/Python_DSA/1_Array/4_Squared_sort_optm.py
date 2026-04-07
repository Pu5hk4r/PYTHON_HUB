def square_array(array):
    newArray = [0] * len(array)
    leftpointer = 0
    rightpointer = len(array) - 1                     #TC = O(n)
                                                      #SC = O(n)

    for i in reversed(range(len(array))):
        leftsquared = array[leftpointer] ** 2
        rightsquared = array[rightpointer] ** 2

        if leftsquared > rightsquared:
            newArray[i] = leftsquared
            leftpointer += 1
        else:
            newArray[i] = rightsquared
            rightpointer -= 1

    return newArray

# Test cases
print(square_array([]))                  # []
print(square_array([-5, -3, -1]))        # [1, 9, 25]
print(square_array([2, 3, 5]))           # [4, 9, 25]
print(square_array([-9, -1, 0, 4, 10]))  # [0, 1, 16, 81, 100]
print(square_array([-2, -2, 0, 4, 4]))   # [0, 4, 4, 16, 16]



# def square_array(array):
#     newArray = [0] * len(array)
#     leftpointer = 0
#     rightpointer = len(array) - 1
#     index = len(array) - 1
#
#     while leftpointer <= rightpointer:
#         leftsquared = array[leftpointer] ** 2
#         rightsquared = array[rightpointer] ** 2
#
#         if leftsquared > rightsquared:
#             newArray[index] = leftsquared
#             leftpointer += 1
#         else:
#             newArray[index] = rightsquared
#             rightpointer -= 1
#         index -= 1
#
#     return newArray
#
# # Test cases
# print(square_array([]))                  # []
# print(square_array([-5, -3, -1]))        # [1, 9, 25]
# print(square_array([2, 3, 5]))           # [4, 9, 25]
# print(square_array([-9, -1, 0, 4, 10]))  # [0, 1, 16, 81, 100]
# print(square_array([-2, -2, 0, 4, 4]))   # [0, 4, 4, 16, 16]
#
#
# #timecomplexity O((n))