def zip_lists(a, b):
    #     current1 = a.head
    #     current2 = b.head
    #     # temp1 = current1.next
    #     # temp2 = current2.next
    #     if current1 and current1.next:
    #         temp1 = current1.next
    #     elif current2:
    #         return b
    #     else:
    #         return None
    #     if current2 and current2.next:
    #         temp2 = current2.next
    #     elif current1:
    #         return a
    #     while temp1 and temp2:
    #         current1.next = current2
    #         current2.next = temp1
    #         current1 = temp1
    #         current2 = temp2
    #         temp1 = current1.next
    #         temp2 = current2.next
    #     if current1:
    #         current1.next = current2
    #     if temp1:
    #         current2.next = temp1
    #     return a

    if a.head is None and b.head is None:
        return None
    if a.head is None or b.head is None:
        return a or b
        # return a if a.head else b

    current1 = a.head
    current2 = b.head

    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next
        current1.next = current2
        if temp1:
            current2.next = temp1
        current1 = temp1
        current2 = temp2
    return a
