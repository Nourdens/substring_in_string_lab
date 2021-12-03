from datetime import datetime

class MainApplication:
    def Rabin_Karp(self, text, pattern):
        start_time = datetime.now()
        SearchingFor = open(pattern, 'r', encoding="utf8")
        pat = SearchingFor.read()

        SearchingIn = open(text, 'r', encoding="utf8")
        txt = SearchingIn.read()

        SimpleNumber = 257
        AlphabetLength = 256
        M = len(pat)
        N = len(txt)
        i = 0
        j = 0
        HashPattern = 0  # хэш-значение для шаблона
        HashText = 0  # хэш-значение для txt
        h = 1
        for i in range(M - 1):
            h = (h * AlphabetLength) % SimpleNumber

        # вычисляем хэши первых M элементов
        for i in range(M):
            HashPattern = (AlphabetLength * HashPattern + ord(pat[i])) % SimpleNumber
            HashText = (AlphabetLength * HashText + ord(txt[i])) % SimpleNumber


        # скользящее окно длины M начиная с M+1 элемента
        for i in range(N - M + 1):
            if HashPattern == HashText:
                # Проверяем коллизию
                for j in range(M):
                    if txt[i + j] != pat[j]:
                        break
                j += 1
                if j == M:
                    print("Rabin Karp algorithm. \nFound at:", str(i))

            if i < N - M:
                # пересчитываем хэш скользящего окна, вычитая значение выкидываемого элемента, и добавляя новый
                HashText = (AlphabetLength * (HashText - ord(txt[i]) * h) + ord(txt[i + M])) % SimpleNumber

                # Не допускаем отрицательного значения хэша, держим в [0, SimpleNumber) интервале
                if HashText < 0:
                    HashText = HashText + SimpleNumber
        print("Rabin-Karp Time on ", text, " and ", pattern, ":\n", datetime.now() - start_time, '\n')
        SearchingFor.close()
        SearchingIn.close()

    def Knuth_Morris_Pratt(self, text, pattern):
        SearchingFor = open(pattern, 'r', encoding="utf8")
        t = SearchingFor.read()
        p = [0] * len(t)
        j = 0
        i = 1

        start_time = datetime.now()

        while i < len(t):
            if t[j] == t[i]:
                p[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j - 1]

        SearchingIn = open(text, 'r', encoding="utf8")
        a = SearchingIn.read()

        m = len(t)
        n = len(a)

        i = 0
        j = 0
        while i < n:
            if a[i] == t[j]:
                i += 1
                j += 1
                if j == m:
                    print("Knuth Morris Pratt algorithm. \nFound at:", (i - j))
                    print("Knuth Morris Pratt Time on ", text, " and ", pattern, ":\n", datetime.now() - start_time)
                    break
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1

        if (i == n) and (j != m):
            print("Didn`t find")

        SearchingFor.close()
        SearchingIn.close()

    def __init__(self, text, pattern):
        self.Rabin_Karp(text, pattern)
        self.Knuth_Morris_Pratt(text, pattern)


texts = ('good_t_3.txt', 'good_t_4.txt', 'bad_t_3.txt', 'bad_t_4.txt')
patterns = ('good_w_3.txt', 'good_w_4.txt', 'bad_w_3.txt', 'bad_w_4.txt')
for i, j in zip(texts, patterns):
    MainApplication(i, j)
    print('\n')
