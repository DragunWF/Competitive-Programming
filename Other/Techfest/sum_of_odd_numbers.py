def sum_of_odds(numbers):
    return sum(number for number in numbers if number % 2 != 0)


if __name__ == '__main__':
    input()
    numbers = list(map(int, input().split()))
    print(sum_of_odds(numbers))
