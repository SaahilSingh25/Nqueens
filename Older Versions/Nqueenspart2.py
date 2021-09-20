#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:19:39 2020

@author: Saahil
"""
import time

global cnt
global glist
cnt = -1
size = 26
glist = [0]*(size+1)

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
        if len(state) == size:
            return state
    var = cnt+1
    for val in get_sorted_values2(state,var):
        new_state = state
        new_state[var] = val
        result = csp_backtracking(new_state,var)
        if result is not None:
            return result
    return None

# def get_next_unassigned_var(state, cnt):
#     cnt = cnt+1
#     return cnt

def get_sorted_values(state, var):
    unav = list()
    vals = list()
    
    if var == 0:
       for x in range(size):
           vals.append(x)
    for x in range(var):
        unav.append(state[x])
        for y in range(size):
            row1=x
            row2=var
            col1=state[x]
            col2=y
            if abs(row2-row1) == abs(col2-col1):
                unav.append(y)
            if y in unav and y in vals:
                vals.remove(y)
            if y not in unav and y not in vals:
                vals.append(y)
    fin = [None for x in range(size)]
    
    # for x in range(len(vals)//2,0,-1):
    #     fin[x] = vals[x]
    # for x in range(len(vals)//2,len(vals)):
    #     fin[x] = vals[x]
        
    return vals

def get_sorted_values2(state, var):
    unav = set()
    vals = set()
    
    if var == 0:
       for x in range(size):
           vals.add(x)
    for x in range(var):
        unav.add(state[x])
        for y in range(size):
            row1=x
            row2=var
            col1=state[x]
            col2=y
            if abs(row2-row1) == abs(col2-col1):
                unav.add(y)
            if y in unav and y in vals:
                vals.remove(y)
            if y not in unav:
                vals.add(y)
    fin = [None for x in range(size)]
    
    # for x in range(len(vals)//2,0,-1):
    #     fin[x] = vals[x]
    # for x in range(len(vals)//2,len(vals)):
    #     fin[x] = vals[x]
        
    return vals
            
ting = [None for x in range(size)]
# start = time.perf_counter()
# temp = csp_backtracking(ting,cnt)
# end = time.perf_counter()
# print(end-start)
# if(test_solution(temp)):
#     print(temp)
# else:
#     print("Not a valid solution")

start = time.perf_counter()
temp = csp_backtracking(ting,cnt)
end = time.perf_counter()
print(end-start)
if(test_solution(temp)):
    print(temp)
else:
    print("Not a valid solution")
