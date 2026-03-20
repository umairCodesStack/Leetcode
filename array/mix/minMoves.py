class Solution(object):
    def minMovesToSeat(self, seats, students):
        moves=0
        seats.sort()
        students.sort()
        print(seats,students)
        for i in range(len(students)):
            x=students[i]
            while(x!=seats[i]):
                x+=1
                moves+=1
        return moves

print(Solution().minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6]))
        