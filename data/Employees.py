import random
import names
import itertools
import string


headerEmployee = ['id', 'name', 'age', 'role', 'salary', 'debt', 'tax_rate', 'email']

def generate_random_email():
    domain = "@example.com"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length)) 
    return username + domain


employees = []
id_obj = itertools.count()

for i in range(2000):
    id = next(id_obj)
    name = names.get_full_name()
    age = random.randint(22, 60) 
    role = random.choice(['Manager', 'Developer', 'Designer', 'Analyst'])
    salary = random.randint(1500000, 9000000)
    debt = random.choice([True, False])
    tax_rate = random.uniform(0.1, 0.3)
    email = generate_random_email()
    
    employee = [id, name, age, role, salary, debt, tax_rate, email]
    employees.append(employee)

#df = pd.DataFrame(employees, columns=['id', 'name', 'age', 'role', 'salary', 'debt', 'tax_rate', 'email'])

#print(df)

# Export to CSV
#df.to_csv('employees.csv', index=False)