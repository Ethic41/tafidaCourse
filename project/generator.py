#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-08 00:11:18
# @Author  : Dahir Muhammad Dahir

def generate(target_length: int, charset: str, count=1, output=""):
    for char in charset:
        if count == target_length:
            # yield output+char
            print(output+char)
        
        if count != target_length:
            generate(target_length, charset, count+1, output=f"{output}{char}")

# charset="abcdefghijklmnopqrstuvwxyz"  # sample charset
charset = "ab"
generate(2, charset)

