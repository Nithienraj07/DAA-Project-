def binary_search(books, target):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2

        if books[mid] == target:
            return mid
        elif books[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
books = list(map(int, input("Enter sorted book IDs separated by space: ").split()))
target = int(input("Enter book ID to search: "))

# Search
result = binary_search(books, target)

# Output
if result != -1:
    print("Book found at index", result)
else:
    print("Book not found")