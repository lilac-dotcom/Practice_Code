class Solution(object):
    def __init__(self):
        pass
    
    def romanToInt(self, s):
        my_dict_single = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        my_dict_double = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        my_list = ["I", "V", "X", "L", "C", "D", "M"]

        count = 0

        if not 1 <= len(s) <= 15:
            print("Please keep the input between 1 and 15 characters")

        elif any(x not in my_list for x in s):
            print("Please make sure that s only contains characters that are roman numerals")

        else:
            for i, val in enumerate(s):
                if i == 0:
                    if not i == len(s)-1:
                        next_val = s[i+1]
                        double_string =  val + next_val

                        if double_string in list(my_dict_double.keys()):
                            count = count + my_dict_double[double_string]

                        elif val in list(my_dict_single.keys()):
                            count = count + my_dict_single[val]
                    
                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]


                elif i == len(s)-1:
                    previous_val = s[i-1]
                    reverse_match = previous_val + val

                    if reverse_match in list(my_dict_double.keys()):
                        continue

                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]

                
                else:
                    next_val = s[i+1]
                    previous_val = s[i-1]
                    double_string =  val + next_val
                    reverse_match = previous_val + val

                    if reverse_match in list(my_dict_double.keys()):
                        continue
                    
                    if double_string in list(my_dict_double.keys()):
                        count = count + my_dict_double[double_string]

                    elif val in list(my_dict_single.keys()):
                        count = count + my_dict_single[val]
        
        return count