Marital_Status = input(" Marital Status \n [Y for YES and N for NO] Enter: ")
Sex = input(" Sex [M for MALE and F for FEMALE] Enter: ")
Age = int(input(" Enter your Age: "))
if(Marital_Status=="Y") or((Marital_Status.upper()=="N") and (((Sex.upper()=="M") and (Age>30)) or ((Sex.upper()=="F") and (Age>25)))):
	print("Driver is insured !")
else:
	print("Driver is not insured !")