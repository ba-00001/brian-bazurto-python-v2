# Assignment 1 - Intro to Python
# Brian Bazurto


# Task 1: Hello
def hello():
    return "Hello!"


# Task 2: Greet with a formatted string
def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return f"Unknown operation: {operation}"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# Task 4: Data type conversion
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


# Task 5: Grading system, using *args
def grade(*args):
    try:
        average = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Task 6: Use a for loop with a range
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result


# Task 7: Student scores, using **kwargs
def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = None
        best_score = None
        for name, score in kwargs.items():
            if best_score is None or score > best_score:
                best_name = name
                best_score = score
        return best_name
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)


# Task 8: Titleize, with string and list operations
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    for i, word in enumerate(words):
        # first and last word always get capitalized
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
    return " ".join(words)


# Task 9: Hangman, with more string operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result


# Task 10: Pig Latin
def pig_latin(text):
    vowels = "aeiou"
    converted = []
    for word in text.split():
        if word[0] in vowels:
            converted.append(word + "ay")
            continue
        # move consonants (and "qu" as one unit) to the end
        i = 0
        while i < len(word) and word[i] not in vowels:
            if word[i:i + 2] == "qu":
                i += 2
                break
            i += 1
        converted.append(word[i:] + word[:i] + "ay")
    return " ".join(converted)


# quick checks when running the file directly
if __name__ == "__main__":
    print(hello())
    print(greet("Brian"))
    print(calc(10, 0, "divide"))
    print(calc(2, 8, "power"))
    print(data_type_conversion("nonsense", "float"))
    print(grade(91, 84, 78))
    print(repeat("ha", 3))
    print(student_scores("best", Ana=88, Leo=93, Mia=79))
    print(titleize("the lord of the rings"))
    print(hangman("alphabet", "ab"))
    print(pig_latin("the quick brown fox"))
