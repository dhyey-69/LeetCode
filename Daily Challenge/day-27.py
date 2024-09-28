# 731. My Calendar II

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendarTwo class:

# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

# Example 1:

# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]

# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked. 
# myCalendarTwo.book(50, 60); // return True, The event can be booked. 
# myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
# myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.

class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for o_start, o_end in self.overlaps:
            if start < o_end and end > o_start:
                return False

        for e_start, e_end in self.events:
            if start < e_end and end > e_start:
                overlap_start = max(start, e_start)
                overlap_end = min(end, e_end)
                self.overlaps.append((overlap_start, overlap_end))
        
        self.events.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
param_1 = obj.book(10,20)
param_2 = obj.book(50,60)
param_3 = obj.book(10,40)
param_4 = obj.book(5,15)
param_5 = obj.book(5,10)
param_6 = obj.book(25,55)

print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
print(param_6)