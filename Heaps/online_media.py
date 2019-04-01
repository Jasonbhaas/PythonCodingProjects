import heapq


def online_median(sequence):
    left_half, right_half, result = [], [], []
    med = sequence[0]
    print(med)
    odd = None
    for val in sequence:
        if odd is None:
            med = val
            odd = True
        elif odd:
            if val >= -1 * left_half[0]:
                med = heapq.heappushpop(right_half, val)
            else:
                med = heapq.heappushpop(left_half, val)
        else:
            if val > med:
                heapq.heappush(right_half, val)
                heapq.heappush(left_half, med * -1)
            else:
                heapq.heappush(right_half, med)
                heapq.heappush(left_half, val * -1)
            med = (right_half[0] - left_half[0]) / 2
        result.append(med)
        odd ^= True
    return result


print(online_median([5, 4, 3, 2, 1]))
print(online_median([5, 4, 3, 2, 1]))
