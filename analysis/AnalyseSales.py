import pandas as pd
import matplotlib.pyplot as plt
from helpers.CreateCSVFile import createCSV
from helpers.CreateGhraphic import generategraphic, colors, graphicsRoute
from data.Sales import sales, headerSale
from data.Employees import employees, headerEmployee
from data.Products import products, headerProduct
from helpers.CreateHTMLTable import createHTMLTable


#GENERAR ARCHIVOS CSV
createCSV(headerSale, sales, 'sales.csv')
createCSV(headerEmployee, employees, 'employees.csv')
createCSV(headerProduct, products, 'products.csv')

employeesDataFrame = pd.read_csv('data/employees.csv')
productsDataFrame = pd.read_csv('data/products.csv')
salesDataFrame = pd.read_csv('data/sales.csv')

#GENERAR TABLAS HTML
createHTMLTable(employeesDataFrame, 'EmployeesTable')
createHTMLTable(productsDataFrame, 'ProductsTable')
createHTMLTable(salesDataFrame, 'SalesTable')

print(employeesDataFrame)
print(productsDataFrame)
print(salesDataFrame)

#ESTADISTICA Y MEDIDAS DE LOS DATAFRAMES
e1 = employeesDataFrame.head()
e2 = employeesDataFrame.tail()
e3 = employeesDataFrame.head(20)
e4= employeesDataFrame.info()
e5 = employeesDataFrame.describe()
e6 = employeesDataFrame.tail(50)

p1 = productsDataFrame.head()
p2 = productsDataFrame.tail()
p3 = productsDataFrame.head(20)
p4 = productsDataFrame.info()
p5 = productsDataFrame.describe()
p6 = productsDataFrame.tail(50)

s1 = salesDataFrame.head()
s2 = salesDataFrame.tail()
s3 = salesDataFrame.head(20)
s4 = salesDataFrame.info()
s5 = salesDataFrame.describe()
s6 = salesDataFrame.tail(50)


filtroUno = salesDataFrame.query("(cost>=290000)  and (cost<=300000)")
totalSales = filtroUno['cost'].sum()
print(filtroUno)

#FILTRO DE VENTAS
ventasMayores = salesDataFrame.query("cost > 600000")
print(ventasMayores[['orderNumber','cost']])
createHTMLTable(ventasMayores[['orderNumber', 'cost']], 'salesHigherThan600000')
createCSV(['orderNumber', 'cost'], ventasMayores[['orderNumber', 'cost']], 'salesHigherThan600000.csv')

ventasIntervalo = salesDataFrame.query("cost >= 100000 & cost <= 600000")
print(ventasIntervalo[['orderNumber','cost']])
createHTMLTable(ventasIntervalo[['orderNumber', 'cost']], 'salesBetween100000And600000')
createCSV(['orderNumber', 'cost'], ventasIntervalo[['orderNumber', 'cost']], 'salesBetween100000And600000.csv')

filtro_uno = salesDataFrame.query("(cost >= 290000) & (cost <= 300000)")
for row in filtro_uno:
  cols = row.split(',')
  if len(cols) >= 3: 
    filtro_uno.append({'orderNumber': cols[0], 'cost': cols[2]})
  else:

    pass
total_ventas = filtro_uno['cost'].sum()
headerSF1=['orderNumber', 'cost']
createCSV(headerSF1, filtro_uno, 'lowSales.csv')
createHTMLTable(filtro_uno, 'lowSales')
print(filtro_uno)

ventas_filtro = salesDataFrame.query("cost > 600000 | (cost >= 100000 & cost <= 600000)")
for row in ventas_filtro:
  cols = row.split(',')
  if len(cols) >= 3: 
    ventas_filtro.append({'orderNumber': cols[0], 'cost': cols[2]})
  else:

    pass
headerSF2=['orderNumber', 'cost']
createCSV(headerSF2, ventas_filtro, 'salesFilter.csv') 
createHTMLTable(ventas_filtro, 'lowSales2')
print(ventas_filtro)

#FILTROS DE EMPLEADOS
empleados_filtro = employeesDataFrame.query("age > 24 & age < 60")
print(empleados_filtro[['name', 'role']])
createHTMLTable(empleados_filtro[['name', 'role']], 'employeesBetween24And60')
createCSV(['name', 'role'], empleados_filtro[['name', 'role']], 'employeesBetween24And60.csv')

empleados_filtro2 = employeesDataFrame.query("role == 'Developer' & salary > 2500000")
print(empleados_filtro2[['name', 'role']])
createHTMLTable(empleados_filtro2[['name', 'role', 'salary']], 'DevelopersWithSalary>2500000')
createCSV(['name', 'role'], empleados_filtro2[['name', 'role']], 'DevelopersWithSalary>2500000.csv')

empleados_filtro3 = employeesDataFrame.query("role == 'Developer' & salary > 2500000 & age > 24 & age < 60")
print(empleados_filtro3[['name', 'role']])
createHTMLTable(empleados_filtro3[['name', 'role', 'salary']], 'DevelopersWithSalary>2500000AndAge')
createCSV(['name', 'role'], empleados_filtro3[['name', 'role']], 'DevelopersWithSalary>2500000AndAge.csv')

# FILTROS DE PRODUCTOS
productos_filtro1 = productsDataFrame.query("unitCost > 500000")
print(productos_filtro1[['id', 'product', 'unitCost']])
createHTMLTable(productos_filtro1[['id', 'product', 'unitCost']], 'productsWithCost>500000')
createCSV(['id', 'product', 'unitCost'], productos_filtro1[['id', 'product', 'unitCost']], 'productsWithCost>500000.csv')

productos_filtro2 = productsDataFrame.query("unitCost >= 0 & unitCost <= 150000")
print(productos_filtro2[['id', 'product', 'unitCost']])
createHTMLTable(productos_filtro2[['id', 'product', 'unitCost']], 'productsFilter2')
createCSV(['id', 'product', 'unitCost'], productos_filtro2[['id', 'product', 'unitCost']], 'productsWithCostBetween0And150000.csv')

#GRAFICOS PNG Y PDF
highestSalary = employeesDataFrame.nlargest(10, "salary")
graphicsRouteSalary = "figures/graphicSalary.png"
graphicsRouteSalarypdf = "figures/graphicSalary.pdf"
generategraphic(highestSalary, highestSalary['name'], highestSalary['salary'], "name", "salary", "10 Highest Salary", graphicsRouteSalary, graphicsRouteSalarypdf, colors)

lowestPricesProducts = productsDataFrame.nsmallest(5, "unitCost")
graphicsRouteProducts = "figures/lowestPricesProducts.png"
graphicsRouteProductspdf = "figures/lowestPricesProducts.pdf"
generategraphic(lowestPricesProducts, lowestPricesProducts['product'], lowestPricesProducts['unitCost'], "product", "unitCost", "5 Lowest Prices Products", graphicsRouteProducts, graphicsRouteProductspdf, colors)

biggerSales =salesDataFrame.sort_values(by='cost', ascending=False)
topSales = biggerSales.head(8)
graphicsRouteSales = "figures/topSales.png"
graphicsRouteSalespdf = "figures/topSales.pdf"
generategraphic(topSales, topSales['client'], topSales['cost'], "client", "cost", "8 Top Sales", graphicsRouteSales, graphicsRouteSalespdf, colors)


''' 1. crear csv
 2. cargar la fente con pandas y un dataframe
 3. explorar los datos
 4 filtar y ordenar
 5 modelar o aplicar modelos de estadistica
 6 crear una estructura de datos
 Home
 en el home diseño libre unos parrafos una descripcion de la aplicacion un banner un menu seccion fotos, tarjetas
 El home redirecciona Al dashboard
 en el dashboard el diseño y la logica que se va renderizar
 csv 1000 ventas
 csv 2000 empleados
 csv 3000 productos
 productos id, nombre, 30 productos, costo unitario , iva 0.19
 debe entregar 3 analisis el dataframe de cada csv y la informacion descriptiva de cada dataframe y entregar de cada dataframe los 50 primeros registros  
 entregar 3 archivos separados de analisis con el dataframe de cada uno la info estadistica y los 50 primeros registros de cada uno
 pilas que despues de descanso examen de conocimiento

 -Mostrar para las ventas ventas>600000, ventas 100000 y 600000,debe salir numeroOrden y costo
-Edad <24 y Edad >60 años , cargo developer, filtrar salarios>2.5 millones, debe salir nombre, apellido, cargo
productoss productos>500000 entre 0 y 150000, debeSalir id nombre, costo
sacar 8 html de esas listas filtradas

Grafica para mostrar los 10 salarios mas altos de la compañia
grafica para mostrar los 5 productos mas baratos
grafica de mayores ventas
hacer un video explicando la aplicacion
hacer el metodo para la grafica
hacer el csv a pdf
'''



