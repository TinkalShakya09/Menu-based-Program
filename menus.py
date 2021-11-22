import os
import time
import myfunction 

def service():
	os.system('espeak-ng -s 145 -v  en+f5 "Welcome Sir! I am Veronica. What can I do for you?"')


	while True:
		os.system("tput setaf 7")
		print("\t---------------------------------------------------------")
		os.system("tput setaf 14")
		print("\t\t\tWelcome to my Menu based program...",end="\n\n")
		os.system("tput setaf 7")
		print("\t---------------------------------------------------------")
		os.system("tput setaf 11")
		print("""\t\t\tPress 1 : To check today's date
		\tPress 2 : To know your ip
		\tPress 3 : To open firefox browser
		\tPress 4 : To setup the httpd webserver
		\tPress 5 : To search item using linear search
		\tPress 6 : To install Docker in your System
		\tpress 7 : To exit
		""")


		
		os.system("tput setaf 7")

		print("\t................................",end="\n\n")
		ch = int(input("Enter your choice here: "))

		if ch == 1:
			print("Today's date is..",end="\n\n")
			os.system('espeak-ng -s 145 -v  en+f5 "Todays date is"')
			os.system('zenity --height=200 --width=220 --info --text="$(date)"')
			


		elif ch == 2:
			os.system("tput setaf 10")
			print("This is info about your main ip..",end="\n\n")
			os.system("tput setaf 7")
			os.system("ifconfig enp0s3")
			os.system('espeak-ng -s 145 -v  en+f5 "This is info about your main ip"')

		elif ch == 3:
			print("Opening firefox..")
			os.system("firefox")

		elif ch == 4:
			os.system("yum install httpd")
			#copy file to /var/www/html
			os.system("systemctl start httpd")
			print("httpd server is being configured..")
			time.sleep(1)
			input("To check its status press ENTER...and after that press Q to exit")
			os.system("systemctl status httpd")

		elif int(ch) == 5:
			data= input("Provide your dataset here: ")
			d = data.split(",")
			item = input("Which item you want to search? ")
			myfunction.linear_search(d,item)

		elif int(ch) == 6:
			print("Installing Docker..")
			print()
			os.system("yum install -y yum-utils")
			os.system("yum-config-manager     --add-repo     https://download.docker.com/linux/centos/docker-ce.repo")
			os.system("yum install docker-ce -y")
			print()
			os.system("systemctl start docker")
			os.system("systemctl enable docker")
			print()
			print("Docker is now ready to use..")
			

		elif ch == 7:
			os.system("clear")
			print("Thankyou for visiting .....")
			exit()

		else:
			os.system("invalid option selected!")
		
		print()
		os.system("tput setaf 9")
		input("Press enter to continue..")
		os.system("clear")

