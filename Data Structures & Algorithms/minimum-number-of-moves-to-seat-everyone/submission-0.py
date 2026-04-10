class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        res = 0
        for i in range(len(seats)):
            while students[i] != seats[i]:
                if students[i] < seats[i]:
                    students[i] += 1
                else:
                    students[i] -= 1
                res += 1
        return res