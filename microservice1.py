# Isac Polasak"
# CS 361
# Microservice 1 for Jazzmyne's project.
import time
while True:
    time.sleep(2)
    billsData = open("bills_data.txt", "r")
    information = billsData.readline()  # 'information' now contains the first line in the bills_data.txt file.
    billsData.close()                   # Close the file for reading, we'll write in it after.

    if information.strip():
        # If there's data, it will remove any spaces w/ no space, and it will split the data wherever there's a comma
        # into two lines, so values will now contain a list of both values.
        values = information.replace(" ", "").split(",")
        if len(values) == 2:
            print("Receiving data from main program.")
            # if there are 2 vals, it's precalculation, so do the calculations.
            total_price = int(values[1])
            total_roomies = int(values[0])
            if total_roomies == 0:
                print("There needs to be more than 1 roommate.")
            else:
                print(f"The total price owed this month is ${total_price}")
                print(f"and splitting that amongst {total_roomies} roommates leaves each roommate with a bill of ")
                per_roomie = total_price/total_roomies
                print(f"{per_roomie} for this month!")
                print("Sending information back to main program.")
                billsData = open("bills_data.txt", "w")
                billsData.write(str(per_roomie))
                billsData.close()

