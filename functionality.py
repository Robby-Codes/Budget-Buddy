import pickle
import re


def new_account(name, password, email):
    if (re.match(r'^([a-zA-Z]| )+$', name) and
            re.match(r'^([a-zA-Z1-9]|\!|@|#|\$|%|\^|\&|\*)+$', password) and
            re.match(r'^[a-zA-Z1-9]+@[a-zA-Z1-9]+\.[a-z]+$', email)):
        Budget_Data = pickle.load(open('storage.dat', 'rb'))
        Budget_Data = {
            name: {
                password: {
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
        return True
    else:
        return False


def log_in(name, password):
    Budget_Data = pickle.load(open('storage.dat', 'rb'))
    if name in Budget_Data:
        if password in Budget_Data[name]:
            Budget_Data['current'] = [name, password]
            pickle.dump(Budget_Data, open('storage.dat', 'wb'))
            return True
        else:
            return False
    else:
        return False


def new_budget_check(category, budget):
    if re.match(r'^-?[0-9]+\.?[0-9]*$', budget):
        update = pickle.load(open('storage.dat', 'rb'))
        current_name = update['current'][0]
        current_pass = update['current'][1]
        update[current_name][current_pass]['Budget_Data'][category][0] = budget
        pickle.dump(update, open('storage.dat', 'wb'))
        return True
    else:
        return False


def remember_budget(category):
    remember = pickle.load(open('storage.dat', 'rb'))
    current_name = remember['current'][0]
    current_pass = remember['current'][1]
    return remember[current_name][current_pass]['Budget_Data'][category][0]
