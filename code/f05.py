import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import preprocessing

'''
considering a linear demand and supply curve
'''


def cobweb(a0: float, b0: float, a1: float, b1: float, x0: float, t: float, p0: float = 0):
    '''
    given variables
    a0: intercept of the demand curve(+ve)
    b0: slope of the demand curve(-ve)
    a1: intercept of the supply curve(-ve)
    b1: slope of the supply curve(+ve)
    t: period
    x0: period0 price

    generated variables
    x1: period1 price
    pp: intertemporal eqm price
    time_path: time path
    dd: eqm demand
    ss: eqm supply
    in eqm condition dd and ss should and would be the same
    '''

    x1 = ((a1 - a0) + (b1 * x0))/b0
    dd = a0 + b0 * x1
    ss = a1 + b1 * x0
    pp = -((a0 - a1) / (b0 - b1))
    time_path = ((p0 - pp) * (b0 / b1) ** t) + pp
    
    return [x1, pp, dd, ss, time_path]


def loop(loop_limit: int):
    data_storage= []
    loop_counter=-1
    loops= 1
    params= [1]*4
    while loop_counter<= loop_limit:
        for i in range(2):
            if params[i+1]>0:
                params[i+1]*=-1
            if params[i*3]<0:
                params[i*3]*=-1
        loop_counter+=1
        b= params[2]/params[3]
        if b<0:
            b*=-1
        if b>1:
            ratio_exp= 0.95
            b1= params[3]
            err= ratio_exp-b
            n= 100
            for i in range(n):
                b1+=err
                err= ratio_exp-b
                if b< ratio_exp:
                    break
        params[1]= b1
        # calling data generator
        x0= 0
        for i in range(loops):
            data= cobweb(
            a0= params[0], b0= params[1],
            a1= params[2], b1= params[3],
            t= i, x0= x0, p0= x0)
            x0= data[0]
            data_storage.append(data)
