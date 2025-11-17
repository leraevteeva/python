def is_year_leap(year):
    return year % 4 == 0


if __name__ == "__main__":
    test_year = 2024
    result = is_year_leap(test_year)

    print(f"год {test_year}: {result}")
