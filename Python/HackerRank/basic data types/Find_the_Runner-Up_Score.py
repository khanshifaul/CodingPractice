if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    # n = 5
    # arr = [2, 3, 6, 6, 5]
    arr = list(arr)
    print(max([a for a in arr if a!=max(arr)]))
