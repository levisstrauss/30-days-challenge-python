import heapq


def maxLearning(courses):
    # Sort the courses based on deadline
    courses.sort(key=lambda x: x[1])

    total_value = 0
    max_heap = []

    for _, deadline, value in courses:
        # Push the negative value because heapq is a min-heap
        heapq.heappush(max_heap, -value)
        total_value += value

        # If the number of courses in the heap exceeds the deadline,
        # we need to remove the course with the highest value
        if len(max_heap) > deadline:
            total_value += heapq.heappop(max_heap)  # Add the popped value (negative becomes positive)

    return len(max_heap), total_value


# Test
print(maxLearning([(1, 2, 30), (2, 2, 40), (3, 1, 10), (4, 1, 10)]))  # Expected output: (2, 70)
print(maxLearning([(1, 1, 40), (2, 1, 50), (3, 1, 60)]))  # Expected output: (1, 60)
