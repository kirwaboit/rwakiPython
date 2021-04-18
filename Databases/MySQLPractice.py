# Practice was done at https://sqltest.net/

CREATE TABLE reservation_table ( 
CustomerID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
Reservation VARCHAR(30) NOT NULL, 
Date TIMESTAMP 
); 

CREATE TABLE customer_table ( 
CustomerID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
FirstName VARCHAR(30) NOT NULL, 
LastName VARCHAR(30) NOT NULL
); 


INSERT INTO `reservation_table` (`CustomerID`, `Reservation`, `Date`) VALUES ('1', 'table_for_two', '2021-03-16');
INSERT INTO `reservation_table` (`CustomerID`, `Reservation`, `Date`) VALUES ('2', 'table_for_six', '2021-03-18');
INSERT INTO `reservation_table` (`CustomerID`, `Reservation`, `Date`) VALUES ('3', 'table_for_three', '2021-03-21');
INSERT INTO `reservation_table` (`CustomerID`, `Reservation`, `Date`) VALUES ('4', 'table_for_two', '2021-03-29');
INSERT INTO `customer_table` (`CustomerID`, `FirstName`, `LastName`) VALUES ('1', 'Glen', 'Stevenson');
INSERT INTO `customer_table` (`CustomerID`, `FirstName`, `LastName`) VALUES ('2', 'John', 'Doe');
INSERT INTO `customer_table` (`CustomerID`, `FirstName`, `LastName`) VALUES ('3', 'April', 'Stephenson ');
INSERT INTO `customer_table` (`CustomerID`, `FirstName`, `LastName`) VALUES ('4', 'Jill', 'Stevensen');

  

SELECT customer_table.FirstName, customer_table.LastName, reservation_table.Reservation 
FROM reservation_table
INNER JOIN customer_table ON reservation_table.CustomerID=customer_table.CustomerID 
and customer_table.LastName in ('Stephenson', 'Stevenson', 'Stevensen');

