# CS361-Microservice
Microservice for a bills and roommates project. 

Communication contract:

To REQUEST data from microservice, follow these steps:

   Prepare the Input File:
  		Create or use a text file named 'bills_data.txt'. Ensure the file is empty before starting.
       
  Enter Data:
		Write the following in the file, using a comma to separate the values: (NOTE: The comma is absolutely necessary for the microservice to function).
          Number of roommates
          Total bill amount
          
  Example: 
      * 5,9350 (for 5 roommates and a total bill of 9350) 
      * Spaces like 5, 9350 are allowed; the microservice ignores them.
      
  Save and Close:
      Overwrite any existing content with your new data and save the file.
  
  Example call:
  "billsData = open("bills_data.txt", "w")
  billsData.write(str(total_roomies) +","+ str(total_bills))"

To RECEIVE data from microservice, follow these steps:

  Open the File:
      Open the same bills_data.txt file used for the request.
      
  Check the Content:
      If the file contains a single value, this is the calculated result from the microservice.
      
  Retrieve the Result:
      Copy the value from the file into a variable in your program.
      
  Example call: 
      information = billsData.readline()
      if ',' not in information...
        
# UML sequence diagram:
<img width="963" alt="Screenshot 2024-11-16 at 7 03 27 PM" src="https://github.com/user-attachments/assets/27331dac-7067-48d9-a964-1565d6acc449">
