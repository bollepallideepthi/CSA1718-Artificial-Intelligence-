import itertools

def solve_cryptarithmetic():
    letters = 'S E N D M O R Y'.split()
    
    for perm in itertools.permutations('0123456789', len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue

        SEND  = int(mapping['S'] + mapping['E'] + mapping['N'] + mapping['D'])
        MORE  = int(mapping['M'] + mapping['O'] + mapping['R'] + mapping['E'])
        MONEY = int(mapping['M'] + mapping['O'] + mapping['N'] + mapping['E'] + mapping['Y'])

        if SEND + MORE == MONEY:
            return mapping, SEND, MORE, MONEY
    return None

res = solve_cryptarithmetic()
if res:
    mapping, SEND, MORE, MONEY = res
    print("Solution found:")
    for k in sorted(mapping):
        print(f" {k} = {mapping[k]}")
    print()
    print(f" {SEND} + {MORE} = {MONEY}")
else:
    print("No solution found.")
