import tkinter
import mysql.connector as mc


#  DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE ------------ DATABASE

# the class for creating object by using which i can interract with mysql server on my local machine

class pess:

	def __init__(self):     # creating connection and cursor for sending querries

		self.conn = mc.connect(host='localhost', user='root', password='12345')

		state = 'settled' if self.conn else 'not settled'

		print('connection ' + state)

		self.cursor = self.conn.cursor()

		self.cursor.execute('use my') # Using database my.db   I created it mysql WorkBench

	

	def selectall(self, list_month):  # method for sending SELECT * query

		self.cursor.execute('select * from elen where month = ' + '"' + list_month + '"')

		self.L = [i for i in self.cursor]     # creates list L that looks like this [(21, 'December', 18771, 17781, 990, 1980)], it's tuple inside the list



	def insertion(self, nameMonth_str, current_month_str, last_month_str, itogo_kvt_str, itogo_rub_srt):  # CREATE

		self.cursor.execute('insert into elen(month, current_month, last_month, itogo_kvt, itogo_rub) values(' + '"'+ nameMonth_str + '"' + ',' + current_month_str + ',' + last_month_str + ',' + itogo_kvt_str + ',' + itogo_rub_srt + ')')

		self.conn.commit()

	def show_months(self):      # shows all months available in table to insert them into listbox widget                # READ

		self.cursor.execute('select month from elen')

		self.f = [i for i in self.cursor]



			# UPDATE



	def delete_months(self, month):    # deletes row in Mysql DB with month chosen in listbox         # DELETE

		self.cursor.execute('delete from elen where month =' + '"' + month + '"')

		self.conn.commit()   # I think I should create some sort of SUBMIT window for this to commit deletion



p = pess()  # creating object here so I can use it downstairs

# #  DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE -----^^----- DATABASE





# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


# main window

root = tkinter.Tk()
root.geometry('500x300')

# Listbox  ----------- for showing and choosing months to show and delete

listbox1 = tkinter.Listbox(height=3, width=15)
listbox1.place(x = 30, y = 30)


# Text  -------------  it's a place where I show info from DB

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


	rate_entry.delete(0, tkinter.END)
	name_month_enrty.delete(0, tkinter.END)
	current_month_entry.delete(0, tkinter.END)		# Clearing all input forms after button clicked
	last_month_enrty.delete(0, tkinter.END)


evaluate_button = tkinter.Button(text='Подсчитать', command = insertion)
evaluate_button.place(x = 270, y = 230)

# Button for fetching data from DB

def button_show():

	text_show_data_fetched.delete(1.0, tkinter.END) # Clean the form

	selected_month = listbox1.get(tkinter.ACTIVE)   # Get info from listbox1

	p.selectall(selected_month)

	text_show_data_fetched.insert(1.0, 'Месяц = ' + p.L[0][1] + '\n' + 'прошл. = ' + str(p.L[0][2]) + '\n' + 'текущ. = ' + str(p.L[0][3]) + '\n' +  'итогоКВТ. = ' + str(p.L[0][4]) + '\n' + 'итогоРУБ. = ' + str(p.L[0][5]))

	
button_fetch_data = tkinter.Button(text='Показать', command=button_show)

button_fetch_data.place(x = 180, y = 230)

def show_months():

	listbox1.delete(0, tkinter.END)
	
	p.show_months()

	list1 = p.f # creating list to insert to listbox

	for i in list1:
		listbox1.insert(tkinter.END, str(i[0]))

	

	

button_show_months = tkinter.Button(text='Месяцы', command=show_months)

button_show_months.place(x = 130, y = 40)

def delete_months():

	selected_month = listbox1.get(tkinter.ACTIVE)

	p.delete_months(selected_month)

	listbox1.delete(0, tkinter.END)

	p.show_months()

	list1 = p.f # creating list to insert to listbox

	for i in list1:
		listbox1.insert(tkinter.END, str(i[0]))


button_delete_months = tkinter.Button(text='Удалить', command=delete_months)

button_delete_months.place(x = 40, y = 90)

# Button for closing the programm window


close_button = tkinter.Button(text='Закрыть', command = root.quit)
close_button.place(x = 390, y = 230)

# #  Tkinter  ------------ Tkinter ------------ Tkinter ------------ Tkinter ------------ Tkinter


root.mainloop()
