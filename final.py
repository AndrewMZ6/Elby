import tkinter
import mysql.connector as mc


#  DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE

class pess:

    def __init__(self):
        self.conn = mc.connect(host='localhost', user='root', password='89234037252')

        state = 'settled' if self.conn else 'not settled'

        print('connection ' + state)

        self.cursor = self.conn.cursor()

    def show_me(self):
        self.cursor.execute('use my')

        self.cursor.execute('show tables')

        R = self.cursor.fetchall()

        R = [i[0] for i in R]

        print(R)

    def selectall(self, x):

        self.cursor.execute('use my')

        self.cursor.execute(x)

        records = self.cursor.fetchall()

        for row in records:

            print(row)

            print(type(row))

    def insertion(self, N_str, nameMonth_str, current_month_str, last_month_str, itogo_kvt_str, itogo_rub_srt):

        self.cursor.execute('use my')

        self.cursor.execute('insert into elen values(' + N_str + ',' + '"'+ nameMonth_str + '"' + ',' + current_month_str + ',' + last_month_str + ',' + itogo_kvt_str + ',' + itogo_rub_srt + ')')

        self.conn.commit()

p = pess()

# #  DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE





# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


# main window

root = tkinter.Tk()
root.geometry('500x300')

# Left side frame 

frame_left = tkinter.Frame(root)  # -------------------------== LEFT FRAME ==--------------------------
frame_left.grid(row=0, column=0)

# Listbox 

listbox1 = tkinter.Listbox(frame_left, height=5, width=15)
listbox1.place(x = 30, y = 30)

list1 = ['Май', 'Июнь', 'Июль']  # creating list to insert to listbox

for i in list1:
    listbox1.insert(tkinter.END, i)

# Textarea

text_show_data_fetched = tkinter.Text(frame_left, height=10, width=10)
text_show_data_fetched.place(x = 30, y = 130)

# Right side frame containing: entries for current month indication, last month indication and rate
#							   labels for the entries
#							   buttons for evaluating payment and closing window
#							   text

frame_right = tkinter.Frame(root)  # -------------------------== RIGHT FRAME ==--------------------------
frame_right.grid(row=0, column=1)


# name month

name_month_enrty = tkinter.Entry(frame_right)
name_month_enrty.grid(row=4, column=1)




# last month

last_month_enrty = tkinter.Entry(frame_right)
last_month_enrty.grid(row=0, column=1)



# Lable last_month

last_month_label = tkinter.Label(frame_right, text='Прошлый месяц:')
last_month_label.grid(row=0, column=0, sticky='e')

# current month

current_month_entry = tkinter.Entry(frame_right)
current_month_entry.grid(row=1, column=1)



# Lable current_month

current_month_label = tkinter.Label(frame_right, text='Текущий месяц:')
current_month_label.grid(row=1, column=0, sticky='e')

# Entry rate

rate_entry = tkinter.Entry(frame_right)
rate_entry.grid(row=2, column=1)



# Lable rate

rate_label = tkinter.Label(frame_right, text='Тариф:')
rate_label.grid(row=2, column=0, sticky='e')

new_comment_label = tkinter.Label(frame_right, text='Новый кек')
new_comment_label.grid(row=3, column=0, sticky='e')

# Button for evaluating payment

def insertion():
	rate = rate_entry.get()
	N_str = '7'
	nameMonth_str = name_month_enrty.get()
	current_month_str = current_month_entry.get()
	last_month_str = last_month_enrty.get()
	itogo_kvt_str = str(int(current_month_str) - int(last_month_str))
	itogo_rub_srt = str(int(itogo_kvt_str)*int(rate))
	p.insertion(N_str, nameMonth_str, current_month_str, last_month_str, itogo_kvt_str, itogo_rub_srt)

evaluate_button = tkinter.Button(frame_right, text='Подсчитать', command = insertion)
evaluate_button.grid(row=3, column=1)

# Button for fetching data from DB

def button_show():
	print(last_month, type(last_month))

button_fetch_data = tkinter.Button(frame_left, text='Показать', command=button_show)
button_fetch_data.grid(row = 1, column = 0)

# Button for closing the programm window


close_button = tkinter.Button(frame_right, text='Закрыть', command = root.quit)
close_button.grid(row=4, column=0)

# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


root.mainloop()
