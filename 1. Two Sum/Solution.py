class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_list = []
        go_ahead = True
        a = pow(-10, 9)
        b = pow(10, 9)
        c = pow(10, 4)

        if type(nums) == list and type(target) == int:
            for value in nums:
                if  not (a <= value <= b):
                    go_ahead = False
                    print("Please follow the given constraints in the description.")

            if ((2 <= len(nums) <= c) and (a <= target <= b)):
                if go_ahead:
                    for i, x in enumerate(nums):
                        if len(my_list) == 0:
                            for j, y in enumerate(nums):
                                if i == j:
                                    continue
                                elif x + y == target:
                                    my_list.append(i)
                                    my_list.append(j)
                                    break
                                else:
                                    continue
                        else:
                            return my_list
                else:
                    print("Please follow the given constraints in the description.")  
        else:
            print("Please follow the correct input data types given in the description.")  