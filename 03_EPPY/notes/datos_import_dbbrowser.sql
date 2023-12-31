BEGIN TRANSACTION;
--INSERT INTO LIBROS VALUES (1,'Harry Potter',10.50,264,1997,0);
INSERT INTO LIBROS VALUES (2,'El Alquimista',0,192,2022,0);
INSERT INTO LIBROS VALUES (3,'El Señor de los Anillos',12.10,1492,2022,0);
INSERT INTO LIBROS VALUES (4,'El Código da Vinci',0,656,2003,0);
INSERT INTO LIBROS VALUES (5,'Lo que el viento se llevó',0,1037,NULL,0);
INSERT INTO LIBROS VALUES (6,'El diario de Ana Frank',0,0,1947,1);
INSERT INTO LIBROS VALUES (7,'La espía',8,0,2016,0);
INSERT INTO LIBROS VALUES (8,'Odisea',15,18,NULL,0);
INSERT INTO LIBROS VALUES (9,'Don Quijote de la Mancha',10,1345,1605,1);
INSERT INTO LIBROS VALUES (10,'El principito',7,0,1943,0);
INSERT INTO LIBROS VALUES (11,'Cien años de soledad',0,0,1967,0);
INSERT INTO LIBROS VALUES (12,'El nombre de la rosa',15.62,737,1980,0);
INSERT INTO LIBROS VALUES (13,'Ilíada',0,0,NULL,0);
INSERT INTO LIBROS VALUES (14,'El hobbit',9,320,1937,0);
INSERT INTO LIBROS VALUES (15,'Romeo y Julieta',5,224,1597,0);
INSERT INTO LIBROS VALUES (16,'20.000 leguas de viaje submarino',0,320,1870,0);
INSERT INTO AUTORES VALUES (1,'J. K. Rowling',1965,null);
INSERT INTO AUTORES VALUES (2,'J. R. R. Tolkien',1892,1973);
INSERT INTO AUTORES VALUES (3,'Paulo Coelho',1947,null);
INSERT INTO AUTORES VALUES (4,'Dan Brown',1964,null);
INSERT INTO AUTORES VALUES (5,'Margaret Mitchell',1900,1949);
INSERT INTO AUTORES VALUES (6,'Anna Frank',1929,1945);
INSERT INTO AUTORES VALUES (7,'Homero',null,null);
INSERT INTO AUTORES VALUES (8,'William Shakespeare',1564,1616);
INSERT INTO AUTORES VALUES (9,'Lewis Wallace',1827,1905);
INSERT INTO AUTORES VALUES (10,'Bram Stoker',1847,1912);
INSERT INTO AUTORES VALUES (11,'Dante Alighieri',1265,1321);
INSERT INTO AUTORES VALUES (12,'V. C. Andrews',1923,1986);
INSERT INTO AUTORES VALUES (13,'Gabriel García Márquez',1927,2014);
INSERT INTO AUTORES VALUES (14,'Miguel de Cervantes',1547,1616);
INSERT INTO AUTORES VALUES (15,'Umberto Eco',1932,2016);
INSERT INTO AUTORES VALUES (16,'Antoine de Saint-Exupéry',1900,1944);
INSERT INTO AUTORES VALUES (17,'Julio Verne',1828,1905);
INSERT INTO ESCRITOS VALUES (1,1);
INSERT INTO ESCRITOS VALUES (2,3);
INSERT INTO ESCRITOS VALUES (4,4);
INSERT INTO ESCRITOS VALUES (3,2);
INSERT INTO ESCRITOS VALUES (7,3);
INSERT INTO ESCRITOS VALUES (5,5);
INSERT INTO ESCRITOS VALUES (11,13);
INSERT INTO ESCRITOS VALUES (9,14);
INSERT INTO ESCRITOS VALUES (6,6);
INSERT INTO ESCRITOS VALUES (14,2);
INSERT INTO ESCRITOS VALUES (12,15);
INSERT INTO ESCRITOS VALUES (10,16);
INSERT INTO ESCRITOS VALUES (13,7);
INSERT INTO ESCRITOS VALUES (8,7);
INSERT INTO ESCRITOS VALUES (15,8);
INSERT INTO ESCRITOS VALUES (16,17);
INSERT INTO USUARIOS VALUES (1,'Lorenzo','Pérez Martín','1980-09-09');
INSERT INTO USUARIOS VALUES (2,'Carmen','Villena Peris','2010-05-01');
INSERT INTO USUARIOS VALUES (3,'Rafael','Alonso Romero','1998-06-25');
INSERT INTO USUARIOS VALUES (4,'David','Ulloa Martínez','1976-01-10');
INSERT INTO PRESTAMOS VALUES (2,1,'2022-06-11','2022-06-20');
INSERT INTO PRESTAMOS VALUES (3,4,'2022-02-03','2022-02-27');
INSERT INTO PRESTAMOS VALUES (3,3,'2022-05-06','2022-06-29');
INSERT INTO PRESTAMOS VALUES (14,4,'2022-05-25',NULL);
INSERT INTO PRESTAMOS VALUES (6,4,'2022-01-10','2022-02-16');
COMMIT;