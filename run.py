import os,sys,mysql.connector

situation = True
no = ['n','N','no','No','nO','NO']

print("Hello, welcome to the feed")
print("In this feed, we all have to do is to control the post")

def escape():
    sys.exit()

def start_server(username,password):
    os.system("sudo service mysql start")
    os.system("sudo mysql -u {0} -p {1}".format(username,password))

def create_db(username,password,localhost='localhost'):
    try:
        db_connect = mysql.connector.connect(
            host = hostname,
            user = username,
            passwd = password
        )

        db_cursor = db_connect.cursor()
        db_cursor.execute("create database newfeed;use newfeed;create table post(id int primary key auto_increment, text varchar(1000)")
        
    except Exception as e:
        print(e)
        print("It seems you aren't start the localhost server yet!\nDon't worry, I will handle this!")
        password = input('Could you please type your mysql password if there any?')
        start_server('localhost','root',password)
        
try:
    while situation:
        username = input('Please type your mysql user =>')
        i = 0
        while username=='':
            username = input('Mysql user can\'t be blank. Please enter the valid input ->')
            i += 1
            if i == 3:
                print("You enter the invaild input many times!")
                escape()
        
        password = input('Please enter the password =>')
        while password=='':
            password = input('Mysql password can\'t be blank. Please enter the valid input ->')
            i += 1
            if i == 3:
                print("You enter the invaild input many times!")
                escape()
        '''
        hostname = input('Enter the hosting server [By Default, it\' localhost] =>')
        while hostname=='':
            hostname = input('Mysql hosting server can\'t be blank. Please enter the valid input ->')
            i += 1
            if i == 3:
                print("You enter the invaild input many times!")
                escape()
        '''
        ques = input("Have you already started the localhost server? [y/N]\nBy default, it's 'no' ->")
        while ques=='':
            ques = input("You should answer this =>")
        if ques in no:
            print("The server will be started")
            start_server(username, password)
        else:
            print("Okay! I trust you.")



except Exception as e:
    print(e)
