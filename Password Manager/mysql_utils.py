import mysql.connector
from my_socket import localhost

try:
	cnx = mysql.connector.connect(
		user="root",
		password="root",
		host=localhost,
		database="passwords"
	)
	cursor = cnx.cursor()
	print("Database connection successful!")
except Exception as _ex:
	print(f"Database connect error: {_ex}")

class DataBase(object):
	def selectFromDB(self, service, info = 'None'):
		cursor = cnx.cursor()
		res = ""
		if len(service) == 0:
			self.service = 'None'
		else:
			self.service = str(service)

		try:
			if info != 'None':
				cursor.execute(f"SELECT `Service`, `Login/username`, `Passwords` FROM `my_password` WHERE `Service` = '{(service)}' AND `Note` = '{(info)}'")
			else:
				cursor.execute(f"SELECT `Service`, `Login/username`, `Passwords` FROM `my_password` WHERE `Service` = '{(service)}'")
			res = cursor.fetchall()
			for i in res:
				print(f"res: {i}")
			if len(res) != 0:
				self.service = str(res[0][0])
				self.login = str(res[0][1])
				self.password = str(res[0][2])
			else:
				self.login = "None"
				self.password = "None"
			print("Data has selected successful or haven't found!")
		except Exception as ex:
			print("[Error] Data select error: ")
			print(ex)
		cursor.close()
