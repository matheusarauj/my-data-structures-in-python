# cuarenta e dois

def find(numbers, x, best, current, rest):
    if x == len(numbers):
        if rest > 0:
            return float('-inf')
        return current

    if (current <= best) and (current > -1):
        return current

    if rest > 0:
        best = max(best, find(numbers, x + 1, best, current & numbers[x], rest - 1))

    return max(best, find(numbers, x + 1, best, current, rest))


n = int(input())

for i in range(n):
    i, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    result = find(numbers, 0, -1, -1, k)
    print(result)