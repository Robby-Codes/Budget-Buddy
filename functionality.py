import pickle
import re


def new_account(name, password, email):
    if (re.match(r'^[a-zA-Z]+$', name) and
            re.match(r'^[a-zA-Z1-9]+$', password) and
            re.match(r'^[a-zA-Z1-9]+@[a-zA-Z1-9]+\.[a-z]+$', email)):
        account = {
            name: {
                password: {
                    'Budget_Data': {
                        'FreeToUse': [0, 0],
                        'Utilities': [0, 0],
                        'Groceries': [0, 0],
                        'Internet': [0, 0],
                        'CellPhone': [0, 0],
                        'Gas': [0, 0],
                        'Rent': [0, 0],
                        'BankAccount': [0, 0],
                        'CarInsurance': [0, 0],
                        'HealthInsurance': [0, 0],
                        'Other': [0, 0],
                    }
                }
            }
        }
        pickle.dump(account, open('storage.dat', 'wb'))
    else:
        return False


def log_in(name, password):
    Budget_Data = pickle.load(open('storage.dat', 'rb'))
    if name in Budget_Data:
        if password in Budget_Data[name]:
            current_user = name
            current_password = password
            pickle.dump(Budget_Data, open('storage.dat', 'wb'))
            return True
        else:
            return False
    else: 
        return False


def new_budget_check(category, budget):
    if re.match(r'^-?[0-9]+\.?[0-9]*$', budget):
        Budget_Data = pickle.load(open('storage.dat', 'rb'))
        Budget_Data[category][0] = budget
        pickle.dump(Budget_Data, open('storage.dat', 'wb'))
        return True
    else:
        return False


def remember_budget(user, category):
    Budget_Data = pickle.load(open('storage.dat', 'rb'))
    return Budget_Data[]
