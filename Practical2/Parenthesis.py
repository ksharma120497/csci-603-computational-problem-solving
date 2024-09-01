
from Stack import Stack

def check_for_brackets(input):
    s = Stack()
    # s.push(input[0])
    for i in range(len(input)):
        if s.isEmpty():
            s.push(input[i])
            continue
        if s.peek() == "(" and input[i] == ")":
           s.pop()
        s.push(input[i])

    if s.size() == 0:
        return True
    return False


if __name__ == "__main__":
    input = "(()(())())"
    print(check_for_brackets(input))