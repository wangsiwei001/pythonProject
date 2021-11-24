#!/usr/bin/python
# -*- coding: UTF-8 -*-
def fo(list, name):
    for ind, v in enumerate(list):
        if v == name:
            return ind
    else:
        return None


nameList = ["王思伟", "张叨叨", "王思敏", "张峰峰", "王旭志", "王建平"]

c = fo(nameList, "王思敏")
print(c)


def selectSum(list, var):
    head = 0
    end = len(list)
    while head <= end:
        mid = (head + end) // 2
        if list[mid] == var:
            return mid
        elif list[mid] > var:
            end = mid - 1
        else:
            head = mid + 1
    else:
        return None


sumList = [1, 2, 3, 4, 5, 7, 8, 10, 13, 16, 18, 19]

resulete = selectSum(sumList, 2)
print(resulete)
