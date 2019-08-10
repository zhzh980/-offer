# # -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         # write code here
#         flag = False
#         for i in range(len(array)):
#             if target in array[i]:
#                 flag = True
#                 break
#         return flag

"运行时间：220 ms	占用内存：5724K"

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = False
        x = 0
        y = len(array)-1
        print(x,y)
        while y >= 0 and x < len(array[0]):
            if array[y][x] == target:
                flag = True
                break
            elif array[y][x] > target:
                y -= 1
            else:
                x += 1
        return flag
    
while True:
    try:
        so = Solution()
        a = list(eval(input()))
        target = a[0]
        array = a[1]
        print(array)
        print(so.Find(target,array))
    except:
        break