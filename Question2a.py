def draw_pattern_2a(n):
    center = n // 2
    for i in range(n):
        for j in range(n):
            if i == center or j == center:
                print("+", end=" ")
            elif i < center and j < center and i + j >= center:
                print("*", end=" ")
            elif i > center and j > center and i + j <= center * 3:
                print("*", end=" ")
            elif i < center and j > center and j - i <= center:
                print("@", end=" ")
            elif i > center and j < center and i - j <= center:
                print("@", end=" ")
            else:
                print(" ", end=" ")
        print()
l=draw_pattern_2a(int(input('Please input n: ')))
print(l)


