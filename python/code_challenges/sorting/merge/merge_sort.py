
def merge_sort(list: list[int]) -> list[int]:

    if len(list) <= 1:

        return list

    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    merge_sort(left_half)

    merge_sort(right_half)

    return merge_helper(left_half, right_half, list)


def merge_helper(left_half, right_half, list):
    try:

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1

            k += 1

            if i == len(left_half):
                for num in right_half[j:]:
                    list[k] = num
                    k += 1

        else:
            for num in left_half[i:]:
                list[k] = num
                k += 1
    except:

        return "Input list contains non-integers"
