with open('input.txt') as f:
    reports = [[int(y) for y in x.strip().split(" ")] for x in f.readlines()]

safe_reports = 0

def safe_report(report):
    state = report[0]
    multiplier = 1 if report[1] > report[0] else -1
    for i in range(1, len(report)):
        if (report[i] - report[i-1]) * multiplier not in [1, 2, 3]:
            return 0

    return 1

            
print(sum([safe_report(report) for report in reports]))

#print(safe_reports)