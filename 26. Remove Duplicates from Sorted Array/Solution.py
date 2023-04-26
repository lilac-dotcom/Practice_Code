class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A boolean to determine whether constraints have been met or not. If it is False we cannot move ahead.
        go_ahead = True

        # Condition to check the first given constraint
        if 1 <= len(nums) <= (3 * (pow(10, 4))):
            # Looping over the index and value of the items in the given list 
            for i, val in enumerate(nums):
                # Checking if the second constraint is met
                if -100 <= val <= 100:
                    # If current element is the last in the list, no need to compare with next for checking third constraint
                    if i == (len(nums) - 1):
                        go_ahead = True
                    else:
                        # If there is an element after the current one in the list, we compare to see if the next element's
                        # value is larger or equal to the current element (non-decreasing)
                        if val <= nums[i+1]:
                            go_ahead = True
                        else:
                            print("Please follow given constraints.")
                            go_ahead = False
                else:
                    print("Please follow given constraints.")
                    go_ahead = False
                    break
        else:
            print("Please follow given constraints.")
            go_ahead = False

        # If all constraints are met (go_ahead is True) we proceed
        if go_ahead:
            # If there is only one element in nums we return k=1 and leave nums as it is
            if len(nums) == 1:
                return 1
            else:
                # We loop over nums in reverse order to counter any index changes during the loop after removing a duplicate.
                # The order of execution changes to reverse order however actual indexes stay the same
                for i, val in reversed(list(enumerate(nums))):
                    # If there are more than 1 items in nums and the loop is currently at the first element, we continue the loop
                    if i == 0:
                        continue
                    else:
                        # If the loop is not at the first element and the current element is equal to the one before it, 
                        # we remove it 
                        if val == nums[i-1]:
                            nums.pop(i)
                        # If the loop is not at the first element and the current element is not equal to the one before it, 
                        # we continue the loop
                        else:
                            continue
                # After looping through nums and removing duplicates, we return the length of nums (k)
                return len(nums)