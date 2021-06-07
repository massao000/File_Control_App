from package import *

# sg.theme("DarkGreen7")

def change_color(wind, values):
    wind.update("ON" if values else "OFF")
    if values == True:
        wind.update(text_color="red")
    else:
        wind.update(text_color="#FFFFFF")

def change_text(wind, wind2, wind3, wind4, valies):
    wind.update("01xxx.yyy" if valies else "1xxx.yyy")
    wind2.update("01_xxx.yyy" if valies else "1_xxx.yyy")
    wind3.update("xxx01.yyy" if valies else "xxx1.yyy")
    wind4.update("xxx_01.yyy" if valies else "xxx_1.yyy")

# 1個にできるのでは
def error(value, error_message, popup_error_tital, popup_get_text, popup_tital):
    sg.popup_error(error_message, title=popup_error_tital)
    pop = sg.popup_get_text(popup_get_text, title=popup_tital)
    value.update(pop)



file_creating_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

templates_folder = "templates"

if not os.path.exists(templates_folder):
    os.mkdir(templates_folder)
    template = glob.glob(f"{templates_folder}\*")
else:
    template = glob.glob(f"{templates_folder}\*")

if os.path.exists("customize_ex.txt"):
    with open("customize_ex.txt", "r", encoding="UTF-8") as f:
        x = f.readlines()
    extension_lists = [ i.replace("\n", "") for i in x]
else:
    extension_lists = ['txt', 'sjis', 'dir', 'ico', 'coffee', 'pct', 'dic', 'asx', 'tif', 'abp', 'as', 'cgm', 'pmp', 'tgz', 'sh', 'xpm', 'dib', 'ani', 'wmv', 'uu', 'ts', 'aif', 'fpx', 'rm', 'rpm', 'Z', 'sys', 'mat', 'htm', 'cab', 'h', 'xsl', 'bat', 'pcd', 'ml', 'pas', 'cobol', 'cpp', 'mht', 'pdf', 'erl', 'dvr', 'lhs', 'pro', 'rle', 'wvx', 'mng', 'asp', 'db', 'mid', 'dcr', 'ai', 'php', 'c', 'vrml', 'sql', 'xml', 'ini', 'ras', 'swi', 'lisp', 'pm', 'm', 'url', 'd', 'forth', 'pict', 'ra', 'zip', 'bin', 'asm', 'art', 'clj', 'inf', 'html', 'jpe', 'dwt', 'rv', 'wma', 'chm', 'py', 'jsx', 'tmp', 'log', 'jpg', 'mov', 'pic', 'exe', 'ppd', 'snd', 'eps', 'cdr', 'tcl', 'tga', 'xquery', 'mac', 'rtf', 'asc', 'reg', 'scala', 'wrl', 'ps', 'obj', 'qt', 'mpg', 'mpeg', 'vbs', 'aifc', 'css', 'maki', 'cnf', 'man', 'conf', 'wpg', 'rmm', 'jfif', 'bmp', 'gif', 'asf', 'ttf', 'mag', 'q0', 'swf', 'dxr', 'jxw', 'com', 'nsk', 'jpeg', 'ocx', 'hx', 'lsl', 'sj1', 'j6i', 'rs', 'pcx', 'pnm', 'doc', 'aiff', 'js', 'xbm', 'sit', 'cf', 'cgi', 'pl', 'au', 'cam', 'dll', 'vdo', 'class', 'png', 'fon', 'dart', 'xht', 'dpx', 'smi', 'a', 'bak', 'cs', 'ram', 'cmp', 'avi', 'scr', 'so', 'wmf', 'tar', 'smil', 'cur', 'old', 'org', 'ttc', 'midi', 'mp3', 'hlp', 'shtml', 'wax', 'csv', 'tiff', 'pps', 'xhtml', 'wri', 'jar', 'go', 'v', 'scm', 'xls', 'groovy', 'hs', 'wav', 'lua', 'rb', 'java', 'lzh', 'r', 'ppt', 'gz', 'dat', 'mp4', 'json', 'md']


# 連番ファイルの作成
layout_cereal = [
          [sg.T("連番作成", pad=((200, 0), (10, 10)), font=("", 20))],
          [sg.T("保存場所", pad=(12, 0)), sg.I(k='-INPUT_SAVE_FILR'), sg.FolderBrowse("検索",s=(10, 1), k='-SAVE_FILR')],
          [sg.T("ファイル名"), sg.I('default_name', s=(35, 1), k='-NAME'), sg.Combo(extension_lists, k="-EXTENSION", default_value="拡張子入力または選択", s=(20, 1))],
          [sg.T("ファイル数"), sg.Combo(file_creating_number, k="-FILE_NUMBER", default_value="ファイル数の入力または選択", s=(26, 1))],
          [sg.Frame(layout=[
                [sg.T("ゼロ詰め ON/OFF"), sg.CBox("", k="CBOX", enable_events=True), sg.T("OFF", size=(3,1), k="Check")],
                [sg.Radio('', "Radio", key='-Radio0', default=True), sg.T("1xxx.yyy", k="RADIO_TEXT1", s=(9, 1)), 
                sg.Radio('', "Radio", key='-Radio1'),sg.T("1_xxx.yyy", k="RADIO_TEXT2", s=(9, 1)),  
                sg.Radio('', "Radio", key='-Radio2'), sg.T("xxx1.yyy", k="RADIO_TEXT3", s=(9, 1)), 
                sg.Radio('', "Radio", key='-Radio3'),sg.T("xxx_1.yyy", k="RADIO_TEXT4", s=(9, 1))]
                            ], title="ファイルタイプ")],
          [sg.T("想定されるファイル名▼", pad=((110, 0), (10, 10)), font=("", 20)), sg.B('更新', k='-DISPLAY')],
          [sg.T('', k='-ASSUMPTION', s=(35, 1), font=("", 20))],
          [sg.B("実行", k="CREATES_BUTTON")] 
         ]

# ファイル名変更＆拡張子変更
layout_rename = [
          [sg.T("ファイルリネーム", k="-MODE_TEXT-", pad=((150, 0), (10, 10)), font=("", 20))],
          [sg.B("単一ファイルに変更", k="CHANGE"), sg.CBox("拡張子変更", k="EXTENSION_EDIT", change_submits=True)],
          [sg.T("単一ファイル"), sg.I("書き込み不可", k='-INPUT_RENAME_FILR', disabled_readonly_background_color="gray", disabled=True), sg.FileBrowse("検索",s=(10, 1), k='-RENAME_FILR', disabled=True)],
          [sg.T("複数変更",  pad=(19, 0)), sg.I("書き込み不可", k='-INPUT_RENAME_FILRS', disabled_readonly_background_color="gray", disabled=True), sg.FilesBrowse("検索",s=(10, 1), k='-RENAME_FILRS', disabled=False)],
          [sg.T("ファイル名", pad=(12, 0)), sg.I('', s=(35, 1), k='-CHANGE_NAME', disabled_readonly_background_color="gray", disabled=False), sg.Combo(extension_lists, k="-CHANGE_EXTENSION", default_value="拡張子入力または選択", s=(20, 1), disabled=True)],
          [sg.Frame(layout=[
                [sg.T("ゼロ詰め ON/OFF"), sg.CBox("", k="CBOX2", enable_events=True), sg.T("OFF", size=(3,1), k="Check2")],
                [sg.Radio('', "C_Radio", key='C_Radio0', default=True), sg.T("1xxx.yyy", k="C_RADIO_TEXT1", s=(9, 1)), 
                sg.Radio('', "C_Radio", key='C_Radio1'),sg.T("1_xxx.yyy", k="C_RADIO_TEXT2", s=(9, 1)),  
                sg.Radio('', "C_Radio", key='C_Radio2'), sg.T("xxx1.yyy", k="C_RADIO_TEXT3", s=(9, 1)), 
                sg.Radio('', "C_Radio", key='C_Radio3'),sg.T("xxx_1.yyy", k="C_RADIO_TEXT4", s=(9, 1))]
                            ], title="ファイルタイプ")],
          [sg.B("実行", k="RENAME_BUTTON")]
         ]

# ファイルのに連番の付与
layout_sequence_grant = [
            [sg.T("連番付与", pad=((150, 0), (10, 10)), font=("", 20))],
            [sg.T("付与ファイル",  pad=(19, 0)), sg.I("書き込み不可", k='-INPUT_GRANT_FILRS', disabled_readonly_background_color="gray", disabled=True), sg.FilesBrowse("検索",s=(10, 1), k='-GRANT_FILRS', disabled=False)],
            [sg.Frame(layout=[
                [sg.T("ゼロ詰め ON/OFF"), sg.CBox("", k="CBOX3", enable_events=True), sg.T("OFF", size=(3,1), k="Check3")],
                [sg.Radio('', "G_Radio", key='G_Radio0', default=True), sg.T("1xxx.yyy", k="G_RADIO_TEXT1", s=(9, 1)), 
                sg.Radio('', "G_Radio", key='G_Radio1'),sg.T("1_xxx.yyy", k="G_RADIO_TEXT2", s=(9, 1)),  
                sg.Radio('', "G_Radio", key='G_Radio2'), sg.T("xxx1.yyy", k="G_RADIO_TEXT3", s=(9, 1)), 
                sg.Radio('', "G_Radio", key='G_Radio3'),sg.T("xxx_1.yyy", k="G_RADIO_TEXT4", s=(9, 1))]
                            ], title="ファイルタイプ")],
            [sg.B("実行", k="GRANT_BUTTON")]
        ]



# テンプレートファイル＆フォルダのコピー
layout_template = [
          [sg.T("テンプレート作成", pad=((150, 0), (10, 10)), font=("", 20))],
          [sg.T("保存場所", pad=(19, 0)), sg.I(k='-DESTINATION', disabled_readonly_background_color="gray", disabled=True), sg.FolderBrowse("検索",s=(10, 1), k='-TEMPLATES')],
          [sg.T("保存名", pad=(26, 0)), sg.I('', s=(35, 1), k='-FOLDER_NAME')],
          [sg.T("テンプレート"), sg.Combo(template, default_value="テンプレート", s=(40, 1), k='TEMPLATES_FOLDER')],
          [sg.B("実行", k="TEMPLATES_BUTTON")] 
         ]


layout = [
    [sg.TabGroup([
        [sg.Tab("連番", layout_cereal), sg.Tab("リネーム", layout_rename), sg.Tab("連番付与", layout_sequence_grant), sg.Tab("テンプレート作成", layout_template)]
    ])], 
]


padding = ["01xxx.yyy" , "01_xxx.yyy", "xxx01.yyy", "xxx_01.yyy", "1xxx.yyy", "1_xxx.yyy", "xxx1.yyy", "xxx_1.yyy"]
not_filename = ['\\', '/', '?', '*', '"', '<', '>', '|']

window = sg.Window('file control', layout)
count = 0
while True:
    event, values = window.read()
    print(event, values)


    if event == sg.WIN_CLOSED:
        break
    
    ##### ファイル作成 #####
    if event == 'CBOX':
        change_color(window["Check"], values["CBOX"])

    
    change_text(window["RADIO_TEXT1"], window["RADIO_TEXT2"], window["RADIO_TEXT3"], window["RADIO_TEXT4"], values["CBOX"])
    file_type_pattern = file_type(list(values.items()), "Radio", values["CBOX"])
    # print(file_type_pattern)

    if event == "-DISPLAY":
        window["-ASSUMPTION"].update(f'{file_type_pattern.replace("xxx", values["-NAME"]).replace("yyy", values["-EXTENSION"])}')

    # 関数にしてきれいにしたい
    if event == 'CREATES_BUTTON':
        if values['-NAME'] == "":
            error(window['-NAME'], 'ファイル名がありません', 'Not file name', 'ファイル名入力', 'file name error')
            continue

        if not values["-EXTENSION"] in extension_lists or type(values["-EXTENSION"]) == "拡張子入力または選択":
            error(window["-EXTENSION"], '拡張子が正しくありません', 'Not extension', '拡張子の入力', 'extension error')
            continue

        if isinstance(values["-FILE_NUMBER"], str):
            error(window["-FILE_NUMBER"], '数字を入力してください', 'Not number', '作成ファイル数の入力', 'file number error')
            continue

        if "\\" in values['-INPUT_SAVE_FILR']:
            values['-INPUT_SAVE_FILR'].replace("\\", "/")
        elif os.path.exists(values['-SAVE_FILR']) != True or os.path.exists(values['-INPUT_SAVE_FILR']) != True:
            error(window['-INPUT_SAVE_FILR'], 'ファイルパスが正しくありません', 'Not file pass', 'ファイルパスの入力', 'pass error')
            continue

        # かけない文字があれば書き直させるか、プログラムで除去する
        for i in values['-NAME']:
            if i in not_filename:
                sg.popup_error('ファイル名に無効な文字が使われています"\n"「 \\ / ? * \" < > | 」', title='Not name')
                continue

        pop_check = sg.popup_yes_no(f'''
　保存場所：{values['-INPUT_SAVE_FILR']}
ファイル名：{values["-NAME"]}
　拡張子　：{values["-EXTENSION"]}
連番タイプ：{file_type_pattern}
ファイル数：{values["-FILE_NUMBER"]}
        ''', title='確認')
        # ファイルパス、名前、拡張子、作成数を初期値に戻す
        if pop_check == 'Yes':
            if os.path.exists(f"{values['-SAVE_FILR']}\\{file_type_pattern.replace('xxx', values['-NAME']).replace('yyy', values['-EXTENSION'])}") == True:
                sg.popup_error("すでにファイルが存在します。\nファイル名\n連番タイプ\n拡張子\nの変更をお願いします", title='file error')
                continue
            if os.path.exists(values['-SAVE_FILR']) == True or os.path.exists(values['-INPUT_SAVE_FILR']) == True:
                file_numbers(values['-INPUT_SAVE_FILR'], values['-FILE_NUMBER'], file_type_pattern, values['-NAME'], values['-EXTENSION'].lower(), padding)
                sg.popup('連番ファイルが作成されました')
                window['-INPUT_SAVE_FILR'].update()
                # sg.popup_quick_message('連番ファイルが作成されました')
            else:
                sg.popup_error('ファイルパスがありません')
                continue
        else:
            sg.popup('作成がキャンセルされました')
            continue

    ##### ファイルリネーム #####
    if event == 'CBOX2':
        change_color(window["Check2"], values["CBOX2"])

    change_text(window["C_RADIO_TEXT1"], window["C_RADIO_TEXT2"], window["C_RADIO_TEXT3"], window["C_RADIO_TEXT4"], values["CBOX2"])
    file_type_r = file_type(list(values.items()), "C_Radio", values["CBOX2"])

    if event == 'CHANGE':
        count += 1
        if count % 2 == 1:
            window['CHANGE'].update("複数変更に変更")
            # window['-INPUT_RENAME_FILR'].update(disabled=False)
            window['-RENAME_FILR'].update(disabled=False)
            # window['-INPUT_RENAME_FILRS'].update("", disabled=True)
            window['-RENAME_FILRS'].update(disabled=True)
            window['-INPUT_RENAME_FILRS'].update("書き込み不可")
        else:
            window['CHANGE'].update("単一ファイルに変更")
            # window['-INPUT_RENAME_FILR'].update("", disabled=True)
            window['-RENAME_FILR'].update(disabled=True)
            # window['-INPUT_RENAME_FILRS'].update(disabled=False)
            window['-RENAME_FILRS'].update(disabled=False)
            window['-INPUT_RENAME_FILR'].update("書き込み不可")

    if values['EXTENSION_EDIT'] == True:
        window['-CHANGE_EXTENSION'].update(disabled=False)
        window['-CHANGE_NAME'].update(disabled=True)
        window['CBOX2'].update(disabled=True)
        window['C_Radio0'].update(disabled=True)
        window['C_Radio1'].update(disabled=True)
        window['C_Radio2'].update(disabled=True)
        window['C_Radio3'].update(disabled=True)
        window['Check2'].update(text_color="gray")
        window['C_RADIO_TEXT1'].update(text_color="gray")
        window['C_RADIO_TEXT2'].update(text_color="gray")
        window['C_RADIO_TEXT3'].update(text_color="gray")
        window['C_RADIO_TEXT4'].update(text_color="gray")
        window['-MODE_TEXT-'].update("拡張子変更")
    else:
        window['-CHANGE_EXTENSION'].update("拡張子入力または選択", disabled=True)
        window['-CHANGE_NAME'].update(disabled=False)
        window['CBOX2'].update(disabled=False)
        window['C_Radio0'].update(disabled=False)
        window['C_Radio1'].update(disabled=False)
        window['C_Radio2'].update(disabled=False)
        window['C_Radio3'].update(disabled=False)
        window['Check2'].update(text_color="#ffffff")
        window['C_RADIO_TEXT1'].update(text_color="#ffffff")
        window['C_RADIO_TEXT2'].update(text_color="#ffffff")
        window['C_RADIO_TEXT3'].update(text_color="#ffffff")
        window['C_RADIO_TEXT4'].update(text_color="#ffffff")
        window['-MODE_TEXT-'].update("ファイルリネーム")



    if values['EXTENSION_EDIT'] == True and event == 'RENAME_BUTTON':
        if values['-CHANGE_EXTENSION'] == "拡張子入力または選択":
            sg.popup_error('拡張子が設定されていません', title='Not extension')
            continue
        elif values['-CHANGE_EXTENSION'] == "":
            sg.popup_error('拡張子が設定されていません', title='Not extension')
            continue
        
        if not values['-CHANGE_EXTENSION'] in extension_lists or type(values['-CHANGE_EXTENSION']) == "拡張子入力または選択":
            sg.popup_error('拡張子が正しくありません', title='Not extension')
            continue
        
        yes = sg.popup_yes_no("拡張子の変更するとファイルが破損する恐れがあります\nそれでもよろしいですか？", title="break file")
        if yes == "Yes":
            if not values['-INPUT_RENAME_FILR'] == "書き込み不可":
                ex_change(values['-INPUT_RENAME_FILR'], values['-CHANGE_EXTENSION'])
                sg.popup_quick_message("拡張子が変更されました")
                window['-INPUT_RENAME_FILR'].update("書き込み不可")
            elif not values['-INPUT_RENAME_FILRS'] == "書き込み不可":
                ex_changes(values['-INPUT_RENAME_FILRS'], values['-CHANGE_EXTENSION'])
                sg.popup_quick_message("拡張子が変更されました")
                window['-INPUT_RENAME_FILRS'].update("書き込み不可")
            else:
                sg.popup_error('拡張子が設定されていません', title='Not extension')
        else:
            sg.popup_quick_message("変更がキャンセルされました")
            continue

    elif event == 'RENAME_BUTTON':
        if values['-CHANGE_NAME'] == "":
            sg.popup_error('ファイル名がありません', title='Not file name')
            continue
        if not values['-INPUT_RENAME_FILR'] == "書き込み不可":
            file_rename(values['-INPUT_RENAME_FILR'], values['-CHANGE_NAME'])
            sg.popup_quick_message("ファイル名が変更されました")
            window['-INPUT_RENAME_FILR'].update("書き込み不可")
        elif not values['-INPUT_RENAME_FILRS'] == "書き込み不可":
            files_rename(values['-INPUT_RENAME_FILRS'], values['-CHANGE_NAME'], file_type_r, padding)
            sg.popup_quick_message("ファイル名が変更されました")
            window['-INPUT_RENAME_FILRS'].update("書き込み不可")
        else:
            sg.popup_error('変更ファイルのパスが設定されていません', title='Not file pass')
            continue

##### 連番付与 #####
    change_text(window["G_RADIO_TEXT1"], window["G_RADIO_TEXT2"], window["G_RADIO_TEXT3"], window["G_RADIO_TEXT4"], values["CBOX3"])
    file_type_grant = file_type(list(values.items()), "G_Radio", values["CBOX3"])
    if event == "GRANT_BUTTON":
        if values['-INPUT_GRANT_FILRS'] == "書き込み不可":
            sg.popup_error("付与ファイルが設定されていません")
            continue
        
        files_grant(values['-INPUT_GRANT_FILRS'], file_type_grant, padding)
        sg.popup_quick_message("ファイルの連番付与ができました")
        window['-INPUT_GRANT_FILRS'].update("書き込み不可")

##### テンプレートファイル #####
    if event == "TEMPLATES_BUTTON":
        if values['-DESTINATION'] == "":
            sg.popup_error("保存先が設定されていません")
            continue

        if values['-FOLDER_NAME'] == "":
            error(window['-FOLDER_NAME'], '保存名がありません', 'Not file name', '保存名入力', 'file name error')
            continue

        for i in values['-FOLDER_NAME']:
            if i in not_filename:
                sg.popup_error('保存名に無効な文字が使われています"\n"「 \\ / ? * \" < > | 」', title='Not name')
                continue

        if os.path.isfile(values['TEMPLATES_FOLDER']):
            basename = os.path.basename(values['TEMPLATES_FOLDER'])
            splitext = os.path.splitext(basename)
            if os.path.exists(f"{values['-DESTINATION']}\\{values['-FOLDER_NAME']}{splitext[1]}"):
                sg.popup_error(f"すでに同じ名前のファイルが存在します")
            else:
                copy_file(values['TEMPLATES_FOLDER'], values['-DESTINATION'], values['-FOLDER_NAME'])
                sg.popup_quick_message(f"{values['-DESTINATION']}\\{values['-FOLDER_NAME']}{splitext[1]}\nに作成されました")
        elif os.path.isdir(values['TEMPLATES_FOLDER']):
            if os.path.exists(f"{values['-DESTINATION']}\\{values['-FOLDER_NAME']}"):
                sg.popup_error(f"すでに同じ名前のフォルダが存在します")
            else:
                copy_folder(values['TEMPLATES_FOLDER'], values['-DESTINATION'], values['-FOLDER_NAME'])
                sg.popup_quick_message(f"{values['-DESTINATION']}\\{values['-FOLDER_NAME']}\nに作成されました")
        else:
            sg.popup_error("テンプレートファイルが存在しません")


window.close()