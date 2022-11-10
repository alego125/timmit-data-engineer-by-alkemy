-- Desafio SQL Alkemy Data Engineer

-- 01 Mostrar el Precio Maximo de los productos de la tabla PRODUCTS por línea de
-- producto y renombrar ese campo como Precio_Maximo
select 
	productLine,
	max(buyPrice) as Precio_Maximo 
from products
group by 1; -- es lo mismo que escribir "group by productLine" 

-- 02 De la tabla ORDERS obtener los números de las últimas 5 órdenes
select * from orders
order by orderDate desc
limit 5; -- usar TOP en SQL SERVER -- limit es para MySQL

-- 03 De la tabla EMPLOYEES mostrar cuanta cantidad de representantes de ventas (su jobTitle) hay en
-- cada oficina que no sea la 4.
select officeCode, count(reportsTo) as cantidad_representantes from employees
where officeCode != 4 and jobTitle = "Sales Rep"
group by officeCode;

-- 04 Indicar en una misma consulta: la cantidad de registros de la tabla productos, el precio promedio de los mismos, el precio maximo y el precio minimo y la suma total de productos en stock (sin agrupar por producto)
select count(*) as total_Registros , max(buyprice) as precio_maximo,  min(buyprice) as precio_minimo
, avg(buyprice) as precio_promedio, sum(quantityinstock) as total_stock from products;

-- 05  Mostrar en una tabla el numero de cada orden, la cantidad y la fecha de envio (shippedDate)
select a.orderNumber, quantityordered, shippeddate from orders a
left join orderdetails b on a.ordernumber=b.ordernumber;

-- 06. Obtener la cantidad de clientes por país, ordenado de mayor a menor.
select
	country,
	count(customerNumber) 
from customers
group by country
order by count(customerNumber) desc;

-- 07. Obtener la cantidad de clientes por país, ordenado de mayor a menor. Solo mostrar aquellos países con mas de 5 clientes.
select
	country,
	count(customerNumber) 
from customers
group by country
having count(customerNumber)>5
order by count(customerNumber) desc;

-- 08. Obtener todas las ordenes por número de cliente que hayan sido emitidas en el año 2005. Solo mostrar aquellos clientes con mas de 3 ordenes.
select 
	customerNumber,
	count(OrderNumber)
from orders
where year(orderDate)=2005
group by customerNumber
having count(orderNumber)>3;

-- 09. Obtener una lista con los nombres de clientes y la cantidad de ordenes que se emitieron para ellos.
select 
	customerName,
    count(orders.orderNumber) as Ordenes
from customers
left join orders on customers.customerNumber = orders.customerNumber
group by customerName;

-- 10. Obtener los nombres de los clientes y el monto (amount) de aquellos que relizaron compras en los meses de Marzo de cada año. Ordenar por monto de mayor a menor
select customername,amount from customers a
inner join payments b on a.customerNumber=b.customernumber
where month(paymentDate)=03
order by amount DESC;

-- 11. Aplicar un descuento del 10% (buyPrice) a los productos cuya cantidad en stock sea mayor a 8000 (quantityInStock)
select productName, quantityInStock, buyPrice, buyPrice*0.9 as buyPrice_discount from products
where quantityInStock>8000;

-- 12. Obtener los registros de los productos cuyo codigo inicie con la secuencia " S10_ "
select * from products
where productcode like 'S10_%';

-- 13. Obtenga los codigos de producto, nombre, linea a la que pertenecen y descripcion de aquellos en los cuales la descricion del producto contenga la palabra "features"
select productcode, productname,productline,productdescription from products
where productdescription like '%features%';

-- 14.  Obtenga los codigos de los pagos (payments) , fecha y monto de aquellos que comienzan con la secuencia "IP" y son mayores o iguales a 1000
select * from payments
where checkNumber like 'IP%' and amount>=1000;

-- 15. Obtener los nombres de las líneas de producto que tengan más de una palabra
select productLine from productlines
where productLine like "% %";

-- 16. Obtener la cantidad de cheques emitidos por año desde el mas actual hasta el mas antiguo, el importe promedio de los mismos, el máximo
-- importe y el mínimo importe
select 
	year(paymentDate) as Año,
    count(checkNumber) as Cheques,
    avg(amount) as Importe_Promedio,
    max(amount) as Importe_Maximo,
    min(amount) as Importe_Minimo
from payments
group by Año
order by Año desc;

-- 17. Obtener un listado de ordenes emitidas a clientes de USA mostrando el valor total de cada orden
-- si se le aplicara un aumento del 10%
select 
	orders.orderNumber,
    sum(orderdetails.priceEach * orderdetails.quantityOrdered) as Importe,
    sum(orderdetails.priceEach * orderdetails.quantityOrdered) * 1.1 as Importe_Aumentado
from orderdetails
left join orders on orders.orderNumber = orderdetails.orderNumber
left join customers on orders.customerNumber = customers.customerNumber
where customers.country = "USA"
group by orders.orderNumber;

-- 18. Obtener el listado de clientes que sean USA o España cuyo límite de crédito sea mayor a 50000 o
-- que no tengan ningun representate de venta asignado
select * 
from customers
where country = "USA" or country = "Spain" and creditLimit > 5000 and salesRepEmployeeNumber is null;

