import sys

print("=== Command Quest ===")
if (len(sys.argv) == 1):
    print("No arguments provided!")
print(f"Programme name: {sys.argv[0]}")
if (len(sys.argv) > 1):
    print("Arguments received:", len(sys.argv) - 1)
for i in range(len(sys.argv) - 1):
    print(f"Argument {i+1}: {sys.argv[i+1]}")
print(f"Total arguments: {len(sys.argv)}")
