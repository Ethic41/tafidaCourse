#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-10 22:21:00
# @Author  : Dahir Muhammad Dahir

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

#for i in range(10):
#    print(fibonacci(i))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# print(factorial(3))

def fun1():
    fun1()

fun1()