def zip_lists(a, b):
    current1 = a.head
    current2 = b.head
    temp1 = None
    temp2 = None
    if current1:
        temp1 = current1.next
    elif current2:
        return b
    else:
        return None
    if current2:
        temp2 = current2.next
    elif current1:
        return a
    while temp1 and temp2:
        current1.next = current2
        current2.next = temp1
        current1 = temp1
        current2 = temp2
        temp1 = current1.next
        temp2 = current2.next
    if current1:
        current1.next = current2
    if temp1:
        current2.next = temp1
    return a
