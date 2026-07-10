from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_next_states(state):
    next_states = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            next_states.append(tuple(new_state))
    return next_states

def bfs(start):
    q = deque([(start, [])])
    visited = {start}
    while q:
        state, path = q.popleft()
        if state == GOAL:
            return path + [state]
        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, path + [state]))

start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)


solution = bfs(start_state)

print("Steps to Solve the 8-Puzzle:")
for step in solution:
    print_board(step)
