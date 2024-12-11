with open("input.txt") as f:
    equations = [x.strip() for x in f.readlines()]
print(equations)


def can_equal(total, numbers):
    if len(numbers) == 1:
        return total == numbers[0]
    last_number = numbers[len(numbers) - 1]
    if total % last_number == 0 and can_equal(total / last_number, numbers[:-1]):
        return True
    if can_equal(total - last_number, numbers[:-1]):
        return True
    return False

cal_result = 0
for equation in equations:
    elements = equation.split(":")
    result = int(elements[0])
    components = [int(x.strip()) for x in elements[1].strip().split(" ")]
    if can_equal(result, components):
        cal_result += result

print(cal_result)