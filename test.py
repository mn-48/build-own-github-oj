# test.py
def test_case():
    # Example test case
    result = 5 + 2
    expected = 2
    return result == expected


if __name__ == "__main__":
    if test_case():
        print("Yes")
    else:
        print("This test case does not pass")
