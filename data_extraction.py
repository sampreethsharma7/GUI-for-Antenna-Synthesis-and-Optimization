# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:54:14 2021

@author: sinf5
"""
import os as o
import pandas as pd
import data_version2 as d



df = pd.DataFrame()
df_frq = pd.DataFrame()
df_s11 = pd.DataFrame()
df_gain = pd.DataFrame()
df_gain1 = pd.DataFrame()   
mode = 0o666

def listfiles(path):
    filenames = o.listdir(path)
    directory = "Data"
    sub_directory ="Training_Data"
    result_path = o.path.join(path, directory)
    result_sub_path = o.path.join(path, sub_directory)
    o.mkdir(result_path, mode)
    o.mkdir(result_sub_path, mode)
    val=1
    for filename in filenames:
        df = d.getdata(o.path.abspath(o.path.join(path,filename)))
        df.to_excel(path+'/'+directory+'/'+filename.split(".")[0]+ '.xlsx', index=False)
        df_frq.insert(loc  = val-1, column = 'Frequency_'+filename,value = df['Frequency'])
        df_s11.insert(loc  = val-1, column = 'S11_'+filename,value = df['S11'])
        df_gain.insert(loc  = val-1, column = 'Gain_'+filename,value = df['Gain'])
        df_gain1.insert(loc  = val-1, column = 'Gain1_'+filename,value = df['Gain1'])
        val = val + 1
    df_frq.to_excel(path+'/'+sub_directory+'/'+'Frequency'+ '.xlsx', index=False)
    df_s11.to_excel(path+'/'+sub_directory+'/'+'S11'+ '.xlsx', index=False)
    df_gain.to_excel(path+'/'+sub_directory+'/'+'Gain'+ '.xlsx', index=False)
    df_gain1.to_excel(path+'/'+sub_directory+'/'+'Gain1'+ '.xlsx', index=False)
    
   

