import re
import os

def file_type(values, keyName, cboxtf):
    for i in values:
        if cboxtf == False:
            if i[1] == True and re.search(f'{keyName}0', str(i[0])):
                return "1xxx.yyy"
            elif i[1] == True and re.search(f'{keyName}1', str(i[0])):
                return "1_xxx.yyy"
            elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
                return "xxx1.yyy"
            elif i[1] == True and re.search(f'{keyName}3', str(i[0])):
                return "xxx_1.yyy"
        else:
            if cboxtf == True:
                if i[1] == True and re.search(f'{keyName}0', str(i[0])):
                    return "01xxx.yyy"
                elif i[1] == True and re.search(f'{keyName}1', str(i[0])):
                    return "01_xxx.yyy"
                elif i[1] == True and re.search(f'{keyName}2', str(i[0])):
                    return "xxx01.yyy"
                elif i[1] == True and re.search(f'{keyName}3', str(i[0])):
                    return "xxx_01.yyy"


def file_numbers(file_pas, number, pattern, file_name, ex, padding_list):

    if pattern == padding_list[0]: # 01xxx.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{numbers:02}{file_name}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[1]: # 01_xxx.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{numbers:02}_{file_name}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[2]: # xxx01.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{file_name}{numbers:02}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[3]: # xxx_01.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{file_name}_{numbers:02}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[4]: # 1xxx.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{numbers}{file_name}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[5]: # 1_xxx.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{numbers}_{file_name}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[6]: # xxx1.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{file_name}{numbers}.{ex}', 'w', encoding='UTF-8') as f:
                pass
    elif pattern == padding_list[7]: # xxx_1.yyy
        for numbers, i in enumerate(range(number), 1):
            with open(f'{file_pas}\\{file_name}_{numbers}.{ex}', 'w', encoding='UTF-8') as f:
                pass

# def rename_file():
#     pass