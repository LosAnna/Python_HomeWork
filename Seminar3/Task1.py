# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def fibonacci_elements(N):
    f1, f2 = 1, 1
    with open('text.txt', 'w', encoding='utf-8') as ouf:
        ouf.write(f'Последовательность фибоначчи от {N}: \n')
        for i in range(1, N + 1):
            ouf.write(str(f1) + ' ')
            f1, f2 = f2, f1 + f2


def main():
    N = int(input())
    fibonacci_elements(N)


if __name__ == '__main__':
    main()