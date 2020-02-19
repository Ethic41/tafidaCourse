#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-07 19:43:55
# @Author  : Dahir Muhammad Dahir

# this text could be arbitrary length
text = "abc"

"""what we need is a function that
takes as argument any text and loop arbitrary
number of times instead of nesting loops 
as below :)"""

def generate():
    for x in text:
        for y in text:
            for z in text:
                # simple f-string
                print(f"{x}{y}{z}")

#generate()












def basic():
    for items in text:
        for itemz in text:
            print(f"{items}{itemz}")

text = "abc"
def gen():
    for items in text:
        for itemz in text:
            for itemx in text:
                (yield f"{items}{itemz}{itemx}")

"""for i in gen():
    print(i)

print("Done!")"""

def rotate(target, count, texts, load=""):
    for text in texts:
        if count == target:
            print(load+text)

        if count != target:
            rotate(target, count+1, texts, load=load+text)
# example of 
rotate(4, 1, "abcdefghijklmnop")