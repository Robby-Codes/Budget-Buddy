import pickle
import datetime


permission = input('Are you sure you would like to Factory Reset your Budget Buddy?\nDoing so will delete your Budget Buddy account. Y / N : ')

improper_input = False

while True:
    if improper_input:
        permission = input('\nImproper Input. Enter either a capital Y for yes or capital N for No.\nAre you sure you would like to Factory Reset your Budget Buddy?\nDoing so will delete your Budget Buddy account. Y / N : ')
    if permission == 'N':
        break
    elif permission == 'Y':
        Budget_Data = pickle.load(open('storage.dat', 'rb'))
        today = datetime.date.today()
        month = today.strftime('%d')
        Budget_Data = {
            'security': [' ', '      '],
            'transaction': {
                'earnedvsspend': '0',
                'amount': '0',
                'category': '0'
            },
            'history': {
                'months': ['x', month,],
                'm_saved': ['0.00', '0',],
                'm_spent': ['x', '0',],
                'm_income': ['x', '0',],
            },
            'current': ['Test', 'Test', 'New'],
            'income': 0,
            'Test': {
                'Test': {
                    'Budget_Data': {
                        'FreeToUse': ['0', '0'],
                        'Utilities': ['0', '0'],
                        'Groceries': ['0', '0'],
                        'Internet': ['0', '0'],
                        'CellPhone': ['0', '0'],
                        'Gas': ['0', '0'],
                        'Rent': ['0', '0'],
                        'BankAccount': ['0', '0'],
                        'CarInsurance': ['0', '0'],
                        'HealthInsurance': ['0', '0'],
                        'Other': ['0', '0'],
                    }
                }
            }
        }
        pickle.dump(Budget_Data, open('storage.dat', 'wb'))
        print('\n\nFactory Reset Completed! Your Budget Buddy account has been deleted!')
        break
    else:
        improper_input = True
