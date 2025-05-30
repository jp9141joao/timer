import time
import os

def Start():
    os.system('cls')  # Clear the terminal screen (Windows)
    
    # Ask the user to input the timer duration
    TimeValue = int(input('\nEnter how long the timer will run: '))
    
    # Validate input: TimeValue should be between 0 and 60
    while TimeValue > 60 or TimeValue < 0:
        TimeValue = int(input('\nInvalid value!\nPlease enter another value!\nR: '))
    
    # Ask the user for the time unit
    Unit = str(input('\nThis value will be in\nH- Hours\nM- Minutes\nS- Seconds\nCS- Hundredths\nR: '))
    
    # Validate input: Unit must be one of the allowed options
    while Unit.lower() not in ('h', 'm', 's', 'cs'):
        Unit = str(input('\nInvalid option!\nPlease enter another option!\nR: '))
    
    # Initialize the timer variables based on the chosen unit
    if Unit.lower() == 'h':
        hh = TimeValue - 1
        mm = 59
        ss = 59
        cs = 9
    elif Unit.lower() == 'm':
        hh = 0
        mm = TimeValue - 1
        ss = 59
        cs = 9
    elif Unit.lower() == 's':
        hh = 0
        mm = 0
        ss = TimeValue - 1
        cs = 9
    else:  # 'cs' for hundredths
        hh = 0
        mm = 0
        ss = 0
        cs = TimeValue

    # Countdown loop: decrease from hh:mm:ss:cs down to 00:00:00:0
    for i in range(hh, -1, -1):
        for j in range(mm, -1, -1):
            for k in range(ss, -1, -1):
                for l in range(cs, -1, -1):
                    os.system('cls')  # Clear the screen before printing the updated timer
                    print('hh:mm:ss:cs')
                    print(f'{i:02d}:{j:02d}:{k:02d}:{l:1d}')  # Print formatted timer
                    time.sleep(0.1)  # Wait 0.1 seconds (100 milliseconds)

    # After countdown finishes, ask user to enter "1" to return to menu
    ReturnToMenu = int(input('\nEnter "1" to return\nR: '))
    while ReturnToMenu != 1:
        ReturnToMenu = int(input('\nInvalid option!\nEnter "1" to return\nR: '))

# Main program loop
while True:
    os.system('cls')  # Clear screen

    # Display menu and ask for choice
    MenuOption = int(input(f'\n* Menu *\n1- Start\n2- Exit\nR: '))
    
    # Validate menu choice
    while MenuOption not in (1, 2):
        MenuOption = int(input('\n* Menu *\nInvalid option!\n1- Start\n2- Exit\nR: '))
    
    # Execute choice
    if MenuOption == 1:
        Start()
    else:
        print('\nProgram finished!')
        break
