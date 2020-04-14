def bubble_sort(numbers):
    finished = False

    while not finished:
        finished = True
        for index in range(len(numbers) - 1):
            if numbers[index] > numbers[index + 1]:
                swap(numbers, index, index + 1)
                finished = False
            
def swap(numbers, a, b):
    numbers[a], numbers[b] = numbers[b], numbers[a]


if __name__ == '__main__':
    numbers = [17, 41, 5, 22, 54, 6, 29, 3, 13]

    print(numbers)
    bubble_sort(numbers)
    print(numbers)