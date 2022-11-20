translator = {"A":"T","T":"A","C":"G","G":"C"}
pattern = input()
result = []
for i in range(len(pattern)):
    result.insert(0, translator[pattern[i]])
print("".join(result))