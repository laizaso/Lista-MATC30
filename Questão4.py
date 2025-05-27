MOD = 10**9 + 7

def countRecognizedStrings(R, L):
    from collections import defaultdict, deque
    
    class State:
        def __init__(self):
            self.trans = defaultdict(int)
            self.eps = set()
    
    def build_nfa(exp):
        stack = []
        state_count = 0
        start = State()
        end = State()
        state_count += 2
        stack.append((start, end))
        
        i = 0
        while i < len(exp):
            c = exp[i]
            if c == '(':
                stack.append(('(', None))
                i += 1
            elif c == ')':
                parts = []
                while stack[-1][0] != '(':
                    parts.append(stack.pop())
                stack.pop()
                
                if i+1 < len(exp) and exp[i+1] == '*':
                    s1, e1 = parts[0]
                    new_start = State()
                    new_end = State()
                    state_count += 2
                    
                    new_start.eps.add(s1)
                    new_start.eps.add(new_end)
                    e1.eps.add(s1)
                    e1.eps.add(new_end)
                    
                    stack.append((new_start, new_end))
                    i += 2
                elif len(parts) > 1 and parts[-1][0] == '|':
                    s2, e2 = parts[-2]
                    s1, e1 = parts[-4]
                    new_start = State()
                    new_end = State()
                    state_count += 2
                    
                    new_start.eps.add(s1)
                    new_start.eps.add(s2)
                    e1.eps.add(new_end)
                    e2.eps.add(new_end)
                    
                    stack.append((new_start, new_end))
                    i += 1
                else:
                    current_s, current_e = parts.pop()
                    while parts:
                        s, e = parts.pop()
                        e.eps.add(current_s)
                        current_s = s
                    stack.append((current_s, current_e))
                    i += 1
            elif c in ['a', 'b']:
                s = State()
                e = State()
                state_count += 2
                s.trans[c] = e
                stack.append((s, e))
                i += 1
            else:
                i += 1
        
        while len(stack) > 1:
            s2, e2 = stack.pop()
            s1, e1 = stack.pop()
            e1.eps.add(s2)
            stack.append((s1, e2))
        
        return stack[0][0], stack[0][1]
    
    start_state, end_state = build_nfa(R)
    
    state_id = {}
    id_counter = 0
    
    initial_states = set()
    stack = [start_state]
    while stack:
        s = stack.pop()
        if s not in initial_states:
            initial_states.add(s)
            for eps_s in s.eps:
                stack.append(eps_s)
    
    state_id[frozenset(initial_states)] = id_counter
    id_counter += 1
    
    dfa_trans = [{} for _ in range(1000)]
    
    queue = deque()
    queue.append(initial_states)
    
    while queue:
        current_states = queue.popleft()
        current_id = state_id[frozenset(current_states)]
        
        for symbol in ['a', 'b']:
            next_states = set()
            for s in current_states:
                if symbol in s.trans:
                    next_s = s.trans[symbol]
                    stack = [next_s]
                    visited = set()
                    while stack:
                        ns = stack.pop()
                        if ns not in next_states:
                            next_states.add(ns)
                            for eps_ns in ns.eps:
                                if eps_ns not in next_states:
                                    stack.append(eps_ns)
            
            if not next_states:
                continue
            
            fs = frozenset(next_states)
            if fs not in state_id:
                state_id[fs] = id_counter
                id_counter += 1
                queue.append(next_states)
            
            dfa_trans[current_id][symbol] = state_id[fs]
    
    size = id_counter
    trans_matrix = [[0]*size for _ in range(size)]
    for i in range(size):
        for symbol in ['a', 'b']:
            if symbol in dfa_trans[i]:
                j = dfa_trans[i][symbol]
                trans_matrix[i][j] += 1
    
    final_states = set()
    for states in state_id:
        if end_state in states:
            final_states.add(state_id[states])
    
    def matrix_mult(a, b):
        res = [[0]*size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if a[i][k]:
                    for j in range(size):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
        return res
    
    def matrix_pow(mat, power):
        result = [[0]*size for _ in range(size)]
        for i in range(size):
            result[i][i] = 1
        
        while power > 0:
            if power % 2 == 1:
                result = matrix_mult(result, mat)
            mat = matrix_mult(mat, mat)
            power //= 2
        return result
    
    mat = matrix_pow(trans_matrix, L)
    
    initial_id = state_id[frozenset(initial_states)]
    total = 0
    for final_id in final_states:
        total = (total + mat[initial_id][final_id]) % MOD
    
    return total

def main():
    # Casos de teste incorporados diretamente no código
    test_cases = [
        ("((ab)|(ba))", 2),
        ("((a|b)*)", 5),
        ("((a*)(b(a*)))", 100)
    ]
    
    for R, L in test_cases:
        print(L)
        resultado = countRecognizedStrings(R, L)
        print()

if __name__ == '__main__':
    main()