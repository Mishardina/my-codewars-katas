def elevator(left, right, call):
    if abs(call - left) >= abs(call - right):
        return "right"
    else:
        return "left"