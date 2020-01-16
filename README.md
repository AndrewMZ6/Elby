# Elby
My app for electroenergy consumption calculation - GUI(tkinter) + Database(Sqlite3) + Python

I want my app to store data about my monthly electroenergy consumption

As an addition I want to pull out (extract) data for the past months 

So the functionality I want is this:

  1. adding current + past month indictions to existing database
  
  2. calculation of consumed energy and how much to pay for it
  
  3. fetching data of chosen month to be displayed

So the blocks are these:

  1. GUI created using standard tkinter python library
  
  2. MySql server 8.0 (or smth) which contains data
  
  3. python Core which does all the manipulations with data:
  
      MySqlDataBase  <----------->  Python Core  <------------>  GUI
