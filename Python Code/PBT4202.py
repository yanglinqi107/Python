# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 17:22:43 2021

@author: MLZ107
"""

#程序名称：PBT4202.py
#功能：列表应用：有序表合并
#!/usr/bin/python
# -* - conding:UTF-8 -* -

def mergeList(lista,listb):
    n = len(lista)
    m = len(listb)
    listc = lista + listb
    while(n > 0 and m > 0):
        if(lista[n-1] >= listb[m-1]):
            listc[n+m-1] = lista[n-1]
            n = n-1
        else:
            listc[n+m-1] = listb[m-1]
            m = m-1
    #将LB中认为合并到LA中的元素合并到LA
    while(m > 0):
        listc[n+m-1]=listb[m-1]
        m = m-1
    return listc

def main():
    lista = [3,5,8,11]
    listb = [2,6,8,9,11,15,20]
    listc = mergeList(lista,listb)
    print("lista = ",lista)
    print("listb = ",listb)
    print("listc = ",listc)
    
main()