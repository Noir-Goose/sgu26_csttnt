import imageio.v2 as imageio
import matplotlib.pyplot as plt
import os
def solve_combinations():
    INPUT_FILE_NAME = "MA.INP"
    OUTPUT_GIF = "02.gif"

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
        N = int(lines[0].strip())
    except:
        print("Lỗi ")
        return
    if N==2 or N==3 or N==4 :
        print(0)
        return 
    board = [[0]*N for _ in range(N)]
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] # cach kinght move
    frames = []
    def save_frame():
        fig, ax = plt.subplots()
        ax.set_xticks(range(N))
        ax.set_yticks(range(N))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True)
        for r in range(N):
            for c in range(N):
                if board[r][c] == 1:
                    ax.text(c, N-r-1, 'Q', ha='center', va='center', fontsize=20)
        plt.xlim(-0.5, N-0.5)
        plt.ylim(-0.5, N-0.5)
        filename = f"frame_{len(frames)}.png"
        plt.savefig(filename)
        frames.append(filename)

    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N and board[r][c] == -1
        
    def backtracking(c,r,step ):
        board  [c][r]= step
        save_frame()
        if step ==N*N:
            return True 
        for dr, dc in moves :
            nr , nc = c+dr , r+dc
            if is_valid (nr , nc ):
                if backtracking(nr , nc ,step+c):
                    return True 
        board[c][r] = -1
    
    
    if backtracking(0,0,1):
        print(1)
        for r in board:
            print(*r)
    else:
        print(0)
    if frames: # tạo gif
        with imageio.get_writer(OUTPUT_GIF, mode='I', duration=0.5) as writer:
            for filename in frames:
                image = imageio.imread(filename)
                writer.append_data(image)

        for filename in frames:
            os.remove(filename)

        print(f"Đã tạo file GIF: {OUTPUT_GIF}")
if __name__ == "__main__":
    solve_combinations()
