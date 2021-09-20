#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:24:27 2020

@author: Saahil
"""
import random
import time

global cnt
cnt = -1
size = 31
def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
        return True

def csp_backtracking(state,cnt):
    if None not in state:
        if test_solution(state):
            return state
    var = get_next_unassigned_var(state,cnt)
    for val in get_sorted_values(state,var):
        new_state = state
        new_state[var] = val
        result = csp_backtracking(new_state,var)
        if result is not None:
            return result
    return None

def get_next_unassigned_var(state, cnt):
    cnt = cnt+1
    return cnt

def get_sorted_values(state, var):
    unav = []
    vals = []
    for x in range(var):
        unav.append(state[x])
        for y in range(size):
            row1=x
            row2=var
            col1=state[x]
            col2=y
            if abs(row2-row1) == abs(col2-col1):
                unav.append(y)
    for x in range(size):
        if x not in unav:
            vals.append(x)
            random.shuffle(vals)
    return vals

def find_conflicts(state, var):
    unav = 0
    for x in range(len(state)):
        if x != var:
            row1=x
            row2=var
            col1=state[x]
            col2=state[var]
            if abs(row2-row1) == abs(col2-col1):
                unav+=1
    if state.count(state[var]) > 1:
        unav += (state.count(state[var])-1)
    return unav

def find_largest_conflict(board,total):
    cons = [] 
    tie = []
    fin = 0
    for x in range(len(board)):
        temp = find_conflicts(board, x)
        cons.append(temp)
    m = max(cons)
    total = sum(cons)
    if cons.count(0) == size:
        return None
    elif cons.count(m) > 1:
        for x in cons:
            if x == m:
                tie.append(cons.index(x))
                cons[cons.index(x)] = None
        fin = random.choice(tie)
        return (fin,total)
    return (cons.index(m),total)

def find_smallest_conflict(board,row):
    cons = [] 
    tie = []
    fin = 0
    for x in range(len(board)):
        board[row] = x
        temp = find_conflicts(board, row)
        cons.append(temp)
    m = min(cons)
    if cons.count(m) > 1:
        for x in cons:
            if x == m:
                tie.append(cons.index(x))
                cons[cons.index(x)] = None
        fin = random.choice(tie)
        return fin
    return cons.index(m)

def make_flawed_state(size):
    used = set()
    board = [None for x in range(size)]
    unused = []
    count = 0
    while None in board:
        vals = get_sorted_values(board, count)
        if len(vals) < 1:
            for x in range(size):
                if x not in used:
                    unused.append(x)
            while None in board:
                ran = random.choice(unused)
                if ran not in board:
                    board[count] = random.choice(unused)
                    count+=1
        else:
            ran = random.choice(vals)
            if ran not in used:
                board[count] = ran
                count+=1
            used.add(ran)
    return board
        
def incr_repair(state,total):
    while find_largest_conflict(state,total) != None:
        row = find_largest_conflict(state, total)
        new = find_smallest_conflict(state, row[0])
        state[row[0]]=new
        print(row[1])
        print(state)
    print("0")
    return state

print("Backtracking:")
init = [None for x in range(size)]
start = time.perf_counter()
temp = csp_backtracking(init,cnt)
if test_solution(temp):
    print(temp)
else:
    print("Not a valid solution")
    
size = 32
cnt = -1
init = [None for x in range(size)]
temp = csp_backtracking(init, cnt)
if test_solution(temp):
    print(temp)
else:
    print("Not a valid solution")
print()

print("Incremental Repair:")
size = 31
total = 0
board = make_flawed_state(size)
print("Initial:" + str(board))
temp = (incr_repair(board,total))
if test_solution(temp):
    print("Final: " + str(temp))
else:
    print("Not a valid solution")
    
print()
size = 32
total = 0
board = make_flawed_state(size)
print("Initial:" + str(board))
temp = (incr_repair(board,total))
if test_solution(temp):
    print("Final: " + str(temp))
else:
    print("Not a valid solution")

end = time.perf_counter()
print(end-start)

