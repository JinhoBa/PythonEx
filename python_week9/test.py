def is_even(x):
    if x % 2 == 0:
        return True
    return False

arr1 = []
for val in range(1,11):
    if is_even(val):
        arr1.append(val)

print(f"arr function : {arr1}")