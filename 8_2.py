pattern = input()
try:
    while True:
        pattern += input()[-1]
except:
    print(pattern)