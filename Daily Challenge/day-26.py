class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for booked_start, booked_end in self.calendar:
            if start < booked_end and end > booked_start:
                return False

        self.calendar.append((start, end))
        print(self.calendar)
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()

param_1 = obj.book(10, 20)
param_2 = obj.book(15, 25)
param_3 = obj.book(20, 30)
print(param_1)
print(param_2)
print(param_3)