def bubble_sort(seznam, x):
    for x in seznam:
        prvek=seznam[x+1]
        if x > prvek:
            prvek=x
