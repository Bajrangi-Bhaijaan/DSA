class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_cnt, students_cnt = [0] * (max(seats) + 1), [0] * (max(students) + 1)
        for seat in seats:
            seats_cnt[seat] += 1
        for student in students:
            students_cnt[student] += 1
        ans = 0
        i = j = 1
        while i < len(students_cnt):
            if students_cnt[i]:
                # find the next available seat
                while j < len(seats_cnt) and not seats_cnt[j]:
                    j += 1
                ans += abs(i - j)
                seats_cnt[j] -= 1
                students_cnt[i] -= 1
            else:
                i += 1
        return ans