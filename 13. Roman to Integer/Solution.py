class Solution(object):
    def __init__(self):
        pass
    
    def romanToInt(self, s):
        # Creating a dictionary of single letters and their values
        my_dict_single = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        # Creating a dictionary of double letters and their values
        my_dict_double = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        # A list of all roman numerals
        my_list = ["I", "V", "X", "L", "C", "D", "M"]

        # Initializing the counter
        count = 0

        # Checking if length of string is within given limit
        if not 1 <= len(s) <= 15:
            print("Please keep the input between 1 and 15 characters")

        # Checking if characters of string is within the list of roman numerals
        elif any(x not in my_list for x in s):
            print("Please make sure that s only contains characters that are roman numerals")

        # If all constraints are met, we continue
        else:
            for i, val in enumerate(s):
                # If the current character is the first character of the string
                if i == 0:
                    # If the current character is not the last character 
                    if not i == len(s)-1:
                        next_val = s[i+1]
                        double_string =  val + next_val

                        if double_string in list(my_dict_double.keys()):
                            count = count + my_dict_double[double_string]

                        elif val in list(my_dict_single.keys()):
                            count = count + my_dict_single[val]# Checking if length of string is within given limit
                    
                    # In this case the current character is the first, last and hence only character. So we just return its corresponding value
                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]

                # In the case of current character being the last character 
                elif i == len(s)-1:
                    previous_val = s[i-1]
                    # A combination of current character and its previous character
                    reverse_match = previous_val + val

                    # If this combination is within the keys of the double character roman numerals, we continue since it has already been counted
                    if reverse_match in list(my_dict_double.keys()):
                        continue

                    # If there is no reverse match and the current value is a single character roman value, we count it in result
                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]

                
                else:
                    next_val = s[i+1]
                    previous_val = s[i-1]
                    double_string =  val + next_val
                    reverse_match = previous_val + val

                    # If this combination is within the keys of the double character roman numerals, we continue since it has already been counted
                    if reverse_match in list(my_dict_double.keys()):
                        continue
                    
                    # If there is a match with double characters we count it
                    if double_string in list(my_dict_double.keys()):
                        count = count + my_dict_double[double_string]

                    # If the current character is a roman numeral with no previous match we count it
                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]
        
        return count