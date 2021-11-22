	
import os
import ml
import menus
import espeaktool

def docker():
	os.system("tput setaf 7")
	print("\t---------------------------------------------------------")
	
	os.system("tput setaf 14")
	print("\t\t\tWelcome to Docker World")
	os.system("tput setaf 7")
	print("\t---------------------------------------------------------")
	os.system("tput setaf 11")
	print("""\t Choose the options what you want
         \tPress 1 : Show the all Docker images
	 \tPress 2 : Pull the images from registry
	 \tPress 3 : List the all running containers
	 \tPress 4 : Run the docker Image in a new Container
	 \tPress 5 : Create own docker image
	 \tPress 6 : remove the containers
	 \tPress 7 : remove the images
	 \tPress 8 : upload/push the created image on Docker Hub
	 \tPress 9 : To exit the program
         """)
	os.system("tput setaf 7")

	print("\t................................",end="\n\n")
	doc = int(input("Enter the key what do you want to do: "))

	while True:
	
	
	
		if(doc==1):
			os.system("docker_img")
		elif(doc==2):
			os.system("docker_pull")
		elif(doc==3):
			os.system("docker_con")
		elif(doc==4):
			os.system("docker_run")
		elif(doc==5):
			os.system("docker_cimg")
		elif(doc==6):
			os.system("docker_rmc")
		elif(doc==7):
			os.system("docker_rmi")
		elif(doc==8):
			os.system("docker_upload")
		elif(doc==9):
			os.system("clear")
			print("Thankyou for visiting .......")
			exit()
				
		else:
			print("Invalid Key! Try again")
		print()
		os.system("tput setaf 9")
		input("Press enter to continue..")
		os.system("clear")
		break

		


print("\t---------------------------------------------------------")
os.system("tput setaf 7")
os.system("tput setaf 14")
print("\t\t\tWelcome to My World")
os.system("tput setaf 7")
print("\t---------------------------------------------------------")
os.system("tput setaf 11")
print("""\tWhat do you like want to choose
	 \tPress 1 : Show some interesting things and also send the mail 
         \tPress 2 : Setup Services And basic commands
         \tPress 3 : Docker 
	 \tPress 4 : Machine Learning
	 \tPress 5 : To exit 
         
""")
os.system("tput setaf 7")
print("\t................................",end="\n\n")
cmd=int(input("what you want : "))

while True:
	
	 
	if cmd==1:
		espeaktool.espeak()
	elif cmd==2:
		menus.service()

	elif cmd==3:
		docker()
		
	elif cmd==4:
		ml.machineLearning()			
		
	elif cmd==5:	
		os.system("clear")
		print("Thankyou for visiting .......")		
		exit()
	else:
		print("Invaid Key try again")
	


