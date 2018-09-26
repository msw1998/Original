from mysql.connector import MySQLConnection, Error

def Time():

        rows = []               #fetch values for y axis
        try:

                db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Time FROM pa")

                rows = [item[0] for item in cursor.fetchall()]
                print(rows)






        except Error as error:
                print(error)

        return rows


def Temp_soil():
			rows1 = []              #fetch values for x axis
			try:
				db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
				conn = MySQLConnection(**db_config)
				cursor = conn.cursor()
				cursor.execute("SELECT 	Temp_soil FROM pa")
				rows1 = [int(item[0]) for item in cursor.fetchall()]
				print(rows1)
			except Error as error:
				print(error)
			return rows1



def Temp_atm():
			rows2 = []              #fetch values for x axis
			try:
				db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
				conn = MySQLConnection(**db_config)
				cursor = conn.cursor()
				cursor.execute("SELECT 	Temp_atm FROM pa")
				rows2 = [int(item[0]) for item in cursor.fetchall()]
				print(rows2)
			except Error as error:
				print(error)
			return rows2

def Moisture():
			rows3 = []              #fetch values for x axis
			try:
				db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
				conn = MySQLConnection(**db_config)
				cursor = conn.cursor()
				cursor.execute("SELECT 	Moisture FROM pa")
				rows3 = [int(item[0]) for item in cursor.fetchall()]
				print(rows3)
			except Error as error:
				print(error)
			return rows3

def Humidity():
			rows4 = []              #fetch values for x axis
			try:
				db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
				conn = MySQLConnection(**db_config)
				cursor = conn.cursor()
				cursor.execute("SELECT 	Humidity FROM pa")
				rows4 = [int(item[0]) for item in cursor.fetchall()]
				print(rows4)
			except Error as error:
				print(error)
			return rows4


def Fetch1():
        row5 = []
        try:
                
                db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Temp_soil FROM pa ORDER BY Time DESC")
                row5 = [int(item[0]) for item in cursor.fetchall()]


                print(row5)
        except Error as error:
                print(error)
        return row5[0]

def Fetch2():
        row6 = []
        try:
                
                db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Temp_atm FROM pa ORDER BY Time DESC")
                row6 = [int(item[0]) for item in cursor.fetchall()]

                print(row6)
        except Error as error:
                print(error)
        return row6[0]

def Fetch3():
        row7 = []
        try:
                
                db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Moisture FROM pa ORDER BY Time DESC")
                row7 = [int(item[0]) for item in cursor.fetchall()]

                print(row7)
        except Error as error:
                print(error)
        return row7[0]


def Fetch4():
        row8 = []
        try:
                
                db_config = {'password': '', 'host': 'localhost', 'user': 'root', 'database': 'dcc'}
                conn = MySQLConnection(**db_config)
                cursor = conn.cursor()
                cursor.execute("SELECT Humidity FROM pa ORDER BY Time DESC")
                row8 = [int(item[0]) for item in cursor.fetchall()]

                print(row8)
        except Error as error:
                print(error)
        return row8[0]


if __name__ == '__main__':
	Time()
	Temp_soil()
	Temp_atm()
	Moisture()
	Humidity()
	Fetch1()
