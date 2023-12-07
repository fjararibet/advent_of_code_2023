d = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    }
with open("test_input_2") as f:
    input = f.read()
    print(input)
    lines = input.split("\n")
    sum = 0
    for word in lines:
        first = None
        second = None
        for c in word:
            if c in d:
                if not first:
                    first = c
                second = c
        if first and second:
            calibration = first + second
            sum += int(calibration)
    print(sum)
