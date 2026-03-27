FI = "Input_Asao.inp"

from heapq import heappush, heappop
from itertools import count

Inbuoc = False 
Taogif = True  

ketthuc_POS = {}

def read_input(fi):
    with open(fi, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    if len(lines) < 6:
        raise ValueError('ít nhất đủ 6 dòng dữ liệu trong file ')
    batdauchuoi = [list(map(int, lines[i].split())) for i in range(3)]
    ketthucchuoi = [list(map(int, lines[i].split())) for i in range(3, 6)]
    batdau = tuple(sum(batdauchuoi, []))
    ketthuc = tuple(sum(ketthucchuoi, []))
    return batdau, ketthuc

def print_board(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) for x in state[i:i+3]))
    print()

def manhattan(state, ketthuc):
    # tính khoảng cách Manhattan
    pos_ketthuc = {tile: (i // 3, i % 3) for i, tile in enumerate(ketthuc)}
    dist = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        r, c = divmod(i, 3)
        gr, gc = pos_ketthuc[tile]
        dist += abs(r - gr) + abs(c - gc)
    return dist

def get_neighbors(state):
    neighbors = []
    z = state.index(0)
    r, c = divmod(z, 3)
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')] # Điều hướng
    for dr, dc, name in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr * 3 + nc
            lst = list(state)
            lst[z], lst[nz] = lst[nz], lst[z]
            neighbors.append((tuple(lst), name))
    return neighbors

def inversions(state):
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def is_solvable(batdau, ketthuc):
    # để kiểm tra tính khả thi, số nghịch đảo của hai trạng thái phải có cùng chẵn lẻ
    return (inversions(batdau) % 2) == (inversions(ketthuc) % 2)

def a_star(batdau, ketthuc):
    if batdau == ketthuc:
        return [batdau], []
    if not is_solvable(batdau, ketthuc):
        return None, None

    counter = count()
    open_heap = []  # nhập hàng đợi ưu tiên
    g_score = {batdau: 0}
    came_from = {}
    move_from = {}

    h0 = manhattan(batdau, ketthuc)
    heappush(open_heap, (h0, next(counter), 0, batdau))

    closed = set()

    while open_heap:
        f, _, g, current = heappop(open_heap)
        if current == ketthuc:
            # tạo lại đường đã đi
            path = []
            moves = []
            cur = current
            while cur in came_from:
                path.append(cur)
                moves.append(move_from[cur])
                cur = came_from[cur]
            path.append(cur)
            path.reverse()
            moves.reverse()
            return path, moves

        closed.add(current)

        for neighbor, move_name in get_neighbors(current):
            if neighbor in closed:
                continue
            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                move_from[neighbor] = move_name
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan(neighbor, ketthuc)
                heappush(open_heap, (f_score, next(counter), tentative_g, neighbor))

    return None, None

def animate_solution(path, moves=None, save_file='solution.gif', interval=700): #In gif
    try:
        import matplotlib.pyplot as plt 
        from matplotlib.animation import FuncAnimation, PillowWriter # thư viện để tạo ảnh động
    except Exception as e:
        raise RuntimeError('cái matplot để tạo ảnh gif ' + str(e))

    def draw_state(ax, state):
        ax.clear()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(-0.5, 2.5)
        # vẽ lưới
        for x in range(4):
            ax.plot([x-0.5, x-0.5], [-0.5, 2.5], color='black')
            ax.plot([-0.5, 2.5], [x-0.5, x-0.5], color='black')
        for idx, val in enumerate(state):
            r, c = divmod(idx, 3)
            ax.text(c, 2 - r, str(val) if val != 0 else '', ha='center', va='center', fontsize=30)
        ax.set_aspect('equal')

    fig, ax = plt.subplots(figsize=(3,3))

    def update(i):
        draw_state(ax, path[i])
        step = i
        title = f'Step {step}'
        if i > 0 and moves:
            title += f' - move: {moves[i-1]}'
        ax.set_title(title)
        return ax,

    anim = FuncAnimation(fig, update, frames=len(path), interval=interval, blit=False)
    writer = PillowWriter(fps=max(1, int(1000/interval)))
    anim.save(save_file, writer=writer)
    plt.close(fig)

def main():
    batdau, ketthuc = read_input(FI)
    print('batdau:')
    print_board(batdau)
    print('ketthuc:')
    print_board(ketthuc)

    path, moves = a_star(batdau, ketthuc)
    if path is None:
        print('Không có lời giải ')
        return
    print(f'Solution length: {len(path)-1} moves')
    if Inbuoc:
        for i, state in enumerate(path):
            print(f'Step {i}:')
            print_board(state)
            if i > 0:
                print(f'  move: {moves[i-1]}')

    if Taogif:
        try:
            animate_solution(path, moves, save_file='solution.gif', interval=700)
            print('Animation saved to solution.gif')
        except Exception as e:
            print(f'Animation failed: {e}')

if __name__ == '__main__':
    main()
