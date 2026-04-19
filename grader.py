def grader(reached, steps):
    if not reached:
        return 0.1
    return max(0.1, 1 - steps/20)