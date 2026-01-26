class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        student = 0

        if self.students:
            # the distance is the distance to the closest student
            dist = self.students[0]
            for i, seat in enumerate(self.students):
                if i:
                    prev = self.students[i - 1]

                    d = (seat - prev) // 2
                    if d > dist:
                        dist = d
                        student = prev + d

            # account for right
            d = self.n - 1 - self.students[-1]
            if d > dist:
                student = self.n - 1
            
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        if p in self.students:
            self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)