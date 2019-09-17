import datetime
import matplotlib.pyplot as plt
import pickle
import re


def new_account(name, password, email):
    if (re.match(r'^([a-zA-Z]| )+$', name) and
            re.match(r'^([a-zA-Z1-9]|\!|@|#|\$|%|\^|\&|\*)+$', password) and
            re.match(r'^[a-zA-Z1-9]+@[a-zA-Z1-9]+\.[a-z]+$', email)):
        Budget_Data = pickle.load(open('storage.dat', 'rb'))
        Budget_Data = {
            'income': 1000,
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


def date_range():
    today = datetime.date.today()
    the_first = today.strftime('%B 1, %Y')
    today = today.strftime('%B %d, %Y')
    return the_first + '  -  ' + today


def find_income():
    data = pickle.load(open('storage.dat', 'rb'))
    return str(data['income'])


def calc_savings_spending(bar):
    data = pickle.load(open('storage.dat', 'rb'))
    name = data['current'][0]
    passw = data['current'][1]
    income = data['income']
    spending = eval(
        data[name][passw]['Budget_Data']['FreeToUse'][0]
        + '+' + data[name][passw]['Budget_Data']['Utilities'][0]
        + '+' + data[name][passw]['Budget_Data']['Groceries'][0]
        + '+' + data[name][passw]['Budget_Data']['Internet'][0]
        + '+' + data[name][passw]['Budget_Data']['CellPhone'][0]
        + '+' + data[name][passw]['Budget_Data']['Gas'][0]
        + '+' + data[name][passw]['Budget_Data']['Rent'][0]
        + '+' + data[name][passw]['Budget_Data']['BankAccount'][0]
        + '+' + data[name][passw]['Budget_Data']['CarInsurance'][0]
        + '+' + data[name][passw]['Budget_Data']['HealthInsurance'][0]
        + '+' + data[name][passw]['Budget_Data']['Other'][0]
    )
    if bar == 'spending':
        return str(spending)
    elif bar == 'savings':
        return str(income - spending)


def find_spending(category, type_):
    data = pickle.load(open('storage.dat', 'rb'))
    name = data['current'][0]
    passw = data['current'][1]
    had = data['income']
    spent = data[name][passw]['Budget_Data'][category][0]
    if type_ == 'percent':
        return str(((had - (had - eval(spent))) / had) * 100)
    if type_ == 'whole':
        return str(had - (had - eval(spent)))

