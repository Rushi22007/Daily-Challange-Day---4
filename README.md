### maximum sum of two non-overlapping events

this problem asks us to select at most two events such that they do not overlap in time and the total value obtained is maximum. each event is given with a start time, end time, and value.

the solution first sorts all events by their start time. this makes it easier to search for the next valid event that can be attended after the current one.

a suffix maximum array is created to store the maximum event value available from a given index to the end. this helps in quickly finding the best possible second event.

for each event, we treat it as the first event and use binary search to find the next event whose start time is greater than the current event’s end time. if such an event exists, its best value is added using the suffix array.

the maximum sum is updated at each step. by combining sorting, suffix maximum, and binary search, the solution efficiently finds the correct answer.

the time complexity of this approach is o(n log n) and the space complexity is o(n), making it suitable for large inputs on leetcode.
