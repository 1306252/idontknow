# This program assists a technician in thre process of checking a substance's temperatuer
# Set Maximum temperature(100)
max_tem = 100
# Get the substance's temperature
substance_tem = float(input("Enter the substance's temperature: "))

# As long as necessary, give instruct the user to adjust the temrmostat. If the temperature is too high(Max temp >)and less than 5 mins, display the message 
while substance_tem > max_tem:
    print("Turn the thrtmostat down and wait 5 mins")
    
    print("Then take the temperature again and enter it")
    substance_tem = int(input("The current temperature:"))


print("All temperature is in normal parameter")

   
# If the temperature is too high (max tem>) and less than 5 mins display the message
    #Instruction is display the following message
    #Turn the thrtmostat down and wait 5 mins
    #Then take the temperature again and enter it
    #Ask the current temperature
# Display"All temperature is in normal parameter"





