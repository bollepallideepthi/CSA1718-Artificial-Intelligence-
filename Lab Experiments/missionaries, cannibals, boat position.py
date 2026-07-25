from collections import deque

def is_safe(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False
    return True

def solve():
    start = (3, 3, 'left') 
    goal = (0, 0, 'right')
    queue = deque()
    queue.append([start])
    visited = set([start])

    while queue:
        path = queue.popleft()
        m_left, c_left, boat = path[-1]

        if (m_left, c_left, boat) == goal:
            return path

        
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    if boat == 'left':
                        new_state = (m_left - m, c_left - c, 'right')
                    else:
                        new_state = (m_left + m, c_left + c, 'left')

                    if is_safe(new_state[0], new_state[1]) and new_state not in visited:
                        visited.add(new_state)
                        queue.append(path + [new_state])

def print_path(path):
    for i, (m, c, b) in enumerate(path):
        print(f"Step {i}: Left - M:{m} C:{c} | Right - M:{3 - m} C:{3 - c} | Boat on {b}")

solution = solve()
if solution:
    print_path(solution)
else:
    print("No solution found.")