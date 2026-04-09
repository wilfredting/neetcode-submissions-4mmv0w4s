from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        students = deque(students)
        sandwiches = deque(sandwiches)

        while sandwiches and cnt[sandwiches[0]]:
            if students[0] == sandwiches[0]:
                cnt[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())

        return len(students)