# registration_mail
When a user registers on the website with his details, an acceptance email needs to be sent to the user with a pdf document. The pdf document contains the details of the user.

I am assuming you have python and pip already installed on your system.

1. To build this project make sure you have mysql installed on your system

To install mysql 

(mac users)
$ brew install mysql 

(linux users)
$ sudo apt-get update 					
$ sudo apt-get install mysql-server

Replace the 'root' and 'password' in database_pdf.py file with your mysql username and password.

2. Install the pymysql library to work with mysql using python

$pip install pymysql

3. Install fpdf library to use and create pdf in python

$pip install fpdf

Now you are all set to work.
