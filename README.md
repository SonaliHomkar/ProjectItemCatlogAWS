Project : Linux server configuration
======================================
This project is mainly intended to deploy Item Catlog application on Amazon Light sail server.
The application is installed start from creating virtual environment for python to apache server installation
and configuration.The newly added instance of light sail server is also added to the google console  for allowing
google id to access the application.


Prerequisites
============
1. Lightsail server
2. virtual environment for python
3. apache server
4. mode_wsgi
5. sqlalchemy
6. oauth2client
7. flask




Steps for creating new user on light server
============================================
1. sudo adduser new_user --disabled-password
2. sudo su new_user
3. cd
4. mkdir .ssh
5. chmod 700 .ssh
6. cd
7. touch .ssh/authorized_keys
8. chmod 600 .ssh/authorized_keys
9. On local server 
10. ssh-keygen
11. copy the public key on /home/testuser/.ssh/
12. sudo service ssh restart
13. ssh testuser@35.154.232.14 -i <filepath to private key>
14. Private key is attached to notes reviewer field

softwares installed
==================
	1. Have installed lightsail instance
	
	2. Install apache and mode_wsgi
	========================= 
	#sudo apt-get install apache2 
	#sudo apt-get install libapache2-mod-wsgi

	3. Clone the project
	==================
	#cd /usr/share
	#sudo git clone https://github.com/SonaliHomkar/ProjectItemCatlogAWS
	#cd ProjectItemCatlogAWS

	4. rename the directory as ProjectItemCatlog
	# mv ProjectItemCatlogAWS ProjectItemCatlog

	5. Move the directory ItemCatlogData to /usr/share.It contains ItemCatlog.db and client_secrets.json file
	# mv ProjectItemCatlog/ItemCatlogData ItemCatlogData

	6. Create Virtualenv
	====================
	#sudo pip3 install virtualenv
	# virtualenv venv
	#source venv/bin/activate
	#sudo pip install -r requirements.txt

	7. requirements.txt contains following packages 	

		1. sqlalchemy
		2. oauth2client
		3. flask
	8. Create wsgi file
	==================
	#sudo mkdir wsgi
	#cd wsgi
	#sudo vim ItemCatlog.wsgi
	

	import os
	import sys

	activatethis = "/usr/share/ProjectItemCatlog/venv/bin/activate_this.py"

	with open(activatethis) as f:
    	exec(f.read(), dict(__file__=activatethis))

	sys.stdout = sys.stderr

	sys.path.insert(0, os.path.join(
    			os.path.dirname(os.path.realpath(__file__)), '../..'))

	sys.path.append('/usr/share/ProjectItemCatlog/')
	print(sys.path)

	from ProjectItemCatlog.ItemCatlog import app as application


	9.Apache Settings
	=================

	#cd /etc/apache2/conf-enabled
	#sudo vim ItemCatlog.conf 

	WSGIScriptAlias / /usr/share/ProjectItemCatlog/wsgi/ItemCatlog.wsgi
	WSGIScriptReloading On
 
	Directory /usr/share/ProjectItemCatlog/wsgi>
  	    Order allow,deny
            Allow from all
        Directory>

	10. vim /etc/apache2/apache2.conf
	#Include generic snippets of statements. 
	#Following line should be there
	IncludeOptional conf-enabled/*.conf



	11. Restart apache
	===============
	#sudo service apache2 restart

	verify if the application is installed properly using following link
	http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com/

Getting Started
==============
1. IP address to access the server : 35.154.232.14
2. ssh port : use default port no need to specify the port
3. on your test the testuser with the defult port and private key in notes to reviewer field
4. ssh testuser@35.154.232.14 -v (filepath to private key)
5. Url for website : http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com/


Running the tests
========================
1. http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com
2. It will open the login Page. The user can log in using his gmail id or application's user Id
3. User can create his own userId using link New User sign up form
4. Once he successfully creates his user Id he can login with his credentials.
5. After login user is able to see home page where all the categories are listed with
   few list of item which are created recently
6. When the user clicks on category it displays list of items created under that category.
7. When the user clicks on item it displays detailed information about the item
8. If the user has created the item then only he can see the Edit and delete button on the screen.
9. If the user clicks on Edit button the form opens in edit mode and user can edit the item details.
10. If the user cllicks on Delete button it displays a screen to confirm the deletion and when clicked submit button
    he is allowed to delete the items
11. All the screens are validating madatory fields.
12. Please type URL http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com/ItemCatlog/JSON to display the Categorywise Item list  in JSON format
13. A logout button is displayed on all the screens to logout the user at any point of time
14. Apart from the required functionality user is allowed to edit category 
using URL http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com/<int:cat_id>/EditItem/
15. Also the user is allowed to delete category 
using URL http://ec2-35-154-232-14.ap-south-1.compute.amazonaws.com/<int:cat_id>/DeleteItem/



	
