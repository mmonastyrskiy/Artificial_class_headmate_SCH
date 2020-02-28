from matplotlib import pyplot as plt
import tkinter as tk
import xlwt
import numpy as np
import os
"""
не работает!!! нужно заполнить массивы classes
0) стартовый индекс учеников
1) индекс последнего студента

"""
classes = [[None,None] for i in range(0,145)]
    




# Класс для всех сотрудников и учеников, для администрации.
classes[0][0] = 0 # Начальный сотрудник в log-ах
classes[0][1] = 3737 # конечный сотрудник в log-ах




root = tk.Tk()

root.title("Импорт таблицы")

class_inp = tk.Entry(root)

def GenerateINList(event):
    cl = class_inp.get()
    logfile = "log.log"
    with open(logfile) as f:
        data_to_process = []
        for student in range(classes[int(cl)][1],(classes[int(cl)][2] + 1)):
            if "True" in f[student]:
                data_to_process.append(f[student.append(str(student))])
    ## работа с таблицей
            font0 = xlwt.Font()
            font0 = "Times New Roman"
            font0.colour_index = 2
            style0 = xlwt.XFStyle()
            style0 = font0
            wb = xlwt.Workbook()
            ws = wb.add_sheet(str(cl + "Sheet"))
            for i in range(0,len(logfile)):
                ws.write(0,i,data_to_process[i][-1])
                ws.write(1,i,data_to_process[i][1])
            wb.save(str(cl) + ".xls")
            return data_to_process
    
def GenerateOUTList(event):
    logfile = "/Data/log.log"
    cl = class_inp.get()
    with open(logfile) as f:
        data_to_process = []
        for student in range(classes[int(cl)][1],(classes[int(cl)][2] + 1)):
            if "False" in f[student]:
                data_to_process.append(f[student])
            font0 = xlwt.Font()
            font0 = "Times New Roman"
            font0.colour_index = 2
            style0 = xlwt.XFStyle()
            style0 = font0
            wb = xlwt.Workbook()
            ws = wb.add_sheet(str(cl + "Sheet"))
            for i in range(0,len(logfile)):
                ws.write(0,i,data_to_process[i][-1])
                ws.write(1,i,data_to_process[i][1])
            wb.save(str(cl) + ".xls")
            return data_to_process

                
def GenerateLATEList(event):
    logfile = "/Data/log.log"
    cl = class_inp.get()
    with open(logfile) as f:
        data_to_process = []
        for student in range(classes[int(cl)][1],(classes[int(cl)][2] + 1)):
            if "True" in f[student] and (f[student].split()[1].split()[1].split('.')[0].split(":")[0] <= 8)  and (f[student].split()[1].split()[1].split('.')[0].split(":")[1]) <= 25:
                data_to_process.append(f[student])
            font0 = xlwt.Font()
            font0 = "Times New Roman"
            font0.colour_index = 2
            style0 = xlwt.XFStyle()
            style0 = font0
            wb = xlwt.Workbook()
            ws = wb.add_sheet(str(cl + "Sheet"))
            for i in range(0,len(logfile)):
                ws.write(0,i,data_to_process[i][-1])
                ws.write(1,i,data_to_process[i][1])
            wb.save(str(cl) + ".xls")
            return data_to_process


def Plort_builder(event):
    actual_data = []
    actual_data.append(GenerateINList(None))
    actual_data.append(GenerateOUTList(None))
    actual_data.append(GenerateLATEList(None))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis("equal")
    titles = ["В школе","отсувствуют","опоздавших"]
    ax.pie(actual_data,labels = titles,autopct = "%1.2f%%")
    plt.show()



l = tk.Label(root,text = "Введите ID класса")
Plort_builder_btn = tk.Button(root,text = "Построить график")
in_btn = tk.Button(root,text="Получить список присутствующих")
out_btn = tk.Button(root,text="Получить список отсувствующих")
late_btn = tk.Button(root,text="Получить список опоздавших")

in_btn.bind("<Button-1>",GenerateINList)
out_btn.bind("<Button-1>",GenerateOUTList)
late_btn.bind("<Button-1>",GenerateLATEList)
Plort_builder_btn.bind("<Button-1>",Plort_builder)

l.pack()
class_inp.pack()
in_btn.pack()
out_btn.pack()
late_btn.pack()
Plort_builder_btn.pack()




root.mainloop()
