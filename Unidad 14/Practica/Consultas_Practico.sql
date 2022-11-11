Consultas:

--1)Listar los nombres de los proveedores cuya ciudad contenga
--la cadena de texto “Ramos”

SELECT p.Nombre
FROM Proveedor p
WHERE Ciudad LIKE '%Ramos%';

--2) Listar los códigos de los materiales que provea el proveedor 4
--y no los provea el proveedor 5. Se debe resolver de 3 formas.

--FORMA 1

SELECT CodMat
FROM Provisto_Por
WHERE CodProv = 4 AND CodProv NOT IN (
	SELECT CodMat
	FROM Provisto_Por 
	WHERE CodMat = 5
	);

--FORMA 2

SELECT CodMat
FROM Material
WHERE CodMat IN (
	SELECT CodMat
	FROM Provisto_Por
	WHERE CodProv = 4
);

--FORMA 3

SELECT pp1.CodMat
FROM Provisto_Por pp1
WHERE EXISTS(
	SELECT 1
	FROM Provisto_Por pp2
	WHERE pp1.CodProv = pp2.CodProv AND pp2.CodProv = 4
);

--FORMA 4

SELECT m.CodMat
FROM Material m
INNER JOIN Provisto_Por pp
ON m.CodMat = pp.CodMat
WHERE m.CodMat NOT IN (
	SELECT CodMat
	FROM Provisto_Por
	WHERE CodProv = 5
) AND pp.CodProv = 4;


--3) Listar los materiales, código y descripción, provistos por
--proveedores de la ciudad de Ramos Mejía.

--No hay nada en Ramos Mejía

SELECT m.CodMat, m.Descripcion
	FROM Material m
	WHERE EXISTS(
		SELECT 1 
		FROM Provisto_Por pp 
		WHERE m.CodMat = pp.CodMat AND pp.CodProv IN (
			SELECT CodProv
			FROM Proveedor p
			WHERE p.Ciudad = 'Ramos Mejía'
		))

---------------------------------------------------------

--(Lista de materiales provistos por la ciudad de CABA, use 
--CABA por que Ramos Mejía no tiene Materiales)

SELECT DISTINCT m.CodMat, m.Descripcion
FROM Material m
INNER JOIN Provisto_Por pp
ON m.CodMat = pp.CodMat
INNER JOIN Proveedor p
ON pp.CodProv = p.CodProv
WHERE p.Ciudad LIKE '%CABA%'

--4) Listar los proveedores y materiales que provee. La lista
--resultante debe incluir a aquellos proveedores que no proveen
--ningún material.

SELECT p.Nombre AS Nombre_Proveedor, m.Descripcion AS Material_Provisto
FROM Material m
INNER JOIN Provisto_Por pp
ON m.CodMat = pp.CodMat
RIGHT JOIN Proveedor p
ON p.CodProv = pp.CodProv;

--5) Listar los artículos que cuesten más de $30 o que estén
--compuestos por el material 2.

SELECT *
  FROM Articulo art
 WHERE Precio > 30
    OR EXISTS (SELECT 1
	       FROM Compuesto_Por cp
			WHERE cp.CodArt = art.CodArt
			AND CodMat = 2)

----------------------------------

--NO USAR O TRATAR DE NO USAR DISTINCT A MENOS QUE SI HAYAN VALORES REPETIDOS

SELECT DISTINCT a.Descripcion, a.Precio
FROM Articulo a
INNER JOIN Compuesto_Por cp
ON a.CodArt = cp.CodArt
INNER JOIN Material m
ON m.CodMat = cp.CodMat
WHERE a.Precio > 30 OR m.CodMat = 2;

--6) Listar los artículos de Mayor precio.

--Usar = en vez de IN por ejemplo es mas intuitivo y ocupa menos recursos

SELECT *
FROM Articulo
WHERE Precio = (
	SELECT MAX(Precio)
	FROM Articulo
);

--7) Listar los proveedores que proveen más de 3 materiales

SELECT *
FROM Proveedor p
WHERE EXISTS(
	SELECT 1
	FROM Provisto_Por pp
	WHERE pp.CodProv = p.CodProv
	HAVING COUNT(pp.CodMat) > 3
)

--8) Crear una vista para el caso de los proveedores que proveen
--más de 4 materiales. Mostrar la forma de invocar esa vista.

--Creamos la vista
CREATE VIEW proveedores_mas_materiales AS (
	SELECT *
		FROM Proveedor p
		WHERE EXISTS(
				SELECT 1
				FROM Provisto_Por pp
				WHERE pp.CodProv = p.CodProv
				HAVING COUNT(pp.CodMat) > 3
			)
);

--Llamamos a la vista
SELECT *
FROM proveedores_mas_materiales;

--EXTRA

--Cantidad de materiales segun proveedores por ciudad
SELECT COUNT(pp.CodProv) Cantidad, p.Ciudad
FROM Provisto_Por pp
INNER JOIN Proveedor p
ON pp.CodProv = p.CodProv
GROUP BY p.Ciudad