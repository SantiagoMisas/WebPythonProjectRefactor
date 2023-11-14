import random
import names
import csv

headerSale = ['orderNumber', 'client', 'cost']

sales = []

for _ in range(1000):
  orderNumber = random.randint(0, 500000)
  client = names.get_full_name()
  cost = random.randint(150000, 600000)
  order = [orderNumber, client, cost]
  sales.append(order)

# Add header row 
#ventas.insert(0, ['NumeroOrden', 'Cliente', 'Costo'])

# Export to CSV
'''with open('sales.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(ventas)
  
print('CSV file exported successfully!')'''