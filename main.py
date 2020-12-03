from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now().date())
    print(calculate_salary())
    print(get_employees())
