#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:19:39 2020

@author: Saahil
"""
import sys

global cnt
global glist
global ans
global isfound
ans = 0
cnt = -1
size = 28
glist = [0]*(size+1)

isfound = False


def test_solution(state):
    for var in range(1,size+1):
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

def csp_backtracking(cur_row):
    for col in range(size):
        if isValid(cur_row, col):
            glist[cur_row]=col
            if cur_row == size - 1:
                #ans=0
                print(glist)
                #cnt = 1
                #break
                sys.exit()
                return True
            else:
                if csp_backtracking(cur_row+1):
                    return True
    return False
    
def isValid(row, col):
    
    for x in range(row):
        if (glist[x] == col) or (abs(glist[x]-col) == abs(x-row)):
            return False
    return True
    # if None not in state:
    #     if test_solution(state):
    #         return state
    # for val in get_sorted_values(state,var):
    #     new_state = state
    #     new_state[var] = val
    #     result = csp_backtracking(new_state,var)
    #     if result is not None:
    #         return result
    # return None


            
# ting = [None for x in range(size)]
print(csp_backtracking(0))