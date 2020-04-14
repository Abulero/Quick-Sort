def quick_sort(A, low=None, hi=None):
    if low is None or hi is None:
        quick_sort(A, 0, len(A)-1)
    elif low < hi:
	    p = partition(A, low, hi)
	    quick_sort(numbers, low, p - 1)
	    quick_sort(numbers, p + 1, hi)
	
def get_pivot(numbers, low, hi):
	mid = (hi + low) // 2
	s = sorted([numbers[low], numbers[mid], numbers[hi]])

	if s[1] == numbers[low]:
		return low
	elif s[1] == numbers[mid]:
		return mid

	return hi
	
def partition(numbers, low, hi):
	pivot_index = get_pivot(numbers, low, hi)
	pivot_value = numbers[pivot_index]
	numbers[pivot_index], numbers[low] = numbers[low], numbers[pivot_index]
	border = low

	for i in range(low, hi+1):
		if numbers[i] < pivot_value:
			border += 1
			numbers[i], numbers[border] = numbers[border], numbers[i]
	numbers[low], numbers[border] = numbers[border], numbers[low]

	return (border)


if __name__ == '__main__':
    numbers = [17, 41, 5, 22, 54, 6, 29, 3, 13]

    print(numbers)
    quick_sort(numbers)
    print(numbers)