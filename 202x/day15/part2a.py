import re

with open('/Users/imaclennan/build/play/aoc/day15/input.txt') as f:
    lines = [x.strip() for x in f.readlines()]

line_parser = re.compile('Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)')

def reduce_intervals(intervals):
    new_intervals = []
    collapsed = True
    while collapsed:
        collapsed = False
        for i in range(0, len(intervals) - 1):
            for j in range(i+1, len(intervals)):
                interval1 = intervals[i]
                interval2 = intervals[j]
                if interval1 == None or interval2 == None:
                    continue
                if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
                    collapsed = True
                    intervals.append([min(interval1[0], interval2[0]), max(interval1[1], interval2[1])])
                    intervals[i] = None
                    intervals[j] = None
                elif interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
                    collapsed = True
                    intervals.append([min(interval1[0], interval2[0]), max(interval1[1], interval2[1])])
                    intervals[i] = None
                    intervals[j] = None

        intervals = [interval for interval in intervals if interval]
    return [interval for interval in intervals if interval]


line_count = 0
start_point = 0
end_point = 4000000
for i in range(3420000, 4000001):
    if i % 10000 == 0:
        print(i)
    intervals = []
    for line in lines:
        parsed_line = line_parser.match(line)
        (sensor_x, sensor_y, beacon_x, beacon_y) = (int(parsed_line.group(1)), int(parsed_line.group(2)), int(parsed_line.group(3)), int(parsed_line.group(4)))
        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        remaining_distance = distance - abs(i - sensor_y)
        if remaining_distance > 0:
            interval_start = max(start_point, sensor_x - remaining_distance)
            interval_end = min(end_point, sensor_x + remaining_distance)
            intervals.append([interval_start, interval_end])

    reduced_intervals = reduce_intervals(intervals)
    if len(reduced_intervals) > 1:
        x = 2749047 
        y = 3429555
        print(x * 4000000 + y)
        print(reduced_intervals)
        print(i)
        print("found")
        exit()


# x = 2749047 
# y = 3429555