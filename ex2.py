def mysum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(f"Test with no args retuns: {mysum()}")
print(f"Test with some numbers returns: {mysum(1,2,3)}")
print(f"Test with an iterable (needs * to unpack in order to avoid TypeError) returns: {mysum(*[1,2 ,3])}")