
import pathlib

def total_salary(path):
    #додаю блок try /except
    try:
        #відкриваю файл з with
        with open(path, "r", encoding='UTF-8') as data:
         my_dict={}
         for l in data.readlines():
             key,value = l.split(',')
             my_dict.update({key:value.strip()})
                
        t=sum([int(v) for v in my_dict.values()]) 
        av=t//len(my_dict)
        return t, av
    except Exception as e:
        return f"Something is worng with {data}"
    
    
total, average = total_salary("/Users/mruda/Desktop/repos/goit-pycore-hw-04/ex_1/data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
        
        

   
   
 
 
 
