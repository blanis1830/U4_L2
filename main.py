from StackClass import ArrayStack
import os


def reversed(original):
    new = ""
    stack = ArrayStack()
    for char in original:
        stack.push(char)
    while len(stack) > 0:
        new += stack.pop()
    return new
        
def main():
    original = "Sphinx of black quartz, judge my vow"
    new = reversed(original)
    print(f"Original: {original}\n")
    print(f"New: {new}")

if __name__ == "__main__":
    os.system("clear")
    main()