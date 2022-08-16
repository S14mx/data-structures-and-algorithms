
def quick_sort(list: list[int]) -> list[int]:

    try:
        if len(list) < 2:
            return list

        else:
            pivot = list[0]
            lesser_list = [num for num in list[1:] if num <= pivot]
            greater_list = [num for num in list[1:] if num > pivot]

            return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)

    except:

        return "Input list contains non-integers"
