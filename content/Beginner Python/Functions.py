def add_numbers(a, b):
    # Write your code here
    pass

# ---------------------------------------------------------
# Don't modify the code below
def check_answer():
    test_cases = [
        ((2, 3), 5),
        ((-1, 1), 0),
        ((0, 0), 0)
    ]
    
    try:
        for (inputs, expected) in test_cases:
            result = add_numbers(*inputs)
            assert result == expected, f"❌ Test Failed: add_numbers{inputs} → Expected {expected}, got {result}"
        
        print("✅ All test cases passed!")
    
    except Exception as e:
        print(f"Error: {str(e)}")

check_answer()