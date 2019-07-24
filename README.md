# test_rest_2
Django backend for the IUCAA Project

Following steps to be followed in order to launch respective modules.

	# Start Spider Crawl
		
		-> scrapy crawl spidey
	
	# Start Apache LAMPP / MySQL Server
		
		-> sudo /opt/lampp/lampp start
		
	# Start Django Backend Web Service

		-> python3 manage.py makemigrations 
		-> python3 manage.py migrate
		-> python3 manage.py runserver     ip adress:port no          Eg. 192.168.43.12:8000
