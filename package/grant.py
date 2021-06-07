from package.file_rename import *
import os




def files_grant(values, pattern, padding_list):
    absolute_path_lists = values.split(";")

    if pattern == padding_list[0]: # 01xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers:02}{name_extension_list[0]}{name_extension_list[1]}')
    elif pattern == padding_list[1]: # 01_xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers:02}_{name_extension_list[0]}{name_extension_list[1]}')
    elif pattern == padding_list[2]: # xxx01.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}{numbers:02}{name_extension_list[1]}')
    elif pattern == padding_list[3]: # xxx_01.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}_{numbers:02}{name_extension_list[1]}')
    elif pattern == padding_list[4]: # 1xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers}{name_extension_list[0]}{name_extension_list[1]}')
    elif pattern == padding_list[5]: # 1_xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers}_{name_extension_list[0]}{name_extension_list[1]}')
    elif pattern == padding_list[6]: # xxx1.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}{numbers}{name_extension_list[1]}')
    elif pattern == padding_list[7]: # xxx_1.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}_{numbers}{name_extension_list[1]}')