
import os
import subprocess as sp


def machineLearning():
	while True:
		os.system("tput setaf 7")
		print("\t---------------------------------------------------------")
		os.system("tput setaf 14")
		print("\t\t\tWelcome to Machine Learning World")
		os.system("tput setaf 7")
		print("\t---------------------------------------------------------")
		os.system("tput setaf 11")
		print("""\tWhich voice you like male voice or female Voice  
			 \tPress 1 : Salary Predict using Linear Regression
			 \tPress 2 : MultiLinear Regression
			 \tPress 3 : Logistic Regression
			 \tPress 4 : To exit
		 
			""")
		os.system("tput setaf 7")
		print("................................",end="\n\n")
		cmd=int(input("what you want voice  : "))
		 

		if cmd==1:
			print("Salary Predict using Linear Regression \n \t In this program, we have predict the salary")
			year=input("Enter the year of Experience :")
			os.system("docker run -it tinkalshakya/ml_salary_predict:v1 {}".format(year))
			

		elif cmd==2:
			print("MultiLinear Regression")

		elif cmd==3:
			print("Logistic Regression")
			
		elif cmd==4:
			os.system("clear")
			print("Thankyou..............")			
			exit()
		else:
			print("Invalid Key! Try again")

		print()
		os.system("tput setaf 9")
		input("Press enter to continue..")
		os.system("clear")


