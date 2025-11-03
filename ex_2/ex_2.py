#
import pathlib

def get_cats_info(path):
    
    try:
        #відкриваю файл з with
        with open(path, "r", encoding='UTF-8') as data:
            result=[]
            lines=data.readlines()
            if not lines:
                raise ValueError("File is empty")
            
            for line in lines:
                 values = line.split(',')
                 if len(values) != 3:
                    raise ValueError("Wrong format")
                 my_dict={"id":values[0], "name":values[1], "age":values[2].strip()}
                 result.append(my_dict)
            return result
    except FileNotFoundError:
        return f"🔦 Could not find {data}"
    except ValueError as e:
        return f" 🔧 {e}"
    except Exception as e:
        return f" Unexpected error {e}"
    
cats_info=get_cats_info("/Users/mruda/Desktop/repos/goit-pycore-hw-04/ex_2/data.txt")
if isinstance(cats_info,str):
    print(cats_info)
else:
    for item in cats_info:
        print(item)
    