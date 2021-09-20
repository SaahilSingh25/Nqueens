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
size = 8

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
    # print(state)
    # print(var)
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
    # print(unav)
    # print()
    return vals
            
ting = [None for x in range(size)]
start = time.perf_counter()
temp = csp_backtracking(ting,cnt)
end = time.perf_counter()
print(end-start)
if test_solution(temp):
    print(temp)
else:
    print("Not a valid board")

