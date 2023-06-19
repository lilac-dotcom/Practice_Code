class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # A key takeaway for me while solving this problem 
        # was that we must use the whole notation (such as digits[i] or digits[len(digits) - 1])
        # when changing the value of an element in the python list/array
        
        # A boolean to satisfy contraints
        go_ahead = True

        # If the length of digits is not between 1 and 100 inclusive, we do not proceed
        if not 1 <= len(digits) <= 100:
            go_ahead = False

        for i, val in enumerate(digits):
            # If any digit in array is not between 0 and 9, we do not proceed
            if not 0 <= val <= 9:
                go_ahead = False
            
            # If the first positioned digit is a 0 with more digits to its right, we do not proceed
            elif i == 0 and val == 0:
                if i + 1 < len(digits):
                    go_ahead = False
                
                #Otherwise, it means 0 is the only element. So we increment by 1
                else:
                    digits[i] = 1
                    return digits
        
        # Proceeding if constraints are met
        if go_ahead:
            # If the last digit is between 0 and 8, we increment by 1
            if 0 <= digits[len(digits) - 1] <= 8:
                digits[len(digits) - 1] = digits[len(digits) - 1] + 1
                return digits

            # If the last digit is 9, we set the last digit to 0 and increment the digit on its left by 1
            else:
                # If the array is empty, we give an error
                if len(digits) == 0:
                    print("please enter a valid digit array")

                else:
                    # Otherwise, we set the current digit to 0 and move on backwards if the digit to its left is also 0. 
                    # If the one on the left is not 9, we still set current to 0 but we also increment the left digit by 1
                    for i, val in reversed(list(enumerate(digits))):
                        if val == 9 and i == 0:
                            digits[i] = 0
                            digits.insert(0, 1)
                            
                        elif val == 9 and digits[i-1] == 9:
                            digits[i] = 0
                            
                        elif val == 9 and 0 <= digits[i-1] <= 8:
                            digits[i] = 0
                            digits[i-1] = digits[i-1] + 1
                            break
                            
                return digits

