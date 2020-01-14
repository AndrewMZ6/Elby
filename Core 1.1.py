import tkinter
import sqlite3

# Creating main window named root

root = tkinter.Tk()
root.geometry('500x300')


# Left side frame containing listbox, fetch data button and display data area 

frame_left = tkinter.Frame(root)     # -------------------------== LEFT FRAME ==--------------------------
frame_left.grid(row = 0, column = 0)


# Listbox widget for choosing month to display

listbox1 = tkinter.Listbox(frame_left, height = 5, width = 15)
listbox1.pack()

list1 = ['Май', 'Июнь', 'Июль'] # creating list to insert to listbox

for i in list1:
	listbox1.insert(tkinter.END, i)



# Button for fetching data from DB

button_fetch_data = tkinter.Button(frame_left, text = 'Показать',)
button_fetch_data.pack()


# Textarea for showing data from DB

text_show_data_fetched = tkinter.Text(frame_left, height = 10, width = 10)
text_show_data_fetched.pack()


# Right side frame containing: entries for current month indication, last month indication and rate
#							   labels for the entries
#							   buttons for evaluating payment and closing window
#							   text

frame_right = tkinter.Frame(root)   # -------------------------== RIGHT FRAME ==--------------------------
frame_right.grid(row = 0, column = 1)


# Enrty for the last month indication

last_month_enrty = tkinter.Entry(frame_right)
last_month_enrty.grid(row = 0, column = 1)


# Lable for last_month_enrty

last_month_label = tkinter.Label(frame_right, text = 'Прошлый месяц:')
last_month_label.grid(row = 0, column = 0, sticky = 'e')

# Entry for the current month indication

current_month_entry = tkinter.Entry(frame_right)
current_month_entry.grid(row = 1, column = 1)


# Lable for current_month_entry

current_month_label = tkinter.Label(frame_right, text = 'Текущий месяц:')
current_month_label.grid(row = 1, column = 0, sticky = 'e')

# Entry for the rate value

rate_entry = tkinter.Entry(frame_right)
rate_entry.grid(row = 2, column = 1)


# Lable for rate_entry

rate_label = tkinter.Label(frame_right, text = 'Тариф:')
rate_label.grid(row = 2, column = 0, sticky = 'e')

new_comment_label = tkinter.Label(frame_right, text = 'Новый кек')
new_comment_label.grid(row = 3, column = 0, sticky = 'e')

# Button for evaluating payment

evaluate_button = tkinter.Button(frame_right, text = 'Подсчитать')
evaluate_button.grid(row = 3, column = 1)

# Button for closing the programm window

close_button = tkinter.Button(frame_right, text = 'Закрыть')
close_button.grid(row = 4, column = 1)


#
#  DATABASE
#
# 


root.mainloop()



# 
