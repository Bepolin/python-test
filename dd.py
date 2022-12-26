import PySimpleGUI as sg
from os.path import basename


layout = [[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(key='OK'), sg.Cancel(key='終了')],
          [sg.Listbox([], size=(100, 10), enable_events=True, key='-LIST-')],]

new_files = []
new_file_names = []
window = sg.Window('エクセルの結合', layout)
while True:             # Event Loop
    event, values = window.read()
    if event in (None, '終了'):
        break

    elif event == 'OK':
        print('FilesBrowse')

        # TODO:実運用には同一ファイルかどうかの処理が必要
        new_files.extend(values['_FILES_'].split(';'))
        new_file_names.extend([basename(file_path) for file_path in new_files])

        print('ファイルを追加')
        window['-LIST-'].update(new_file_names)  # リストボックスに表示します

window.close()
print(values['_FILES_'].split(';'))