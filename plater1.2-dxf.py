# -*- coding: utf-8 -*-

import os

def funk(element):
    n=0
    for i, k in enumerate(element,0):
        if k=='_':
            n+=1
            if n==2:
                #print(i,k)
                #print('usunieto nazwe BLACHA: ',element[:i+1])
                file_upgrade = element[i+1:]
    return file_upgrade


os.mkdir('backup')

#searching file in folder with ending: '.dxf'

for filename in os.listdir():

        
    if filename.endswith('.dxf'):
        with open(filename) as f: #Zbus cnc file open
            file = f.read()
            
            
            #backuping            
        filename_backup = filename+'.bak'
        path = os.path.abspath(os.getcwd())
        path+= '\\backup'
        filename_backup_path = 'backup\\'+ filename_backup
       
        #ckecking backup
        if not filename_backup in os.listdir(path):
            with open(filename_backup_path, 'a') as backup:
                file_backup = backup.write(file)
            #ENG version:    
            #print(f'creating backup: {filename_backup} is complete!')

            #PL version:
            print(f'{filename_backup}: utworzono backup!')

  
     #upgradeing 
           
        filename_upgrade = funk(filename)
        path = os.path.abspath(os.getcwd())
        #path+= '\\upgrade'
        filename_upgrade_path = filename_upgrade
       
        #ckecking upgrade
        if not filename_upgrade in os.listdir(path):
            with open(filename_upgrade_path, 'a') as upgrade:
                file_upgrade = upgrade.write(file)
            #ENG version:    
            #print(f'creating upgrade: {filename_upgrade} is complete!')

            #PL version:
            print(f'{filename_upgrade}: utworzono upgrade!')
    
