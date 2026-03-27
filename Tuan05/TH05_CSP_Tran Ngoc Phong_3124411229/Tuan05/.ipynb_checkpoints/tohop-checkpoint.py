def solve_combinations():
    INPUT_FILE_NAME = "TOHOP.INP"
    # Đọc file input
    try:
        with open(INPUT_FILE_NAME, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{INPUT_FILE_NAME}'.")
        return
    if not lines:
        print("Lỗi chưa nhập input")
        return
    try:
        N, K = map(int, lines[0].strip().split())
    except:
        print("Lỗi ")
        return
    A = []
    for line in lines[1:]:
        c = line.strip()
        if len(c) == 1 and 'A' <= c <= 'Z':
            A.append(c)
        if len(A) == N:
            break
    if len(A) < N:
        N = len(A)
    combinations = []
    def backtrack(cur, start):
        if len(cur) == K:
            combinations.append(cur.copy())
            return
        for i in range(start, N):
            cur.append(A[i])
            backtrack(cur, i + 1)
            cur.pop()

    backtrack([], 0)
    print(len(combinations))
    for c in combinations:
        print(*c)
if __name__ == "__main__":
    solve_combinations()
