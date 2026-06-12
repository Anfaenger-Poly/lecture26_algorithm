while True:
    s = input()
    if s == ".":
        break
        
    stack = []
    is_valid = True
        
    for char in s:
        if char in "(":
            stack.append(char)
        elif char in "[":
            stack.append(char)
        
        elif char == ")":
            if len(stack) == 0 or stack[-1] != "(":
                is_valid = False
                break
            stack.pop()
        
        elif char == "]":
            if len(stack) == 0 or stack[-1] != "[":
                is_valid = False
                break
            stack.pop()
            
    if is_valid and len(stack) == 0:
        print("yes")
    else:
        print("no")