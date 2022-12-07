# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:29:49 2021

@author: sinf5
"""

def getdata(filepath): 
    import numpy as np
    import pandas as pd
    df = pd.DataFrame()
    s11 = []
    frq = []
    gain = []
    directivity =[]
    file = open(filepath)
    check_file = file.readlines()
    word1 = 'FREQ ='
    word2 = ' S     1      1 '
    word3 ='Gain'
    word4 ='0.00    0.00'
    
    for line in check_file:
        if word1 in line:
            frq_value = line.split()[5]
            frq.append(frq_value)
        if word2 in line:
            s11_value = line.split()[6]
            s11.append(s11_value)
        if word3 in line:
            gain_value = line.split()[7]
            gain.append(gain_value)
        if word4 in line:
            directivity_value = line.split()[8]
            directivity.append(directivity_value)
    df['Frequency'] = frq
    df['S11'] = s11
    df['Gain']=gain
    df['Directivity'] = directivity
    sub = []
    for i in range(len(directivity)):
        sub.append(float(directivity[i]) - float(gain[i]))

    df['Gain1'] = sub
    return df

