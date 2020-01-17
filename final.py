import tkinter
import mysql.connector as mc


#  DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE

class pess:

    def __init__(self):

        self.conn = mc.connect(host='localhost', user='root', password='89234037252')

        state = 'settled' if self.conn else 'not settled'

        print('connection ' + state)

        self.cursor = self.conn.cursor()

    '''def show_me(self):

        self.cursor.execute('use my')

        self.cursor.execute('show tables')

        R = self.cursor.fetchall()

        R = [i[0] for i in R]

        print(R)  '''

    def selectall(self, list_month):

        

        self.cursor.execute('use my')

        self.cursor.execute('select * from elen where month = ' + '"' + list_month + '"')

        self.L = [i for i in self.cursor]


    def insertion(self, nameMonth_str, current_month_str, last_month_str, itogo_kvt_str, itogo_rub_srt):

        self.cursor.execute('use my')

        self.cursor.execute('insert into elen(month, current_month, last_month, itogo_kvt, itogo_rub) values(' + '"'+ nameMonth_str + '"' + ',' + current_month_str + ',' + last_month_str + ',' + itogo_kvt_str + ',' + itogo_rub_srt + ')')

        self.conn.commit()

    def show_months(self):

        self.cursor.execute('use my')

        self.cursor.execute('select month from elen')

        self.f = [i for i in self.cursor]


p = pess()

# #  DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE





# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


# main window

root = tkinter.Tk()
root.geometry('500x300')

# Listbox 

listbox1 = tkinter.Listbox(height=3, width=15)
listbox1.place(x = 30, y = 30)



# Textarea

text_show_data_fetched = tkinter.Text(height=8, width=15)
text_show_data_fetched.place(x = 30, y = 130)


# name month

name_month_enrty = tkinter.Entry()
name_month_enrty.place(x = 330, y = 50)

new_comment_label = tkinter.Label(text='Имя месяца:')
new_comment_label.place(x = 200, y = 50)


# last month

last_month_enrty = tkinter.Entry()
last_month_enrty.place(x = 330, y = 90)



# Lable last_month

last_month_label = tkinter.Label(text='Прошлый месяц:')
last_month_label.place(x = 200, y = 90)

# current month

current_month_entry = tkinter.Entry()
current_month_entry.place(x = 330, y = 130)



# Lable current_month

current_month_label = tkinter.Label(text='Текущий месяц:')
current_month_label.place(x = 200, y = 130)

# Entry rate

rate_entry = tkinter.Entry()
rate_entry.place(x = 330, y = 180)



# Lable rate

rate_label = tkinter.Label(text='Тариф:')
rate_label.place(x = 200, y = 180)



# Button for evaluating payment

def insertion():
	rate = rate_entry.get()

	nameMonth_str = name_month_enrty.get()

	current_month_str = current_month_entry.get()

	last_month_str = last_month_enrty.get()

	itogo_kvt_str = str(int(current_month_str) - int(last_month_str))

	itogo_rub_srt = str(int(itogo_kvt_str)*int(rate))

	p.insertion(nameMonth_str, current_month_str, last_month_str, itogo_kvt_str, itogo_rub_srt)

evaluate_button = tkinter.Button(text='Подсчитать', command = insertion)
evaluate_button.place(x = 270, y = 230)

# Button for fetching data from DB

def button_show():

    text_show_data_fetched.delete(1.0, tkinter.END)

    selected_month = listbox1.get(tkinter.ACTIVE)

    p.selectall(selected_month)

    print(p.L)

    text_show_data_fetched.insert(1.0, p.L)

    
button_fetch_data = tkinter.Button(text='Показать', command=button_show)

button_fetch_data.place(x = 180, y = 230)

def show_months():
    
    p.show_months()

    list1 = p.f # creating list to insert to listbox

    for i in list1:
        listbox1.insert(tkinter.END, str(i[0]))

    print(list1, type(list1))

    

button_show_months = tkinter.Button(text='месяцы', command=show_months)

button_show_months.place(x = 130, y = 40)

# Button for closing the programm window


close_button = tkinter.Button(text='Закрыть', command = root.quit)
close_button.place(x = 390, y = 230)

# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


root.mainloop()
