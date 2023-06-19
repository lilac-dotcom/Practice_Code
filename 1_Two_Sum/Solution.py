class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_list = [] # A list to return as output containing indices of the two numbers such that they add up to target. Initially empty
        go_ahead = True # Boolean to check if constraints are met. If True, we can proceed 
        a = pow(-10, 9)
        b = pow(10, 9)
        c = pow(10, 4)

        # Checking if input is of correct type
        if type(nums) == list and type(target) == int:
            # Checking if every element in nums has a value within given constraints. If not, we set the boolean to False.
            for value in nums:
                if  not (a <= value <= b):
                    go_ahead = False
                    print("Please follow the given constraints in the description.")
            
            # Checking if the length of nums is within the given constraint, and if target is within the constraints
            if ((2 <= len(nums) <= c) and (a <= target <= b)):
                # If boolean is True, we proceed
                if go_ahead:
                    for i, x in enumerate(nums):
                        if len(my_list) == 0:
                            for j, y in enumerate(nums):
                                if i == j:
                                    # We cannot use the same element twice so we skip the iteration
                                    continue
                                # If the values add up to the target we append the indexes to my_list
                                elif x + y == target:
                                    my_list.append(i)
                                    my_list.append(j)
                                    break
                                # In other cases where values are different and do not add to target, we move on
                                else:
                                    continue
                        else:
                            # Return the resulting list as output 
                            return my_list
                else:
                    print("Please follow the given constraints in the description.")  
        else:
            print("Please follow the correct input data types given in the description.")  