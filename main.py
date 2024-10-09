from application.salary import calculate_salary
import datetime
import pyfiglet

if __name__ == '__main__':
    print(calculate_salary('Петров', 100,'май'))
    # текцщее время
    print(f'текущая дата: {datetime.date.today()}')
    # библиотека figlet
    figlet = pyfiglet.Figlet(font='banner')
    print()
    print(figlet.renderText('Привет, это figlet'))