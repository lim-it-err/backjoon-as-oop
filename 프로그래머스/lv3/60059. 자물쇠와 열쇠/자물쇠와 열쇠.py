def rot(key):
    def rot90(key):
        return [[key[j][i] for j in range(len(key))] for i in range(len(key[0])-1,-1,-1)]
    return [rot90(key),rot90(rot90(key)), rot90(rot90(rot90(key))), rot90(rot90(rot90(rot90(key))))]


def solution(key, lock):
    keys = rot(key)
    N, M = len(key), len(lock)
    for rotated_key in keys:
        for x in range(-(N - 1), M):
            for y in range(-(N - 1), M):
                temp_lock = [row[:] for row in lock]
                is_valid = True
                
                try:
                    for i in range(N):
                        for j in range(N):
                            if 0 <= i + x < M and 0 <= j + y < M:
                                temp_lock[i + x][j + y] += rotated_key[i][j]
                            
                    for row in temp_lock:
                        if 0 in row:
                            is_valid = False
                            break
                        if 2 in row:
                            is_valid = False
                            break
                    if is_valid:
                        return True
                
                except IndexError:
                    pass

    return False