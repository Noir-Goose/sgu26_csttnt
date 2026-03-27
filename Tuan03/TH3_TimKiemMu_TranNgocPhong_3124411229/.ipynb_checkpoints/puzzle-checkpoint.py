FI = "puzzle.inp"

class State:
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Lên, Xuống, Trái, Phải

    def __init__(self, key, parent=None, cost=0):
        self.key = tuple(tuple(row) for row in key)
        self.pos0 = self.find0(self.key)
        self.parent = parent
        self.cost = cost

    @staticmethod
    def find0(key):
        for i in range(3):
            for j in range(3):
                if key[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    def tokey(self):
        return self.key

    def expand(self):
        d, c = self.pos0
        for dr, dc in State.actions:
            dn, cn = d + dr, c + dc
            if 0 <= dn < 3 and 0 <= cn < 3:
                new_key = [list(row) for row in self.key]
                new_key[d][c], new_key[dn][cn] = new_key[dn][cn], new_key[d][c]
                yield new_key

    def pprint(self, title=''):
        if title:
            print(f'---------- {title} ----------')
        for row in self.key:
            print(" ".join(map(str, row)))
        print()

def bfs(skey, gkey):
    frontier = [tuple(tuple(row) for row in skey)]
    target_key = tuple(tuple(row) for row in gkey)
    
    start_node = State(skey)
    states = {start_node.tokey(): start_node}

    while frontier:
        cur_key = frontier.pop(0)
        cur_node = states[cur_key]

        if cur_key == target_key: # check cái goal
            return states, cur_key

        for child_key_list in cur_node.expand():
            child_key = tuple(tuple(row) for row in child_key_list)#di chuyển ổn = tạo 1 mặt puzzle mới
            
            if child_key not in states: # ktra thk con đã tồn tại trước đó chưa 
                child_node = State(child_key_list, parent=cur_node, cost=cur_node.cost + 1) 
                states[child_key] = child_node
                frontier.append(child_key)
                
    return states, None

def test2():
    try:
        with open(FI, "rt") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        start = [[int(v) for v in lines[i].split()] for i in range(3)]
        goal = [[int(v) for v in lines[i].split()] for i in range(3, 6)]
        
    except FileNotFoundError:
        print(f"Không tìm thấy file {FI}")
        return
        
    all_states, final_key = bfs(start, goal)
    if final_key: # vẽ lại đường đi
        path = []
        curr = all_states[final_key]
        while curr:
            path.append(curr)
            curr = curr.parent
        
        print(f"Tìm thấy lời giải sau {len(path)-1} bước:")
        # In ngược lại từ Start đến Goal
        for i, node in enumerate(reversed(path)):
            node.pprint(f"Bước {i}")
    else:
        print("Không tìm thấy lời giải!")

if __name__ == "__main__":
    test2()