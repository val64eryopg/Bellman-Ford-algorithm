def main():
    inputT = []
    with open('C:\\Users\\user\\PycharmProjects\\fordBellman\\venv\\input.txt', 'r') as f:
        for line in f:
            inputT.append(line)

    n = int(inputT[0])

    mas = [0] * n
    for i in range(n):
        mas[i] = [-10 ** 9] * n

    for i in range(1, n+1):
        z = [int(x) for x in inputT[i].split()]
        for x in range(len(z)):
            if not (x % 2 == 0 and z[x] == 0):
                if x % 2 == 0:
                    mas[i-1][z[x] - 1] = z[x+1]

    start = int(inputT[-2])

    end = int(inputT[-1])


    bellmanFord(start - 1, mas, n, end - 1)


def bellmanFord(start, W, N, end):
    INF = -10 ** 9
    F = [[INF] * N for i in range(N)]
    F[0][start] = 1
    previous = {}


    for k in range(1, N):
        for i in range(N):
            F[k][i] = F[k - 1][i]
            for j in range(N):
                if not(F[k - 1][j] == INF) and not(W[j][i] == INF) and F[k - 1][j] * W[j][i] > F[k][i] :
                    previous[i] = j
                    F[k][i] = F[k - 1][j] * W[j][i]
    for i in F:
        print(i)
    result = ''
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
            result = "Y" + "\n" + ' '.join(str(x) for x in path) + "\n" + str(F[-1][i])
        else:
            if i == end:
                print("N")
                result = "N"
        with open('C:\\Users\\user\\PycharmProjects\\fordBellman\\venv\\output.txt', 'w+') as f:
            f.write(result)
if __name__ == '__main__':
    main()
