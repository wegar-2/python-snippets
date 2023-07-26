from functools import cache
from collections import defaultdict

@cache
def fibo(n: int) -> int:
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


def fibo_list(n: int) -> list[int]:
    out = [1, 1]
    if n<=2:
        return [1]*n
    for k in range(3, n+1, 1):
        out.append(out[k-2] + out[k-1])
    return out


if __name__ == "__main__":
    for i in range(40):
        print(fibo(i))
