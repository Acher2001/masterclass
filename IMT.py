from tkinter import *
from tkinter import messagebox

root=Tk()

def clic():
    v=ves.get()
    r=rost.get()
    imt=int(v)/((int(r)/100)**2)

    info_str=f'ИМТ: {imt}'
    messagebox.showinfo(title='Индекс Массы Тела', message=info_str)


root['bg']='#ffffff'  #Вводим фон
root.title('Индекс Массы Тела')  #Вводим название
root.wm_attributes('-alpha', 0.85)  #Вводим прозрачность окна
root.geometry('300x175')  #Вводим размер окна

root.resizable(width=False, height=False)  #Огроничение размера окна

canvas=Canvas(root, height=300, width=175)  #Создоём холст
canvas.pack()

frame=Frame(root, bg='white')  #Рамка с другими виз. кампонентоми
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)  #Обект

title1=Label(frame, text='Введите вес', bg='#990066', font=40)  #Текст
title1.pack()
ves=Entry(frame, bg='#fafafa')
ves.pack()
title2=Label(frame, text='Введите рост', bg='#990066', font=40)  #Текст
title2.pack()
rost=Entry(frame, bg='#fafafa')
rost.pack()
btn=Button(frame, text='Расчитать индекс', bg='#fafafa', command=clic)  #Кнопка
btn.pack()


root.mainloop()  #Постояный цикл запуска окна
