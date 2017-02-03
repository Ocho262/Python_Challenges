import sys

password = raw_input("What is the secret password?")

if password == "":
  sys.exit()
  

p_input = raw_input("Enter the secret password.")

if p_input == password:
  print("Hello there! ")
	
else:
   print("Who are you? I don't know you! ") 
