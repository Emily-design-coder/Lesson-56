code = ""

print("Paste your Python code below.")
print("Type END when finished:\n")

while True:
    line = input()

    if line == "END":
        break

    code += line + "\n"

loop_count = code.count("for ") + code.count("while ")
recursive_calls = code.count("myfunction")

print("TIME COMPLEXITY RESULT")

if recursive_calls >= 2 and "n/2" in code:
    print("Detected: Recursive Function")
    print("Possible Complexity:")
    print("T(n)=T(n/2)+T(n/3)+O(n)")
    print("Approx Complexity: O(n)")
elif loop_count == 0:
    print("Time Complexity: O(1)")

elif loop_count == 1:
    print("Time Complexity: O(n)")

elif loop_count == 2:
    print("Time Complexity: O(n²)")

elif loop_count == 3:
    print("Time Complexity: O(n³)")

else:
    print("Complexity could not be determined.")

print("=========================")