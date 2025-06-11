# encoding: utf8
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry('300x200')
app.title('画像リサイズ')

lb1_1 = tk.Label(text='リサイズしたいサイズを入力してください')
lb1_1.place(x=30,y=30)

lbl = tk.Label(text='横幅')
lbl.place(x=30, y=50)

lb2 = tk.Label(text='縦幅')
lb2.place(x=30, y=70)

txt1 = tk.Entry(width=20)
txt1.place(x=90, y=50)

txt2 = tk.Entry(width=20)
txt2.place(x=90, y=70)

def btn_click1():
    global width_size
    global height_size
    width_size, height_size = txt1.get(), txt2.get()
    lb1_2 = tk.Label(text=f'横幅: {width_size}')
    lb1_2.place(x=60, y=100)
    lb2_2 = tk.Label(text=f'縦幅: {height_size}')
    lb2_2.place(x=130, y=100)

btn1 = tk.Button(app, text='入力したサイズを読み込み', command=btn_click1)
btn1.place(x=30, y=140)

# 画像リサイズ
def btn_click2():
    canvas = tk.Canvas(app,
                       width= int(width_size),
                       height= int(height_size),
                       relief=tk.RIDGE)
    canvas.place(x=0,y=0)

    file = filedialog.askopenfilename(
    title = "画像ファイルを開く",
    filetypes = [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], # ファイルフィルタ
    initialdir = "./" # 自分自身のディレクトリ
    )

    img = Image.open(open(file, 'rb'))
    img_1 = img.resize((int(width_size),int(height_size)))
    img_1.save(f"{file}_resize.jpg")
    #img_2 = ImageTk.PhotoImage(img_1)
    #canvas.create_image(0, 0, image=img_2, tag="illust", anchor=tk.NW)
    app.destroy()

btn2 = tk.Button(app, text='リサイズしたい画像ファイルを選択して実行', command=btn_click2)
btn2.place(x=30, y=170)

app.mainloop()
