from Solution import Solution

my_solution = Solution()

l1 = [1,2,3,0,0,0]
l2 = [2,5,6]
num_el1 = 3
num_el2 = 3

my_solution.merge(l1, num_el1, l2, num_el2)
print(l1)

# result should be [1,2,2,3,5,6]