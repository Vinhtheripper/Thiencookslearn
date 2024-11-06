def draw_pattern_2b(n):
    center = n // 2
    for i in range(n):
        for j in range(n):
            if abs(i - center) + abs(j - center) == center:
                print("+", end=" ")
            elif i < center and j < center and i + j < center:
                print("*", end=" ")
            elif i < center and j > center and j - i > center:
                print("@", end=" ")
            elif i > center and j < center and i - j > center:
                print("@", end=" ")
            elif i > center and j > center and i + j >= center * 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
h=draw_pattern_2b(int(input('Please input n: ')))
print(h)