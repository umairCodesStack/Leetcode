class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
       count=hours.count(target)
       return count
print(Solution().numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))
        