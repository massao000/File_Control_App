import os

def disassembly(name):
    name_extension = os.path.basename(name)
    name_extension_list = os.path.splitext(name_extension)
    directory = os.path.dirname(name)
    return name_extension, name_extension_list, directory

def files_rename(values, new_name, pattern, padding_list):
    absolute_path_lists = values.split(";")

    if pattern == padding_list[0]: # 01xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers:02}{new_name}{name_extension_list[1]}')
    elif pattern == padding_list[1]: # 01_xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers:02}_{new_name}{name_extension_list[1]}')
    elif pattern == padding_list[2]: # xxx01.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{new_name}{numbers:02}{name_extension_list[1]}')
    elif pattern == padding_list[3]: # xxx_01.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{new_name}_{numbers:02}{name_extension_list[1]}')
    elif pattern == padding_list[4]: # 1xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers}{new_name}{name_extension_list[1]}')
    elif pattern == padding_list[5]: # 1_xxx.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{numbers}_{new_name}{name_extension_list[1]}')
    elif pattern == padding_list[6]: # xxx1.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{new_name}{numbers}{name_extension_list[1]}')
    elif pattern == padding_list[7]: # xxx_1.yyy
        for numbers, absolute_path in enumerate(absolute_path_lists, 1):
            name_extension, name_extension_list, directory = disassembly(absolute_path)
            os.rename(f'{directory}/{name_extension}', f'{directory}/{new_name}_{numbers}{name_extension_list[1]}')
        
        # print(f"ディレクト名　　　　　{os.path.dirname(absolute_path)}")
        # print(f"ファイル名.拡張子　　 {name_extension}")
        # print(f"ファイル名.拡張子分割 {os.path.splitext(name_extension)}")
        # print(f"親ディレクトリ　　　　{os.path.splitdrive(absolute_path)}")
        # print(f"ペア　　　　　　　　　{os.path.split(absolute_path)}")
        # print(f"拡張子　　　　　　　　{os.path.splitext(absolute_path)}")
        # print("-" * 20)

def file_rename(values, new_name):

    name_extension, name_extension_list, directory = disassembly("".join(values))
    os.rename(f'{directory}/{name_extension}', f'{directory}/{new_name}{name_extension_list[1]}')
    # print(f"ディレクト名　　　　　{os.path.dirname(absolute_path)}")
    # print(f"ファイル名.拡張子　　 {x}")
    # print(f"ファイル名.拡張子分割 {os.path.splitext(x)}")
    # print(f"親ディレクトリ　　　　{os.path.splitdrive(absolute_path)}")
    # print(f"ペア　　　　　　　　　{os.path.split(absolute_path)}")
    # print(f"拡張子　　　　　　　　{os.path.splitext(absolute_path)}")
    # print("-" * 20)

def ex_change(values, ex):
    absolute_path_lists = ("".join(values))
    name_extension, name_extension_list, directory = disassembly(absolute_path_lists)
    os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}.{ex}')

def ex_changes(values, ex):
    absolute_path_lists = values.split(";")
    for absolute_path in absolute_path_lists:
        name_extension, name_extension_list, directory = disassembly(absolute_path)
        os.rename(f'{directory}/{name_extension}', f'{directory}/{name_extension_list[0]}.{ex}')
    