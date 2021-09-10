def info_input():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    return diagnosis, weight_input

def calculations(diagnosis, weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return weight, dosage_mg_first_day
    #can further modularize it by making a unit conversion function in which convert btw lb and kg

def data_output(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


def program_driver():
    diag, w_input = info_input()
    wt, dose_1 = calculations(diag, w_input)
    data_output(wt, dose_1)
    

if __name__ == '__main__':
    program_driver()
    #diag, w_input = info_input()
    #wt, dose_1 = calculations(diag, w_input)
    #data_output(wt, dose_1)
    #this part is driver part of the code, drives the function bc it needs to do each one of these things
    #thus prob best to put in own function