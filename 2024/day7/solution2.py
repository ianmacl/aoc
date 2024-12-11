with open("input_test.txt") as f:
    equations = [x.strip() for x in f.readlines()]
print(equations)


def can_equal(total, numbers):
    if len(numbers) == 1:
        return total == numbers[0]
    first_number = numbers[0]
    if total % first_number == 0 and can_equal(total / first_number, numbers[1:]):
        return True
    if can_equal(total - first_number, numbers[1:]):
        return True
    if len(numbers) >= 2:
        return can_equal(total, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])
    return False

cal_result = 0
for equation in equations:
    elements = equation.split(":")
    result = int(elements[0])
    components = [int(x.strip()) for x in elements[1].strip().split(" ")]
    if can_equal(result, components):
        cal_result += result

print(cal_result)