import tkinter as tk
import tkinter.font
import subprocess
import os

# ウィンドウを作成 --- (*1)
root = tk.Tk()
root.geometry("500x250")  # サイズを指定
root.title("SteamLikeApp")

# file_path program
file_name = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

app_namelist = []

# Font SET
button_font = tkinter.font.Font(
    family= 'Menlo',
    size = 20,
    weight = tkinter.font.BOLD,
)

def btn_click(text):
    def inner():
        os.startfile(rf'{file_name}\{text}.lnk')
    return inner

# フォルダ内のショートカットのみを抽出
for i in os.listdir(file_name):
    app_name = i.split('.')
    if len(app_name) == 2 and app_name[1] == 'exe':
        app_namelist.append(app_name[0])
    if len(app_name) == 2 and app_name[1] == 'lnk':
        app_namelist.append(app_name[0])

# 起動時実行するのを回避


for app_text in app_namelist:
    btn = tk.Button(
        root,
        text = app_text,
        command=btn_click(app_text), 
        bg = '#32cd32' , 
        fg = '#fff',
        font= button_font)
    btn.pack(expand = 1, fill = tk.BOTH, anchor = tk.NW)



root.mainloop()


        