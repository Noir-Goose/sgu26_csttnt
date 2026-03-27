import imageio.v2 as imageio
import matplotlib.pyplot as plt
import os
def solve_combinations():
    INPUT_FILE_NAME = "QUEEN.INP"
    OUTPUT_GIF = "01.gif"

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
    
    banco = [[0]*N for _ in range(N)]
    cot = [False]*N
    duongcheo1 = [False]*(2*N)
    duongcheo2 = [False]*(2*N)
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
                if banco[r][c] == 1:
                    ax.text(c, N-r-1, 'Q', ha='center', va='center', fontsize=20)
        plt.xlim(-0.5, N-0.5)
        plt.ylim(-0.5, N-0.5)
        filename = f"frame_{len(frames)}.png"
        plt.savefig(filename)
        plt.close(fig)
        frames.append(filename)
    def backtracking(row):
        if row == N:
            return True
        for c in range(N):
            if not cot[c] and not duongcheo1[row - c + N] and not duongcheo2[row + c]:
                banco[row][c] = 1
                cot[c] = True
                duongcheo1[row - c + N] = duongcheo2[row + c] = True
                save_frame()
                if backtracking(row + 1):
                    return True
                
                banco[row][c] = 0
                cot[c] = False
                duongcheo1[row - c + N] = duongcheo2[row + c] = False

                save_frame()
                
        return False
    if backtracking(0):
        print(1)
        for r in banco:
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
