
def mistake():
	return "I'm sorry!\nSomething went wrong!"

def start_database(db_host, db_user, db_pass):
	try:
		import mysql.connector as mysql
		db_connection = mysql.connect(host="{}".format(db_host),user="{}".format(db_user),passwd="{}".format(db_pass))
		db_cursor = db_connection.cursor()
		print("Creating Database!")
		db_cursor.execute("create database mailbox;use mailbox;create table texts(post_id int primary key auto_increment,name varchar(30),content varchar(1000));")
		db_connection.commit()
	except Exception as e:
		err = mistake()
		print(err)

def posting(db_host, db_user, db_pass):
	try:	
		import mysql.connector as mysql
		one = [1, '1', "one", "One"]
		two = [2, '2', "two", "Two"]
		three = [3, '3', "three", 'Three']
		db_connection = mysql.connect(host="{}".format(db_host),user="{}".format(db_user),passwd="{}".format(db_pass),database='mailbox')
		db_cursor = db_connection.cursor()
		
		que = input("Choose one to continue!\ntype 1 > to post\ntype 2 > to see posts\ntype 3 > to quit\n>>> ")
		while que not in one and que not in two and que not in three:
			que = input("Choose one to continue!\ntype 1 > to post\ntype 2 > to see posts\ntype 3 > to quit\n>>> ")

		if que in one:
			name = input("Enter your name -> ")
			some_texts = input("What's happening in your feeling? (Enter to post)\n")
			if name == "":
				name = 'Null'
			if some_texts == "":
				some_texts = 'Null'
			db_cursor.execute("insert into texts(name,content) value('{0}','{1}')".format(name, some_texts))
			db_connection.commit()

		if que in two:
			print("Posts")
			db_cursor.execute("select * from texts;")
			for data in db_cursor:
				print(data)

		if que in three:
			import sys
			print("Deleting all the data!")
			delete(db_host, db_user, db_pass)
			print("Bye Bye!")
			sys.exit()

	except Exception as e:
		err = mistake()
		print(err)

def delete(db_host, db_user, db_pass):
	try:	
		import mysql.connector as mysql
		db_connection = mysql.connect(host="{}".format(db_host),user="{}".format(db_user),passwd="{}".format(db_pass),database='mailbox')
		db_cursor = db_connection.cursor()
		db_cursor.execute("drop database mailbox;")
	except Exception as e:
		err = mistake()
		print(err)

def main_task():
	try:	
		print("Welcome to Mailbox")
		v="Please, enter the valid input -> "
		numbers=[1,2,3,4,5,6,7,8,9,0]
		yes_ans = ['y','Y','Yes','yes']
		no_ans = ['n','N','No','no']
		question = input("Have you already done the installation? [y/n] -> ")
		while question not in yes_ans and question not in no_ans:
			question = input(v)
		if question in no_ans: first_step()
		#question = input("Have you already created the database? [y/n] -> ")
		#while question not in yes_ans and question not in no_ans:
		#	question = input(v)
		db_host = input("Please enter your database host! Default[localhost]\n-> ")
		if db_host == "":
			db_host = 'localhost'
		db_user = input("Please enter your database user! Default[root]\n-> ")
		if db_user == "":
			db_user = 'root'
		db_pass = input("Please enter your database password! Default[blank]\n-> ")
		if db_pass == "":
			db_pass = ""
		#if question in no_ans: 
		start_database(db_host, db_user, db_pass)
		while True:
			print("Welcome to Newfeed!")
			posting(db_host, db_user, db_pass)
	except Exception as e:
		err = mistake()
		print(err)

def first_step():
	try:
		import os
		v="Please, enter the valid input -> "
		numbers=[1,2,3,4,5,6,7,8,9,0]
		yes_ans = ['y','Y','Yes','yes']
		no_ans = ['n','N','No','no']

		first_question = input("Have you already installed mysql-server? [y/n] -> ")
		while first_question not in yes_ans and first_question not in no_ans:
			first_question = input(v)
		if first_question in no_ans:
			os.system("sudo apt-get install mysql-server")

		second_question = input("Have you already started the mysql-server? [y/n] -> ")
		while second_question not in yes_ans and second_question not in no_ans:
			second_question = input(v)
		if second_question in no_ans:
			os.system("sudo service mysql start")

		third_question = input("Have you already installed python module to connect mysql-server? [y/n] -> ")
		while third_question not in yes_ans and third_question not in no_ans:
			third_question == input(v)
		if third_question in no_ans:
			os.system('pip3 install mysql.connector')
		
	except Exception as e:
		err = mistake()
		print(err)
'''
try:
	while True: main_task()
except Exception as e:
	print(mistake())
	#print(e)
'''
