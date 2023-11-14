import random

headerProduct = ['id', 'product', 'unitCost', 'tax']

nombresProductos = ['computadora', 'tableta', 'celular', 'reloj inteligente', 'bocinas',
                    'laptop', 'televisión', 'consola', 'audífonos', 'altavoz']

products = []

for i in range(3000):
    product = random.choice(nombresProductos)
    unitCost = random.randint(45000, 150000)
    tax = unitCost* 0.19

    product = [i, product, unitCost, tax]
    products.append(product)

#df = pd.DataFrame(products, columns=['id', 'producto', 'costoUnitario', 'iva'])

#print(df.head())

#df.to_csv('products.csv', index=False)
