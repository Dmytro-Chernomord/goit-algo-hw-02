def check_brackets(expression):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = bracket_map.values()

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return "Not Symmetrical"

    return "Symmetrical" if not stack else "Not Symmetrical"


if __name__ == "__main__":
    test_expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "(([]{}))",
        "([)]",
    ]

    for expr in test_expressions:
        result = check_brackets(expr)
        print(f"'{expr}': {result}")
