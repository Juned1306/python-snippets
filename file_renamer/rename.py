import os

os.chdir('D:\\Python\\File Operation\\Renaming Mult Filles')


for f in os.listdir():
    #print(f)
    
    f_name,f_extention=os.path.splitext(f)
    f_title,f_desc,f_num=f_name.split('-')
    f_title=f_title.strip()
    f_desc=f_desc.strip()
    f_num=f_num.strip()[1:].zfill(2)
    print(f_num,f_title,f_desc)
    print('------------------------------')
    new_name=f"{f_num}-{f_title}-{f_desc}{f_extention}"
    print(new_name)
    print('------------------------------')
    os.rename(f,new_name)
    
    
    
    

    
