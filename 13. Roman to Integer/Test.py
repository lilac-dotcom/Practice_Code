from Solution import Solution

my_solution = Solution()

print(my_solution.romanToInt("III"))
print(my_solution.romanToInt("LVIII"))
print(my_solution.romanToInt("MCMXCIV"))

user_num = input("Enter a roman numeral between 1 and 15 characters:")
print(f"The integer equivalent is {my_solution.romanToInt(user_num)}")