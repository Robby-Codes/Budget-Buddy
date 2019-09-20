import datetime
import pickle
import re


def new_account(name, password, email):
    if (re.match(r'^([a-zA-Z]| )+$', name) and
            re.match(r'^([a-zA-Z1-9]|\!|@|#|\$|%|\^|\&|\*)+$', password) and
            re.match(r'^[a-zA-Z1-9]+@[a-zA-Z1-9]+\.[a-z]+$', email)):
        Budget_Data = pickle.load(open('storage.dat', 'rb'))
        Budget_Data = {
            'income': 0,
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


def remember_spending(category):
    remember = pickle.load(open('storage.dat', 'rb'))
    current_name = remember['current'][0]
    current_pass = remember['current'][1]
    return remember[current_name][current_pass]['Budget_Data'][category][1]


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
        data[name][passw]['Budget_Data']['FreeToUse'][1]
        + '+' + data[name][passw]['Budget_Data']['Utilities'][1]
        + '+' + data[name][passw]['Budget_Data']['Groceries'][1]
        + '+' + data[name][passw]['Budget_Data']['Internet'][1]
        + '+' + data[name][passw]['Budget_Data']['CellPhone'][1]
        + '+' + data[name][passw]['Budget_Data']['Gas'][1]
        + '+' + data[name][passw]['Budget_Data']['Rent'][1]
        + '+' + data[name][passw]['Budget_Data']['BankAccount'][1]
        + '+' + data[name][passw]['Budget_Data']['CarInsurance'][1]
        + '+' + data[name][passw]['Budget_Data']['HealthInsurance'][1]
        + '+' + data[name][passw]['Budget_Data']['Other'][1]
    )
    if bar == 'spending':
        return str(round(spending, 2))
    elif bar == 'savings':
        return str(round(income - spending, 2))


def find_spending(category, type_):
    data = pickle.load(open('storage.dat', 'rb'))
    name = data['current'][0]
    passw = data['current'][1]
    had = data['income']
    spent = data[name][passw]['Budget_Data'][category][1]
    if type_ == 'percent':
        try:
            t_spent = eval(calc_savings_spending('spending'))
            percentage = (((t_spent - (t_spent - eval(spent))) / t_spent) * 100)
            percentage = round(percentage, 2)
            return str(percentage)
        except ZeroDivisionError:
            return '0'
    if type_ == 'whole':
        spending = had - (had - eval(spent))
        spending = round(spending, 2)
        return str(spending)


def earn_or_spend(choose):
    data = pickle.load(open('storage.dat', 'rb'))
    data['transaction']['earnedvsspent'] = choose
    pickle.dump(data, open('storage.dat', 'wb'))


def new_amount(amount):
    data = pickle.load(open('storage.dat', 'rb'))
    data['transaction']['amount'] = amount
    pickle.dump(data, open('storage.dat', 'wb'))


def transaction_type(category):
    data = pickle.load(open('storage.dat', 'rb'))
    data['transaction']['category'] = category
    pickle.dump(data, open('storage.dat', 'wb'))


def log_it():
    data = pickle.load(open('storage.dat', 'rb'))
    if data['transaction']['earnedvsspent'] == 'spent':
        name = data['current'][0]
        passw = data['current'][1]
        category = data['transaction']['category']
        amount = data['transaction']['amount']
        spending = data[name][passw]['Budget_Data'][category][1]
        new = eval(amount) + eval(spending)
        data[name][passw]['Budget_Data'][category][1] = str(new)
        pickle.dump(data, open('storage.dat', 'wb'))
        return str(new)
    if data['transaction']['earnedvsspent'] == 'earned':
        amount = data['transaction']['amount']
        income = data['income']
        data['income'] = eval(amount) + eval(income)
        pickle.dump(data, open('storage.dat', 'wb'))
        return None


def choose_category():
    data = pickle.load(open('storage.dat', 'rb'))
    return data['transaction']['category']


def clean_transaction():
    data = pickle.load(open('storage.dat', 'rb'))
    data['transaction']['earnedvsspend'] = '0'
    data['transaction']['amount'] = '0'
    data['transaction']['category'] = '0'
    pickle.dump(data, open('storage.dat', 'wb'))
