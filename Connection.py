import mysql.connector as mc

class pess:


	def __init__(self):

		self.conn = mc.connect(host = 'localhost', user = 'root', password = '89234037252')

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

		

	def insert(self):

		self.cursor.execute('use my')

		self.cursor.execute('insert into elen values(3, "february", 666, 555, 111, 120)')

		self.conn.commit()

x = 'select * from elen'

p = pess()

p.selectall(x)

input()
