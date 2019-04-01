
def find_shaded_box(A):

    def find_middle(left, right):
        return (left + right) // 2

    length = len(A)

    s = 0
    while 2 ** (s - 1) < length:
        divide_factor = 2 ** s

        for i in range(divide_factor):
            print(find_middle(length * i // divide_factor,
                              length * (i + 1) // divide_factor - 1))
            #print((length + (2 * length * i) - 2) // (2 * divide_factor))
            # print(
            #    f'Left {length * i // divide_factor }, Right {length * (i + 1)  // divide_factor - 1}')

        print(f"Moving factor up to {s+1}")
        s += 1


a = [0] * 9
find_shaded_box(a)
