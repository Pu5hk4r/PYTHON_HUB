import sys

class Pair:   #pair class designed for hold min and max value 2 values as single object

    def __init__(self,min_val = None , max_val = None):  # constructor

        self.min = min_val
        self.max = max_val

    def get_min_max(arr):

        minmax = Pair()
        arr.sort()  # sort array

        minmax.min  = arr[0]
        minmax.max = arr[-1]

        return minmax

    def set_mini(arr):

        mini = sys.maxsize  # C++ INT_MAX

        for val in arr:

            if val < mini :

                mini = val

        return mini

    def set_maxi(arr):

        maxi = -sys.maxsize - 1

        for val in arr:
             if val > maxi:
                 maxi = val
        return maxi

    if __name__ == "__main__":
        arr = [12, 78, 98, 100, 5, 1, 789]

        print("============ Method 1 O(n) ====================================")
        print("Minimum element using sys.maxsize:", set_mini(arr))
        print("Maximum element using -sys.maxsize - 1:", set_maxi(arr), "\n")

        print("============ Sorting-Pair Method O(nlogn) =====================")
        minmax = get_min_max(arr)
        print("Minimum element is", minmax.min)
        print("Maximum element is", minmax.max)




