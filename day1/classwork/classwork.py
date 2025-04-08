def truth_or_lie(truth, my_answer):
    if my_answer == truth:
        return 'true'
    else:
        return 'false'

# Example usage
print(truth_or_lie("yes", "yes"))