FI = "dothi.inp"

def docfile():
    dothi = {}
    try:
        with open(FI, "r") as file:
            for line in file:
                part = line.split()
                if part:
                    dothi[part[0]] = part[1:]
    except Khongthayfile:
        print(f'Khong thay file {FI}')
    return dothi

def bfs(dothi, batdau, dich):
    queue = [batdau]
    danhdau = {batdau: None} 
    while queue:
        current = queue.pop(0)
        if current == dich: # = if see dich
            return taoj_duong(danhdau, dich)
        for dinhke in dothi.get(current, []):
            if dinhke not in danhdau:
                danhdau[dinhke] = current
                queue.append(dinhke)              
    return None 

def taoj_duong(danhdau, dich):
    path = []
    curr = dich
    while curr is not None:
        path.append(curr)
        curr = danhdau[curr]
    return path[::-1] # Dao nguoc duong di 
dothi = docfile()
batdau, dich = 'A', 'D'
path = bfs(dothi, batdau, dich)
if path:
    print(f"Duong di tu {batdau} den {dich}: {' -> '.join(path)}")
else:
    print("Khong tim thay duong di!")