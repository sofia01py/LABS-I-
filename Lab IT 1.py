from tkinter import *
from tkinter import ttk
import re

root = Tk()
root.title("Калькулятор алгебры полей")
root.configure(bg="#ffcdd2")

#
bttn_list = [
"1", "2", "3", "C", "=",
"4", "5", "6", "+", "-",
"7", "8", "9", "*", "/",
"(", "0", ")", "±", "mod"]

#
r = 3
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

lbl=Label(root, text="Введите выражение по примеру: 10+3-9*4(mod17)", fg="#000000", bg="#ffcdd2")
lbl.grid(row=0, column = 0, columnspan=5)
calc_entry = Entry(root, width = 70)
calc_entry.grid(row=1, column=0, columnspan=5)
lbl1=Label(root, width = 20, text="Ответ по модулю:", fg="#000000", bg="#ffcdd2")
lbl1.grid(row=2, column = 0, columnspan=5)
calc_entry2 = Entry(root, width = 10)
calc_entry2.grid(row=2, column=2, columnspan=5)

#функции кнопок
def calc(key):

    global memory
    if key == "=":
        string = str(calc_entry.get())
        mod01 = string.find("d")
        string = string[mod01 + 1:]
        mod02 = string.find(")")
        mod03 = string[:mod02]
        mod = int(mod03)
        fd = "/"
        global expression

        if fd in calc_entry.get():
            result = str(calc_entry.get())
            index_del = result.find("/")
            m = result[index_del+1:]
            regexp = r"(\d+)"
            a = re.search(regexp, m)
            kk = result.rfind(a[0])
            a = int(a[0])
            i = 0
            j = 0
            a_new = 0

            for i in range(100):
                for j in range(100):
                    if ((i * a) + (j * mod) == 1) or ((i * a) - (j * mod) == 1):
                        a_new = i
                        expression = result
                        expression = expression.replace('/', '*')
                        expression = expression.replace(str(a), str(a_new))
                        zz = expression.find("(")
                        expression = expression[:zz]
                        total1 = eval(str(expression))
                        total = int(total1) % mod
                        calc_entry2.insert(END, total)

                    else:
                        j += 1
                i += 1
                if a_new != 0:
                    break
        else:
            result = str(calc_entry.get())
            index_mod = result.find("(")
            total1 = eval(result[:index_mod])
            if int(total1) < 0:
                total1 = int(total1) + mod
            total = int(total1) % mod
            calc_entry2.insert(END, total)


#очищение поля ввода
    elif key == "C":
        calc_entry.delete(0, END)
        calc_entry2.delete(0, END)

    elif key == "mod":
        calc_entry.insert(END, "(mod")

    elif key == "(":
        calc_entry.insert(END, "(")

    elif key == ")":
        calc_entry.insert(END, ")")

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()