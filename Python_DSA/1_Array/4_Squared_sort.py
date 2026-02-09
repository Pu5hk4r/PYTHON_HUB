#TIMECOMPLEXITY 0(nlogn) , space O(n)
def square_array(array):
    new_array  = [0] * len(array)

    for i in range(len(array)):

        new_array[i] = array[i]**2

    new_array.sort()

    return new_array

print(square_array([]))
print(square_array([-5,-3,-1]))
print(square_array([2,3,5]))
print(square_array([-9,-1,0,4,10]))
print(square_array([-2,-2,0,4,4]))