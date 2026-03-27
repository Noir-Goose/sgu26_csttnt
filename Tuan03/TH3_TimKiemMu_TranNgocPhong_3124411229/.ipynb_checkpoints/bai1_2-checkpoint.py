from collections import deque
FI = "maze.inp"
def docfile():
    maze = []
    try:
        with open(FI, "r") as file:
            for line in file:
                maze.append(line.split())
    except FileNotFoundError:
        print(f'Ko thay file {FI}')
    return maze

def tim_vi_tri(maze, ky_tu):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == ky_tu:
                return (i, j)
    return None
def bfs (maze , batdau , dich ):
    chuoi, dinh = len(maze), len(maze[0])
    queue = deque([batdau])
    dinhdatoi = {batdau: None}
    action = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, Xuống, Trái, Phải
    while queue :
        x,y = queue.popleft()
        if (x,y) == dich :
            return tao_duong(dinhdatoi, dich)
        for dx ,dy  in action:
            nx, ny = x + dx, y + dy # di chuyen l x t p
            if 0 <= nx < chuoi and 0 <= ny < dinh: # stop out maze
                if maze[nx][ny] != "#" and (nx, ny) not in dinhdatoi:
                    dinhdatoi[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
    return None

def tao_duong(dinhdatoi, dich):
    duongdi = []
    cur = dich
    while cur is not None:
        duongdi.append(cur)
        cur = dinhdatoi[cur]
    return duongdi[::-1]
maze = docfile()
batdau = tim_vi_tri(maze, "S")
dich = tim_vi_tri(maze, "A")

duongdi = bfs (maze , batdau , dich )

if duongdi:
    print("Đường đi:")
    for p in duongdi:
        print(p)
else:
    print("Không tìm thấy đường đi!")