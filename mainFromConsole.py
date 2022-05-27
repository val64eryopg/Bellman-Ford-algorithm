def main():
    # N - количество вершин
    n = int(input())
    # mas - массив из путей направленых
    mas = [0] * n

    for i in range(n):
        mas[i] = [-10 ** 9] * n

    for peaks in range(n):
        b = input()
        z = [int(x) for x in b.split()]
        for i in range(len(z)):
            if not (i % 2 == 0 and z[i] == 0):
                if i % 2 == 0:
                    mas[peaks][z[i] - 1] = z[i + 1]


    start = int(input())
    end = int(input())

    bellmanFord(start - 1, mas, n, end - 1)


def bellmanFord(start, W, N, end):
    INF = -10 ** 9
    F = [[INF] * N for i in range(N)]
    F[0][start] = 1
    previous = {}

    print("---")

    for k in range(1, N):
        for i in range(N):
            F[k][i] = F[k - 1][i]
            for j in range(N):
                if not(F[k - 1][j] == INF) and not(W[j][i] == INF) and F[k - 1][j] * W[j][i] > F[k][i] :
                    previous[i] = j
                    F[k][i] = F[k - 1][j] * W[j][i]
    for i in F:
        print(i)
    for i in range(len(F[-1])):
        if i == end and not (F[-1][i] == INF):
            print("Y")
            path = []
            endEl = end
            while not (endEl == start):
                path.append(endEl + 1)
                endEl = previous.get(endEl)
            path.append(start + 1)
            path.reverse()
            print(path)
            print(F[-1][i])

        else:
            if i == end:
                print("N")


if __name__ == '__main__':
    main()
