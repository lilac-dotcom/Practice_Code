class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        #setting the boolean go_ahead to true initially. go_ahead determines if the algorithm will proceed based
        # on given constraints
        go_ahead = True

        # checking constraints and setting boolean to false 
        if m < 0 or n > 200:
            go_ahead = False
            print("constraints not met")

        elif m + n < 1 or m + n > 200:
            go_ahead = False
            print("constraints not met")

        for el in nums1:
            if el < pow(-10, 9) or el > pow(10, 9):
                go_ahead = False
                print("constraints not met")

        for el in nums2:
            if el < pow(-10, 9) or el > pow(10, 9):
                go_ahead = False
                print("constraints not met")

        # only proceed with the algorithm if the boolean is true (constraints met)
        if go_ahead:
            # creating enumerate objects
            enum_nums1 = enumerate(nums1)
            enum_nums2 = enumerate(nums2)

            # handling numbers of the elements
            if n == 0 and m == 0:
                pass
            elif n == 0 and m != 0:
                pass
            elif m == 0 and n != 0:
                a = 0
                b = m
                while a < n:
                    nums1[b] = nums2[a]
                    a += 1
                    b += 1
            elif m != 0 and n != 0:
                a = 0
                b = m
                while a < n:
                    nums1[b] = nums2[a]
                    a += 1
                    b += 1
                nums1.sort()