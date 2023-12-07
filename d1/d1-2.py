d = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calibrate(word):
    first = None
    second = None
    i = 0
    while i < len(word):
        num = word[i]
        if num in d:
            if not first:
                first = num
            second = num
        # holaqueone
        if i < len(word) - 2:
            num = word[i:i+3]
            if num in d:
                if not first:
                    first = num
                second = num

        if i < len(word) - 3:
            num = word[i:i+4]
            if num in d:
                if not first:
                    first = num
                second = num
        if i < len(word) - 4:
            num = word[i:i+5]
            if num in d:
                if not first:
                    first = num
                second = num
        i += 1
    return first, second


with open("input2") as f:
    input = f.read()
    lines = input.split("\n")
    sum = 0
    for word in lines:
        # print(word)
        first, second = calibrate(word)
        if first and second:
            calibration = d[first] + d[second]
            sum += int(calibration)
    print(sum)
