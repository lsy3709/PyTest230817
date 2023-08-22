from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()

photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/pic7.xlsx')
worksheetR = workbook.add_worksheet('photoR')
worksheetG = workbook.add_worksheet('photoG')
worksheetB = workbook.add_worksheet('photoB')

for i in range(w) :
    for k in range(h) :
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

workbook.close()
print('Save. OK~')