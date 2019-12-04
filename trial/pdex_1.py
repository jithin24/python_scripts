# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:41:46 2019

@author: 583435
Pandas trial tutorials
"""

'''
Important Commands
'''
def display(data):
    print(data['asset_nbr'] + " - " + data['asset_stats'] + 
         " - " , data['warrnty_end_dt'], " - " + data['srv_regn_full'])  

import pandas as pd
try:
    df = pd.read_csv("train_service.csv", parse_dates=["install_dt", "warrnty_start_dt", "warrnty_end_dt", "warrnty_end_mnth"])
except:
    execute=False
    print('Read CSV was unsuccessful')
else:
    execute=True
    pass
if(execute):    
    grp = df.groupby('custmr_catgry_full')
    for customer, cust_df in grp:
        print("Customer Name: " + customer)
        
        df_grp_status = cust_df.groupby(['asset_stats','warrnty_flg'])['asset_nbr'].nunique()
        #print(df_grp_status)
        
        df_grp_warranty = cust_df.groupby('warrnty_flg')['asset_nbr'].nunique()
        #print(df_grp_warranty)
        
        if(customer == 'CUSTMR_CATGRY6'):
            for index, row in cust_df.iterrows():
                if(row['warrnty_flg'].upper()=='N' and 
                   row['contract_flag'].upper()=='N'):
                    pass
                    #display(row)
                elif(row['warrnty_flg'].upper()=='Y' and 
                     row['contract_flag'].upper()=='N'):
                    pass
                    display(row)
                elif(row['warrnty_flg'].upper()=='N' and 
                     row['contract_flag'].upper()=='Y'):
                    pass
                    #display(row)
                elif(row['warrnty_flg'].upper()=='Y' and 
                     row['contract_flag'].upper()=='Y'):
                    pass
                    #display(row)
                else:
                    #Asset in Warranty and service not required
                    pass
                    #print("Caught" + row['warrnty_end_dt'])
            break
        else:
            pass
else:
    pass