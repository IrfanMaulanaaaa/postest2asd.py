def fib_search(arr, x):
    n = len(arr)

    fib2 = 0  # fib(k-2)
    fib1 = 1  # fib(k-1)
    fib = fib2 + fib1  # fib(k)

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while fib > 1:
        i = min(offset+fib2, n-1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and arr[offset+1] == x:
        return offset+1

    return -1


var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# mencari posisi Arsel, Avivah, dan Daiva
print("Arsel di Index", fib_search(var, "Arsel"))
print("Avivah di Index", fib_search(var, "Avivah"))
print("Daiva di Index", fib_search(var, "Daiva"))

# mencari posisi Wahyu di index 3 kolom 0
index_wahyu = fib_search(var[3], "Wahyu")
if index_wahyu != -1:
    print("Wahyu di Index 3 pada kolom", index_wahyu)

# mencari posisi Wibi di index 3 kolom 1
index_wibi = fib_search(var[3], "Wibi")
if index_wibi != -1:
    print("Wibi di Index 3 pada kolom", index_wibi)

