create database project1;
use project1;
CREATE TABLE Products (
    Item_Code INTEGER PRIMARY KEY,
    Item_Name TEXT,
    Item_Price INT,
    GST INT,
    Discount_Offer INT,
    Stock INT
);
select * from Products;
CREATE TABLE project1.Product_Category (
    Category_Id INTEGER PRIMARY KEY,
    Category_Name TEXT,
    Item_Code INTEGER,
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);
select * from  Product_Category;
CREATE TABLE Buy (
    Cust_Id INTEGER,
    Item_Code INTEGER,
    PRIMARY KEY (Cust_Id, Item_Code),
    FOREIGN KEY (Cust_Id) REFERENCES Customers(Cust_Id),
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);

CREATE TABLE Customers (
    Cust_Id INTEGER PRIMARY KEY,
    Cust_Name VARCHAR(255),
    DOB TEXT,
    Email VARCHAR(255),
    Address VARCHAR(255)
);

CREATE TABLE Customers_Contact_No (
    Contact_Number INTEGER PRIMARY KEY,
    Cust_Id INTEGER,
    FOREIGN KEY (Cust_Id) REFERENCES Customers(Cust_Id)
);

CREATE TABLE Payment_Details (
    Payment_Id INTEGER PRIMARY KEY,
    Payment_date TEXT,
    Total_Amount REAL,
    Payment_Method TEXT,
    Emp_Code INTEGER,
    FOREIGN KEY (Emp_Code) REFERENCES Employee(Emp_code)
);

CREATE TABLE Order1(
    Order_Id INTEGER PRIMARY KEY,
    Order_Date TEXT,
    Total_Amount REAL,
    Tracking_Number TEXT,
    Payment_Id INTEGER,
    Order_Det_Id INTEGER,
    Cust_Id INTEGER,
    FOREIGN KEY (Payment_Id) REFERENCES Payment_Details(Payment_Id),
    FOREIGN KEY (Cust_Id) REFERENCES Customers(Cust_Id)
);

CREATE TABLE Bill (
    Order_Det_Id INTEGER PRIMARY KEY,
    Date_Of_billing TEXT,
    Total_amount REAL,
    Item_Code INTEGER,
    Bill_Number INTEGER,
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);

CREATE TABLE Tracking_Details (
    Tracking_Number varchar(255) PRIMARY KEY,
    Courier_Name VARCHAR(255)
);


CREATE TABLE Feedback_Comment (
    Comment varchar(255),
    Feedback_Id INTEGER PRIMARY KEY
);

CREATE TABLE Customer_Feedback (
    Cust_Id INTEGER,
    Item_Code INTEGER,
    Rating INTEGER,
    Feedback_date TEXT,
    PRIMARY KEY (Cust_Id, Item_Code),
    FOREIGN KEY (Cust_Id) REFERENCES Customers(Cust_Id),
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);
select * from Customer_Feedback;

CREATE TABLE Advertises (
    Item_Code INTEGER,
    Company_Code INTEGER,
    PRIMARY KEY (Item_Code, Company_Code),
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);

CREATE TABLE Advertising_Company (
    Company_Code INTEGER PRIMARY KEY,
    Company_Name TEXT
);

CREATE TABLE Supplier (
    Supplier_ID INTEGER PRIMARY KEY,
    Supplier_name TEXT,
    Supplier_address TEXT
);

CREATE TABLE Supplies (
    Supplier_Id INTEGER,
    Item_Code INTEGER,
    PRIMARY KEY (Supplier_Id, Item_Code),
    FOREIGN KEY (Supplier_Id) REFERENCES Supplier(Supplier_ID),
    FOREIGN KEY (Item_Code) REFERENCES Products(Item_Code)
);

CREATE TABLE Supplier_Contact (
    Supplier_contact INTEGER PRIMARY KEY,
    Supplier_Id INTEGER,
    FOREIGN KEY (Supplier_Id) REFERENCES Supplier(Supplier_ID)
);

CREATE TABLE Supplier_Email (
    Supplier_email varchar(255) PRIMARY KEY,
    Supplier_ID INTEGER,
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

CREATE TABLE Employee (
    Emp_code INTEGER PRIMARY KEY,
    Emp_name TEXT,
    Date TEXT,
    Month TEXT,
    Year TEXT,
    Age INTEGER,
    Position TEXT,
    Salary REAL,
    Username TEXT
);

CREATE TABLE Admin (
    Username varchar(255) PRIMARY KEY,
    Password varchar(255),
    Admin_ID INTEGER,
    Admin_name varchar(255)
);

CREATE TABLE Store (
    Store_ID INTEGER PRIMARY KEY,
    Store_Name varchar(255),
    Location varchar(255),
    Operating_hrs varchar(255),
    Username varchar(255)
);

CREATE TABLE Store_Contact_No (
    Contact_Number INTEGER PRIMARY KEY,
    Store_ID INTEGER,
    FOREIGN KEY (Store_ID) REFERENCES Store(Store_ID)
);


-- Inserting data into the tables

-- Products
INSERT IGNORE INTO Products VALUES (1, 'Milk', 2.5, 0.05, 0, 100);
INSERT IGNORE INTO Products VALUES (2, 'Bread', 1.5, 0.05, 0, 150);
INSERT IGNORE INTO Products VALUES (3, 'Apple', 0.5, 0.05, 0, 200);
INSERT IGNORE INTO Products VALUES (4, 'Orange Juice', 3, 0.1, 0, 80);
INSERT IGNORE INTO Products VALUES (5, 'Chocolate', 2, 0.05, 0.1, 120);
INSERT IGNORE INTO Products VALUES (6, 'Rice', 10, 0.1, 0, 50);
INSERT IGNORE INTO Products VALUES (7, 'Chicken', 8, 0.15, 0, 30);
INSERT IGNORE INTO Products VALUES (8, 'Tomato', 0.3, 0.05, 0, 220);
INSERT IGNORE INTO Products VALUES (9, 'Potato', 0.2, 0.05, 0, 300);
INSERT IGNORE INTO Products VALUES (10, 'Eggs', 1, 0.05, 0, 100);
select * from Products;

-- Product_Category
INSERT INTO Product_Category VALUES (1, 'Dairy', 1);
INSERT INTO Product_Category VALUES (2, 'Bakery', 2);
INSERT INTO Product_Category VALUES (3, 'Fruits', 3);
INSERT INTO Product_Category VALUES (4, 'Beverages', 4);
INSERT INTO Product_Category VALUES (5, 'Sweets', 5);
INSERT INTO Product_Category VALUES (6, 'Grains', 6);
INSERT INTO Product_Category VALUES (7, 'Meat', 7);
INSERT INTO Product_Category VALUES (8, 'Vegetables', 8);
INSERT INTO Product_Category VALUES (9, 'Vegetables', 9);
INSERT INTO Product_Category VALUES (10, 'Dairy', 10);
select * from Product_Category;
-- Customers
INSERT INTO Customers VALUES (1, 'John Doe', '1990-05-15', 'johndoe@email.com', '123 Main St');
INSERT INTO Customers VALUES (2, 'Jane Smith', '1985-07-20', 'janesmith@email.com', '456 Elm St');
INSERT INTO Customers VALUES (3, 'Alice Johnson', '1992-02-10', 'alice@email.com', '789 Oak St');
INSERT INTO Customers VALUES (4, 'Bob Williams', '1988-09-05', 'bob@email.com', '101 Pine St');
INSERT INTO Customers VALUES (5, 'Charlie Brown', '1995-04-18', 'charlie@email.com', '202 Cedar St');
INSERT INTO Customers VALUES (6, 'David Davis', '1993-11-12', 'david@email.com', '303 Maple St');
INSERT INTO Customers VALUES (7, 'Emily Jones', '1991-08-25', 'emily@email.com', '404 Birch St');
INSERT INTO Customers VALUES (8, 'Frank White', '1987-03-30', 'frank@email.com', '505 Spruce St');
INSERT INTO Customers VALUES (9, 'Grace Lee', '1994-06-22', 'grace@email.com', '606 Pineapple St');
INSERT INTO Customers VALUES (10, 'Hannah Clark', '1996-01-05', 'hannah@email.com', '707 Mango St');
select * from Customers;
-- Customers_Contact_No
INSERT INTO Customers_Contact_No VALUES (1234567890, 1);
INSERT INTO Customers_Contact_No VALUES (1234567891, 2);
INSERT INTO Customers_Contact_No VALUES (1234567892, 3);
INSERT INTO Customers_Contact_No VALUES (1234567893, 4);
INSERT INTO Customers_Contact_No VALUES (1234567894, 5);
INSERT INTO Customers_Contact_No VALUES (1234567895, 6);
INSERT INTO Customers_Contact_No VALUES (1234567896, 7);
INSERT INTO Customers_Contact_No VALUES (1234567897, 8);
INSERT INTO Customers_Contact_No VALUES (1234567898, 9);
INSERT INTO Customers_Contact_No VALUES (1234567899, 10);
select * from Customers_Contact_No;
-- Payment_Details
INSERT INTO Payment_Details VALUES (1, '2024-03-28', 25, 'Credit Card', 1);
INSERT INTO Payment_Details VALUES (2, '2024-03-29', 15, 'Debit Card', 2);
INSERT INTO Payment_Details VALUES (3, '2024-03-30', 5, 'Cash', 3);
INSERT INTO Payment_Details VALUES (4, '2024-03-31', 20, 'Credit Card', 4);
INSERT INTO Payment_Details VALUES (5, '2024-04-01', 10, 'Debit Card', 5);
INSERT INTO Payment_Details VALUES (6, '2024-04-02', 30, 'Cash', 6);
INSERT INTO Payment_Details VALUES (7, '2024-04-03', 40, 'Credit Card', 7);
INSERT INTO Payment_Details VALUES (8, '2024-04-04', 35, 'Debit Card', 8);
INSERT INTO Payment_Details VALUES (9, '2024-04-05', 45, 'Cash', 9);
INSERT INTO Payment_Details VALUES (10, '2024-04-06', 50, 'Credit Card', 10);
select * from Payment_Details;
-- Order
INSERT INTO Order1 VALUES (1, '2024-03-28', 25, 'TN12345', 1, 1, 1);
INSERT INTO Order1 VALUES (2, '2024-03-29', 15, 'TN12346', 2, 2, 2);
INSERT INTO Order1 VALUES (3, '2024-03-30', 5, 'TN12347', 3, 3, 3);
INSERT INTO Order1 VALUES (4, '2024-03-31', 20, 'TN12348', 4, 4, 4);
INSERT INTO Order1 VALUES (5, '2024-04-01', 10, 'TN12349', 5, 5, 5);
INSERT INTO Order1 VALUES (6, '2024-04-02', 30, 'TN12350', 6, 6, 6);
INSERT INTO Order1 VALUES (7, '2024-04-03', 40, 'TN12351', 7, 7, 7);
INSERT INTO Order1 VALUES (8, '2024-04-04', 35, 'TN12352', 8, 8, 8);
INSERT INTO Order1 VALUES (9, '2024-04-05', 45, 'TN12353', 9, 9, 9);
INSERT INTO Order1 VALUES (10, '2024-04-06', 50, 'TN12354', 10, 10, 10);
select * from Order1;
-- Bill
INSERT INTO Bill VALUES (1, '2024-03-28', 25, 1, 101);
INSERT INTO Bill VALUES (2, '2024-03-29', 15, 2, 102);
INSERT INTO Bill VALUES (3, '2024-03-30', 5, 3, 103);
INSERT INTO Bill VALUES (4, '2024-03-31', 20, 4, 104);
INSERT INTO Bill VALUES (5, '2024-04-01', 10, 5, 105);
INSERT INTO Bill VALUES (6, '2024-04-02', 30, 6, 106);
INSERT INTO Bill VALUES (7, '2024-04-03', 40, 7, 107);
INSERT INTO Bill VALUES (8, '2024-04-04', 35, 8, 108);
INSERT INTO Bill VALUES (9, '2024-04-05', 45, 9, 109);
INSERT INTO Bill VALUES (10, '2024-04-06', 50, 10, 110);
select * from Bill;
-- Tracking_Details
INSERT INTO Tracking_Details VALUES ('TN12345', 'FastCourier');
INSERT INTO Tracking_Details VALUES ('TN12346', 'QuickShip');
INSERT INTO Tracking_Details VALUES ('TN12347', 'SpeedyDelivery');
INSERT INTO Tracking_Details VALUES ('TN12348', 'ExpressDelivery');
INSERT INTO Tracking_Details VALUES ('TN12349', 'SwiftCourier');
INSERT INTO Tracking_Details VALUES ('TN12350', 'RapidShip');
INSERT INTO Tracking_Details VALUES ('TN12351', 'ZoomDelivery');
INSERT INTO Tracking_Details VALUES ('TN12352', 'SpeedyShip');
INSERT INTO Tracking_Details VALUES ('TN12353', 'LightningCourier');
INSERT INTO Tracking_Details VALUES ('TN12354', 'FlashDelivery');
select * from Tracking_Details;
-- Feedback_Comment
INSERT INTO Feedback_Comment VALUES ('Great service!', 1);
INSERT INTO Feedback_Comment VALUES ('Fast delivery', 2);
INSERT INTO Feedback_Comment VALUES ('Good quality products', 3);
INSERT INTO Feedback_Comment VALUES ('Impressive!', 4);
INSERT INTO Feedback_Comment VALUES ('Will shop again', 5);
INSERT INTO Feedback_Comment VALUES ('Recommended', 6);
INSERT INTO Feedback_Comment VALUES ('Satisfied customer', 7);
INSERT INTO Feedback_Comment VALUES ('Excellent!', 8);
INSERT INTO Feedback_Comment VALUES ('Best in town', 9);
INSERT INTO Feedback_Comment VALUES ('Keep it up!', 10);

-- Feedback
INSERT INTO Customer_Feedback VALUES (1, 1, 5, '2024-03-28');
INSERT INTO  Customer_Feedback VALUES (2, 2, 4, '2024-03-29');
INSERT INTO  Customer_Feedback VALUES (3, 3, 5, '2024-03-30');
INSERT INTO  Customer_Feedback VALUES (4, 4, 4, '2024-03-31');
INSERT INTO  Customer_Feedback VALUES (5, 5, 5, '2024-04-01');
INSERT INTO  Customer_Feedback VALUES (6, 6, 4, '2024-04-02');
INSERT INTO  Customer_Feedback VALUES (7, 7, 5, '2024-04-03');
INSERT INTO  Customer_Feedback VALUES (8, 8, 4, '2024-04-04');
INSERT INTO  Customer_Feedback VALUES (9, 9, 5, '2024-04-05');
INSERT INTO  Customer_Feedback VALUES (10, 10, 4, '2024-04-06');

-- Advertises
INSERT INTO Advertises VALUES (1, 1);
INSERT INTO Advertises VALUES (2, 2);
INSERT INTO Advertises VALUES (3, 3);
INSERT INTO Advertises VALUES (4, 4);
INSERT INTO Advertises VALUES (5, 5);
INSERT INTO Advertises VALUES (6, 6);
INSERT INTO Advertises VALUES (7, 7);
INSERT INTO Advertises VALUES (8, 8);
INSERT INTO Advertises VALUES (9, 9);
INSERT INTO Advertises VALUES (10, 10);

-- Advertising_Company
INSERT INTO Advertising_Company VALUES (1, 'FreshAds');
INSERT INTO Advertising_Company VALUES (2, 'QuickAds');
INSERT INTO Advertising_Company VALUES (3, 'FruitAds');
INSERT INTO Advertising_Company VALUES (4, 'DrinkAds');
INSERT INTO Advertising_Company VALUES (5, 'SweetAds');
INSERT INTO Advertising_Company VALUES (6, 'GrainAds');
INSERT INTO Advertising_Company VALUES (7, 'MeatAds');
INSERT INTO Advertising_Company VALUES (8, 'VeggieAds');
INSERT INTO Advertising_Company VALUES (9, 'TaterAds');
INSERT INTO Advertising_Company VALUES (10, 'EggAds');

-- Supplier
INSERT INTO Supplier VALUES (1, 'MilkSupplier', '123 Dairy St');
INSERT INTO Supplier VALUES (2, 'BreadSupplier', '456 Bakery St');
INSERT INTO Supplier VALUES (3, 'AppleSupplier', '789 Orchard St');
INSERT INTO Supplier VALUES (4, 'JuiceSupplier', '101 Beverage St');
INSERT INTO Supplier VALUES (5, 'ChocolateSupplier', '202 Sweets St');
INSERT INTO Supplier VALUES (6, 'RiceSupplier', '303 Grain St');
INSERT INTO Supplier VALUES (7, 'ChickenSupplier', '404 Meat St');
INSERT INTO Supplier VALUES (8, 'TomatoSupplier', '505 Veggie St');
INSERT INTO Supplier VALUES (9, 'PotatoSupplier', '606 Spud St');
INSERT INTO Supplier VALUES (10, 'EggSupplier', '707 Farm St');
select * from Supplier;
-- Supplies
INSERT INTO Supplies VALUES (1, 1);
INSERT INTO Supplies VALUES (2, 2);
INSERT INTO Supplies VALUES (3, 3);
INSERT INTO Supplies VALUES (4, 4);
INSERT INTO Supplies VALUES (5, 5);
INSERT INTO Supplies VALUES (6, 6);
INSERT INTO Supplies VALUES (7, 7);
INSERT INTO Supplies VALUES (8, 8);
INSERT INTO Supplies VALUES (9, 9);
INSERT INTO Supplies VALUES (10, 10);
select * from Supplies;
-- Supplier_Contact
INSERT INTO Supplier_Contact VALUES (1111111111, 1);
INSERT INTO Supplier_Contact VALUES (1111111112, 2);
INSERT INTO Supplier_Contact VALUES (1111111113, 3);
INSERT INTO Supplier_Contact VALUES (1111111114, 4);
INSERT INTO Supplier_Contact VALUES (1111111115, 5);
INSERT INTO Supplier_Contact VALUES (1111111116, 6);
INSERT INTO Supplier_Contact VALUES (1111111117, 7);
INSERT INTO Supplier_Contact VALUES (1111111118, 8);
INSERT INTO Supplier_Contact VALUES (1111111119, 9);
INSERT INTO Supplier_Contact VALUES (1111111120, 10);

-- Supplier_Email
INSERT INTO Supplier_Email VALUES ('milk@email.com', 1);
INSERT INTO Supplier_Email VALUES ('bread@email.com', 2);
INSERT INTO Supplier_Email VALUES ('apple@email.com', 3);
INSERT INTO Supplier_Email VALUES ('juice@email.com', 4);
INSERT INTO Supplier_Email VALUES ('chocolate@email.com', 5);
INSERT INTO Supplier_Email VALUES ('rice@email.com', 6);
INSERT INTO Supplier_Email VALUES ('chicken@email.com', 7);
INSERT INTO Supplier_Email VALUES ('tomato@email.com', 8);
INSERT INTO Supplier_Email VALUES ('potato@email.com', 9);
INSERT INTO Supplier_Email VALUES ('egg@email.com', 10);

-- Employee
INSERT INTO Employee VALUES (1, 'Alex', '2024-01-01', 'January', '2024', 30, 'Manager', 5000, 'alex123');
INSERT INTO Employee VALUES (2, 'Brian', '2024-02-02', 'February', '2024', 25, 'Salesperson', 3000, 'brian123');
INSERT INTO Employee VALUES (3, 'Charlie', '2024-03-03', 'March', '2024', 22, 'Cashier', 2500, 'charlie123');
INSERT INTO Employee VALUES (4, 'David', '2024-04-04', 'April', '2024', 28, 'Storekeeper', 3200, 'david123');
INSERT INTO Employee VALUES (5, 'Emma', '2024-05-05', 'May', '2024', 35, 'Manager', 5500, 'emma123');
INSERT INTO Employee VALUES (6, 'Frank', '2024-06-06', 'June', '2024', 26, 'Salesperson', 3100, 'frank123');
INSERT INTO Employee VALUES (7, 'Grace', '2024-07-07', 'July', '2024', 23, 'Cashier', 2600, 'grace123');
INSERT INTO Employee VALUES (8, 'Henry', '2024-08-08', 'August', '2024', 29, 'Storekeeper', 3300, 'henry123');
INSERT INTO Employee VALUES (9, 'Ivy', '2024-09-09', 'September', '2024', 32, 'Manager', 5200, 'ivy123');
INSERT INTO Employee VALUES (10, 'Jack', '2024-10-10', 'October', '2024', 27, 'Salesperson', 2900, 'jack123');

-- Admin
INSERT INTO Admin VALUES ('admin1', 'password1', 1, 'John');
INSERT INTO Admin VALUES ('admin2', 'password2', 2, 'Jane');
INSERT INTO Admin VALUES ('admin3', 'password3', 3, 'Alice');
INSERT INTO Admin VALUES ('admin4', 'password4', 4, 'Bob');
INSERT INTO Admin VALUES ('admin5', 'password5', 5, 'Charlie');
INSERT INTO Admin VALUES ('admin6', 'password6', 6, 'David');
INSERT INTO Admin VALUES ('admin7', 'password7', 7, 'Emily');
INSERT INTO Admin VALUES ('admin8', 'password8', 8, 'Frank');
INSERT INTO Admin VALUES ('admin9', 'password9', 9, 'Grace');
INSERT INTO Admin VALUES ('admin10', 'password10', 10, 'Henry');

-- Store
INSERT INTO Store VALUES (1, 'StoreA', 'New York', '9am-9pm', 'alex123');
INSERT INTO Store VALUES (2, 'StoreB', 'Los Angeles', '8am-10pm', 'brian123');
INSERT INTO Store VALUES (3, 'StoreC', 'Chicago', '10am-8pm', 'charlie123');
INSERT INTO Store VALUES (4, 'StoreD', 'Houston', '9am-9pm', 'david123');
INSERT INTO Store VALUES (5, 'StoreE', 'Phoenix', '8am-10pm', 'emma123');
INSERT INTO Store VALUES (6, 'StoreF', 'Philadelphia', '10am-8pm', 'frank123');
INSERT INTO Store VALUES (7, 'StoreG', 'San Antonio', '9am-9pm', 'grace123');
INSERT INTO Store VALUES (8, 'StoreH', 'San Diego', '8am-10pm', 'henry123');
INSERT INTO Store VALUES (9, 'StoreI', 'Dallas', '10am-8pm', 'ivy123');
INSERT INTO Store VALUES (10, 'StoreJ', 'San Jose', '9am-9pm', 'jack123');

-- Store_Contact_No
INSERT INTO Store_Contact_No VALUES (1111111100, 1);
INSERT INTO Store_Contact_No VALUES (1111111101, 2);
INSERT INTO Store_Contact_No VALUES (1111111102, 3);
INSERT INTO Store_Contact_No VALUES (1111111103, 4);
INSERT INTO Store_Contact_No VALUES (1111111104, 5);
INSERT INTO Store_Contact_No VALUES (1111111105, 6);
INSERT INTO Store_Contact_No VALUES (1111111106, 7);
INSERT INTO Store_Contact_No VALUES (1111111107, 8);
INSERT INTO Store_Contact_No VALUES (1111111108, 9);
INSERT INTO Store_Contact_No VALUES (1111111109, 10);

select * from Store_Contact_No;

-- 1. Retrieve all product names along with their categories.
SELECT Products.Item_Name, Product_Category.Category_Name 
FROM Products 
INNER JOIN Product_Category ON Products.Item_Code = Product_Category.Item_Code;

-- 2. Retrieve the total amount and payment method for each order.
SELECT Order1.Order_Id, Payment_Details.Total_Amount, Payment_Details.Payment_Method 
FROM Order1 
INNER JOIN Payment_Details ON Order1.Payment_Id = Payment_Details.Payment_Id;

-- 3. Retrieve all customers who made a purchase using 'Credit Card'.
SELECT Customers.Cust_Name, Payment_Details.Payment_Method 
FROM Customers 
INNER JOIN Buy ON Customers.Cust_Id = Buy.Cust_Id 
INNER JOIN Payment_Details ON Buy.Cust_Id = Payment_Details.Payment_Id 
WHERE Payment_Details.Payment_Method = 'Credit Card';

-- 4. Retrieve the total stock for each product category.
SELECT Product_Category.Category_Name, SUM(Products.Stock) AS Total_Stock 
FROM Product_Category 
INNER JOIN Products ON Product_Category.Item_Code = Products.Item_Code 
GROUP BY Product_Category.Category_Name;

-- 5. Retrieve all orders placed by customers with their feedback ratings.
SELECT Order1.Order_Id, Customer_Feedback.Rating 
FROM Order1 
INNER JOIN Customer_Feedback ON Order1.Cust_Id = Customer_Feedback.Cust_Id;

-- 6. Retrieve the total amount of sales for each product.
SELECT Products.Item_Name, SUM(Bill.Total_amount) AS Total_Sales 
FROM Products 
INNER JOIN Bill ON Products.Item_Code = Bill.Item_Code 
GROUP BY Products.Item_Name;

-- 7. Retrieve all suppliers who supply 'Milk' and their contact details.
SELECT Supplier.Supplier_name, Supplier_Contact.Supplier_contact, Supplier_Email.Supplier_email 
FROM Supplier 
INNER JOIN Supplies ON Supplier.Supplier_ID = Supplies.Supplier_Id 
INNER JOIN Products ON Supplies.Item_Code = Products.Item_Code 
INNER JOIN Supplier_Contact ON Supplier.Supplier_ID = Supplier_Contact.Supplier_Id 
INNER JOIN Supplier_Email ON Supplier.Supplier_ID = Supplier_Email.Supplier_ID 
WHERE Products.Item_Name = 'Milk';

-- 8. Retrieve the average rating of each product.
SELECT Products.Item_Name, AVG(Customer_Feedback.Rating) AS Average_Rating 
FROM Products 
LEFT JOIN Customer_Feedback ON Products.Item_Code = Customer_Feedback.Item_Code 
GROUP BY Products.Item_Name;

-- 9. Retrieve all payments made in cash greater than $30.
SELECT * 
FROM Payment_Details 
WHERE Payment_Details.Payment_Method = 'Cash' AND Payment_Details.Total_Amount > 30;

-- 10. Retrieve the name and total sales of the top 5 selling products.
SELECT Products.Item_Name, SUM(Bill.Total_amount) AS Total_Sales 
FROM Products 
INNER JOIN Bill ON Products.Item_Code = Bill.Item_Code 
GROUP BY Products.Item_Name 
ORDER BY Total_Sales DESC 
LIMIT 5;

-- 11. Retrieve the total number of products supplied by each supplier.
SELECT Supplier.Supplier_name, COUNT(Supplies.Item_Code) AS Total_Products 
FROM Supplier 
INNER JOIN Supplies ON Supplier.Supplier_ID = Supplies.Supplier_Id 
GROUP BY Supplier.Supplier_name;

-- 12. Retrieve all customers who have not given any feedback.
SELECT Customers.Cust_Name 
FROM Customers 
LEFT JOIN Customer_Feedback ON Customers.Cust_Id = Customer_Feedback.Cust_Id 
WHERE Customer_Feedback.Cust_Id IS NULL;

-- 13. Retrieve the details of the oldest and youngest employees.
SELECT * FROM Employee 
ORDER BY Date, Month, Year 
LIMIT 1;

SELECT * FROM Employee 
ORDER BY Date DESC, Month DESC, Year DESC 
LIMIT 1;

-- 14. Retrieve the names of the advertising companies that advertise 'Bread'.
SELECT Advertising_Company.Company_Name 
FROM Advertising_Company 
INNER JOIN Advertises ON Advertising_Company.Company_Code = Advertises.Company_Code 
INNER JOIN Products ON Advertises.Item_Code = Products.Item_Code 
WHERE Products.Item_Name = 'Bread';

-- 15. Retrieve the total sales amount for each payment method.
SELECT Payment_Details.Payment_Method, SUM(Order1.Total_Amount) AS Total_Sales 
FROM Order1
INNER JOIN Payment_Details ON Order1.Payment_Id = Payment_Details.Payment_Id 
GROUP BY Payment_Details.Payment_Method;

-- 16. Retrieve all products with a discount offer greater than 10%.
SELECT * 
FROM Products 
WHERE Products.Discount_Offer > 10;

-- 17. Retrieve the names of customers who purchased 'Eggs' more than once.
SELECT Customers.Cust_Name 
FROM Customers 
INNER JOIN Buy ON Customers.Cust_Id = Buy.Cust_Id 
INNER JOIN Products ON Buy.Item_Code = Products.Item_Code 
WHERE Products.Item_Name = 'Eggs' 
GROUP BY Customers.Cust_Name 
HAVING COUNT(Products.Item_Code) > 1;

-- 18. Retrieve the name of the courier for each order.
SELECT Order1.Order_Id, Tracking_Details.Courier_Name 
FROM Order1 
INNER JOIN Tracking_Details ON Order1.Tracking_Number = Tracking_Details.Tracking_Number;

-- 19. Retrieve all employees with a salary greater than the average salary.
SELECT * FROM Employee 
WHERE Salary > (SELECT AVG(Salary) FROM Employee);

-- 20. Retrieve the names of the customers who made a purchase on their birthday.
SELECT Customers.Cust_Name 
FROM Customers 
INNER JOIN Buy ON Customers.Cust_Id = Buy.Cust_Id 
WHERE Buy.Item_Code IN (SELECT Item_Code FROM Products WHERE Item_Name = 'Birthday Cake') 
AND SUBSTR(Customers.DOB, 6) = SUBSTR(Buy.Order_Date, 6);

-- 21. Retrieve the total number of customers who made a purchase.
SELECT COUNT(DISTINCT Cust_Id) AS Total_Customers
FROM Buy;

-- 22. Retrieve the total number of orders placed in the last month.
SELECT COUNT(Order_Id) AS Total_Orders
FROM `Order`
WHERE Order_Date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE();

-- 23. Retrieve the names of the customers who purchased products with a discount.
SELECT DISTINCT Customers.Cust_Name
FROM Customers
INNER JOIN Buy ON Customers.Cust_Id = Buy.Cust_Id
INNER JOIN Products ON Buy.Item_Code = Products.Item_Code
WHERE Products.Discount_Offer > 0;

-- 24. Retrieve the products that have a stock of less than 50.
SELECT Item_Name, Stock
FROM Products
WHERE Stock < 50;

-- 25. Retrieve the total sales amount for each product category.
SELECT Product_Category.Category_Name, SUM(Bill.Total_amount) AS Total_Sales
FROM Product_Category
INNER JOIN Products ON Product_Category.Item_Code = Products.Item_Code
INNER JOIN Bill ON Products.Item_Code = Bill.Item_Code
GROUP BY Product_Category.Category_Name;


 