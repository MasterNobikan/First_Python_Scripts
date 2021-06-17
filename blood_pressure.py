''' Blood pressure reading compared to chart
ask for systolic and diastolic
Display one of following results:
Low
Normal
PreHypertension
High: Stage 1 Hypertension
High: Stage 2 Hypertension
--Use chart

--Use a funct that takes number and a string('sys' or 'dia')
    and returns a string as a result
'''

def bp(reading, kind):
    if kind == 'sys':
        if 40 < reading <= 90:
            return 'Low'
        elif 90 < reading <=120:
            return 'Normal'
        elif 120 < reading <= 140:
            return 'Prehypertension'
        elif 140 < reading <=160:
            return 'High: Stage 1 Hypertension'
        elif 160 < reading:
            return 'High: Stage 2 Hypertension'
        else:
            return 'You are dead, dead, dead....'
    else:
        if 40 < reading <= 60:
            return 'Low'
        elif 60 < reading <=80:
            return 'Normal'
        elif 80 < reading <= 90:
            return 'Prehypertension'
        elif 90 < reading <=100:
            return 'High: Stage 1 Hypertension'
        elif 100 < reading:
            return 'High: Stage 2 Hypertension'
        else:
            return 'You are dead, dead, dead....'


def main():
    #take input from user
    systol = int(input('Enter your systolic reading: '))
    diatol = int(input('Enter your diastolic reading: '))

    # display result
    print('Your systolic result:', bp(systol, 'sys'))
    print('Your diastolic result:', bp(diatol, 'dia'))

main()
    
