import datetime
import pickle
import re


def check_input(word=None, num=None):
    if num is not None:
        if (re.match(r'^[0-9]*\.?[0-9]{0,2}$', num) and not
            re.match(r'^0[0-9]+', num)):
            return True
        else:
            return False
    if word is not None:
        if re.match(r'^[a-zA-Z0-9!@#\$%\^\&\*]+$', word):
            return True
        else:
            return False


def check_account():
    data = pickle.load(open('storage.dat', 'rb'))
    if 'New' in data['current']:
        return True
    else:
        return False


def new_security(question, answer):
    data = pickle.load(open('storage.dat', 'rb'))
    data['security'] = [question, answer]
    pickle.dump(data, open('storage.dat', 'wb'))


def remember_security():
    data = pickle.load(open('storage.dat', 'rb'))
    question = data['security'][0]
    if len(question) >= 25:
        if len(question) >= 40:
            question1 = question[0:len(question)//2]
            question2 = question[len(question)//2:(len(question)//2) * 2]
            question3 = question[(len(question)//2) * 2:]
            return question1 + '\n' + question2 + '\n' + question3
        else:
            question1 = question[0:len(question)//2]
            question2 = question[len(question)//2:]
            return question1 + '\n' + question2
    else:
        return question


def check_security_answer(input_):
    data = pickle.load(open('storage.dat', 'rb'))
    answer = data['security'][1]
    if input_ == answer:
        return True
    else: 
        return False


def recover_account():
    data = pickle.load(open('storage.dat', 'rb'))
    username = data['current'][0]
    password = data['current'][1]
    return 'Username: ' + str(username) + '\n\nPassword: ' + str(password)


def new_account():
    Budget_Data = pickle.load(open('storage.dat', 'rb'))
    name = Budget_Data['current'][0]
    password = Budget_Data['current'][1]
    today = datetime.date.today()
    month = today.strftime('%d')
    Budget_Data = {
        'transaction': {
            'earnedvsspend': '0',
            'amount': '0',
            'category': '0'
        },
        'history': {
            'months': ['x',],
            'm_saved': ['0.00',],
            'm_spent': ['x',],
            'm_income': ['x',],
        },
        'current': [name, password],
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
    update_history()
    return True


def log_in(name, password):
    Budget_Data = pickle.load(open('storage.dat', 'rb'))
    if 'New' in Budget_Data['current']:
        Budget_Data['current'] = [name, password, 'New']
        pickle.dump(Budget_Data, open('storage.dat', 'wb'))
    else:
        if name in Budget_Data:
            if password in Budget_Data[name]:
                return True
            else:
                return False
        else:
            return False


def add_commas(num):
    sign = True if '$' in num else False
    if '$' in num:
        num = num.replace('$', '')
    neg = True if '-' in num else False
    if '-' in num:
        num = num.replace('-', '')
    if '.' in num:
        num = num.split('.')
        main_num = num[0]
        if len(main_num) <= 3:
            result = '.'.join(num)
        elif len(main_num) > 3 and len(main_num) < 7:
            main_num = list(main_num)
            main_num.insert(-3, ',')
            result = ''.join(main_num) + '.' + num[1]
        elif len(main_num) > 6:
            main_num = list(main_num)
            main_num.insert(-3, ',')
            main_num.insert(-7, ',')
            result = ''.join(main_num) + '.' + num[1]
    else:
        if len(num) <= 3:
            result = num
        elif len(num) > 3 and len(num) < 7:
            num = list(num)
            num.insert(-3, ',')
            result = ''.join(num)
        elif len(num) > 6:
            num = list(num)
            num.insert(-3, ',')
            num.insert(-7, ',')
            result = ''.join(num)
    if neg and not sign:
        return '-' + result
    if sign and not neg:
        return '$' + result
    if sign and neg:
        return '$-' + result
    if not neg and not sign:
        return result


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
    if check_month():
        return "0"
    else:
        current_name = remember['current'][0]
        current_pass = remember['current'][1]
        return remember[current_name][current_pass]['Budget_Data'][category][0]


def remember_spending(category):
    remember = pickle.load(open('storage.dat', 'rb'))
    if check_month():
        return '0'
    else:
        current_name = remember['current'][0]
        current_pass = remember['current'][1]
        return remember[current_name][current_pass]['Budget_Data'][category][1]


def date_range():
    today = datetime.date.today()
    the_first = today.strftime('%B 1, %Y')
    today = today.strftime('%B %d, %Y')
    return the_first + '  -  ' + today


def find_income():
    if check_month():
        return '0'
    else:
        data = pickle.load(open('storage.dat', 'rb'))
        return str(data['income'])


def calc_savings_spending(bar):
    if check_month():
        return '0'
    else:
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


def estimated_savings():
    data = pickle.load(open('storage.dat', 'rb'))
    if check_month():
        return '0'
    else:
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
        return str(round(income - spending, 2))


def estimated_savings_color():
    if '-' in str(estimated_savings()):
        return (1, 0, 0, 1)
    else:
        return (1, 1, 1, 1)


def estimated_total_savings(savings):
    if '-' in savings:
        return (1, 0, 0, 1)
    else:
        return (0, 0.5, 0, 1)


def find_spending(category, type_):
    if check_month():
        return '0'
    else:
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


def user_earned():
    data = pickle.load(open('storage.dat', 'rb'))
    reveal = data['transaction']['earnedvsspent']
    if reveal == 'earned':
        return True
    if reveal == 'spent':
        return False


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


def new_income():
    data = pickle.load(open('storage.dat', 'rb'))
    if data['transaction']['earnedvsspent'] == 'earned':
        amount = data['transaction']['amount']
        income = data['income']
        amount = eval(amount)
        income = income
        new_income = amount + income
        data['income'] = new_income
        pickle.dump(data, open('storage.dat', 'wb'))


def choose_category():
    data = pickle.load(open('storage.dat', 'rb'))
    return data['transaction']['category']


def clean_transaction():
    data = pickle.load(open('storage.dat', 'rb'))
    data['transaction']['earnedvsspend'] = '0'
    data['transaction']['amount'] = '0'
    data['transaction']['category'] = '0'
    pickle.dump(data, open('storage.dat', 'wb'))


def remember_color(category):
    if eval(remember_spending(category)) > eval(remember_budget(category)):
        return (1, 0, 0, 1)
    else:
        return (0, 0, 0, 1)


def reset_for_new_month():
    data = pickle.load(open('storage.dat', 'rb'))
    name = data['current'][0]
    password = data['current'][1]
    data['income'] = 0
    data[name][password] = {
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
    pickle.dump(data, open('storage.dat', 'wb'))


def check_month():
    data = pickle.load(open('storage.dat', 'rb'))
    c_month = datetime.date.today()
    c_month = c_month.strftime('%b')
    if c_month != data['history']['months'][-1]:
        return True
    else:
        return False


def update_history():
    data = pickle.load(open('storage.dat', 'rb'))
    c_month = datetime.date.today()
    c_month = c_month.strftime('%b')
    if c_month != data['history']['months'][-1]:
        data['history']['months'].append(c_month)
        data['history']['m_saved'].append('0')
        data['history']['m_spent'].append('0')
        data['history']['m_income'].append(find_income())
        pickle.dump(data, open('storage.dat', 'wb'))
        reset_for_new_month()
    else:
        data['history']['m_saved'][-1] = calc_savings_spending('savings')
        data['history']['m_spent'][-1] = calc_savings_spending('spending')
        data['history']['m_income'][-1] = find_income()
        pickle.dump(data, open('storage.dat', 'wb'))


def remember_month(month=None, saved=None, spent=None, income=None):
    data = pickle.load(open('storage.dat', 'rb'))
    update_history()
    try:
        if month is not None:
            if data['history']['months'][month] != data['history']['months'][0]:
                return data['history']['months'][month]
            else:
                return ' '
        if saved is not None:
            if data['history']['m_saved'][saved] != data['history']['m_saved'][0]:
                return '$' + data['history']['m_saved'][saved]
            else:
                return ' '
        if spent is not None:
            if data['history']['m_spent'][spent] != data['history']['m_spent'][0]:
                return '$' + data['history']['m_spent'][spent]
            else:
                return ' '
        if income is not None:
            if data['history']['m_income'][income] != data['history']['m_income'][0]:
                return '$' + data['history']['m_income'][income]
            else:
                return ' '
    except IndexError:
        return(' ')


def total_savings():
    data = pickle.load(open('storage.dat', 'rb'))
    past_savings = data['history']['m_saved']
    total_past_savings = 0
    for i in past_savings:
        i = eval(i)
        total_past_savings += i
    return '$' + str(total_past_savings)
