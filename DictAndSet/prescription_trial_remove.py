from prescription_data_remove_method import *
import random

sample_patients = set()
max_patients = 6
while len(sample_patients) < 4:
    getno = random.randint(1,max_patients)
    print(getno)
    sample_patients.add(list(dict.fromkeys(patients))[getno])
    print(sample_patients)

#remove warfarin and replace with edoxaban for trial patients if they are taking it

for patient in sample_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f'patient {patient} is not taking warfarin')
    print(f'{patient} is now taking {patients[patient]}')