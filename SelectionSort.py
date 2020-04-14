def selection_sort(numbers):
    for i in range(len(numbers)):
        for index in range(len(numbers) - i):
            if numbers[index + i] < numbers[i]:
                swap(numbers, index + i, i)

def swap(numbers, a, b):
    numbers[a], numbers[b] = numbers[b], numbers[a]


if __name__ == '__main__':
    numbers = [17, 41, 5, 22, 54, 6, 29, 3, 13]

    print(numbers)
    selection_sort(numbers)
    print(numbers)