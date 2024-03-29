
def insertion_sort(list: list[int]) -> list[int]:
    try:
        if len(list) == 0:
            return list

        for i in range(1, len(list)):
            j = i
            while j > 0 and list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
                j -= 1

        return list

    except:

        return "Input list contains non-integers"
