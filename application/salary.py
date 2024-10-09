from accounting.application.db.people import get_employees

def calculate_salary(name, hours,month):
     salary = get_employees(name)
     return f'Сотрудник {name}\nотработано {hours} часов\nзарплата за {month} = {round(salary / 168 * hours,2)} руб.'

