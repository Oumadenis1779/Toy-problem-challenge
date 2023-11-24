#  Converting 12-hour time to 24-hour time

def convert_to_24_hour_format(hour, minute, period):
    if period.lower() == "am" and hour == 12:

        # 12:xx am should be converted to 00:xx in 24-hour format
        hour = 0
    elif period.lower() == "pm" and hour != 12:
        # Add 12 to the hour for any PM time except 12:xx pm
        hour += 12

    # Formating the hour and minute as a four-digit string

    time_24_hour = "{:02d}{:02d}".format(hour, minute)

    return time_24_hour

# Examples:
time_24_hour_1 = convert_to_24_hour_format(8, 30, "am")
time_24_hour_2 = convert_to_24_hour_format(8, 30, "pm")
time_24_hour_3 = convert_to_24_hour_format(12, 15, "am")
time_24_hour_4 = convert_to_24_hour_format(12, 0, "pm")

print(time_24_hour_1)  
print(time_24_hour_2)
print(time_24_hour_3) 
print(time_24_hour_4) 


# Two numbers are positive
def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

# Examples:
print(exactly_two_positive(2, 4, -3))    
print(exactly_two_positive(-4, 6, 8))    
print(exactly_two_positive(4, -6, 9))    
print(exactly_two_positive(-4, 6, 0))    
print(exactly_two_positive(4, 6, 10))    
print(exactly_two_positive(-14, -3, -4))


# Constant value
def solve(s):
    vowels = "aeiou"
    consonant_values = {letter: ord(letter) - ord('a') + 1 for letter in set(s) if letter not in vowels}
    
    consonant_substrings = [s[start:end] for start in range(len(s)) for end in range(start + 1, len(s) + 1) if all(char not in vowels for char in s[start:end])]
    
    max_value = 0
    for substring in consonant_substrings:
        substring_value = sum(consonant_values[char] for char in substring)
        max_value = max(max_value, substring_value)
    
    return max_value

# Examples:
print(solve("zodiacs"))  
print(solve("strength"))  
