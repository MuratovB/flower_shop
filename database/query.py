query = """
-- Enable foreign key support in SQLite
PRAGMA foreign_keys = ON;
-- -----------------------------------------------------
-- Table `ClientType`
-- -----------------------------------------------------
CREATE TABLE ClientType (
    ClientTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    LegalEntity VARCHAR(45) NOT NULL,
    Individual VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `ContactType`
-- -----------------------------------------------------
CREATE TABLE ContactType (
    ContactTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    ContactTypeName VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Contacts`
-- -----------------------------------------------------
CREATE TABLE Contacts (
    ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
    ContactInfo VARCHAR(45) NULL,
    ContactTypeID INTEGER NOT NULL,
    FOREIGN KEY (ContactTypeID) REFERENCES ContactType(ContactTypeID)
);
CREATE INDEX IX_Contacts_ContactType ON Contacts(ContactTypeID);
-- -----------------------------------------------------
-- Table `District`
-- -----------------------------------------------------
CREATE TABLE District (
    DistrictID INTEGER PRIMARY KEY AUTOINCREMENT,
    District VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Client`
-- -----------------------------------------------------
CREATE TABLE Client (
    ClientID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    ClientTypeID INTEGER NOT NULL,
    ContactID INTEGER NOT NULL,
    DistrictID INTEGER NOT NULL,
    Discount INTEGER NULL,
    RegistrationDate VARCHAR(45) NULL,
    Workplace VARCHAR(45) NULL,
    Position VARCHAR(45) NULL,
    PassportNumber VARCHAR(45) NULL,
    Login VARCHAR(45) NULL,
    Password VARCHAR(100) NULL,
    FOREIGN KEY (ClientTypeID) REFERENCES ClientType(ClientTypeID),
    FOREIGN KEY (ContactID) REFERENCES Contacts(ContactID),
    FOREIGN KEY (DistrictID) REFERENCES District(DistrictID)
);
CREATE INDEX IX_Client_ClientType ON Client(ClientTypeID);
CREATE INDEX IX_Client_Contacts ON Client(ContactID);
CREATE INDEX IX_Client_District ON Client(DistrictID);
-- -----------------------------------------------------
-- Table `OrderType`
-- -----------------------------------------------------
CREATE TABLE OrderType (
    OrderTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Wholesale VARCHAR(100) NOT NULL,
    Retail VARCHAR(100) NOT NULL
);
-- -----------------------------------------------------
-- Table `DiscountType`
-- -----------------------------------------------------
CREATE TABLE DiscountType (
    DiscountTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EventName VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `EventType`
-- -----------------------------------------------------
CREATE TABLE EventType (
    EventTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    EventTypeName VARCHAR(100) NULL
);
-- -----------------------------------------------------
-- Table `Events`
-- -----------------------------------------------------
CREATE TABLE Events (
    EventID INTEGER PRIMARY KEY AUTOINCREMENT,
    EventName VARCHAR(100) NULL,
    EventTypeID INTEGER NOT NULL,
    Comment VARCHAR(45) NULL,
    FOREIGN KEY (EventTypeID) REFERENCES EventType(EventTypeID)
);
CREATE INDEX IX_Events_EventType ON Events(EventTypeID);
-- -----------------------------------------------------
-- Table `Discount`
-- -----------------------------------------------------
CREATE TABLE Discount (
    DiscountID INTEGER PRIMARY KEY AUTOINCREMENT,
    DiscountValue INTEGER NOT NULL,
    DiscountTypeID INTEGER NOT NULL,
    EventID INTEGER NOT NULL,
    FOREIGN KEY (DiscountTypeID) REFERENCES DiscountType(DiscountTypeID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);
CREATE INDEX IX_Discount_DiscountType ON Discount(DiscountTypeID);
CREATE INDEX IX_Discount_Events ON Discount(EventID);
-- -----------------------------------------------------
-- Table `OrderStatus`
-- -----------------------------------------------------
CREATE TABLE OrderStatus (
    OrderStatusID INTEGER PRIMARY KEY AUTOINCREMENT,
    InProgress VARCHAR(45) NOT NULL,
    Completed VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Position`
-- -----------------------------------------------------
CREATE TABLE Position (
    PositionID INTEGER PRIMARY KEY AUTOINCREMENT,
    PositionName VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Employee`
-- -----------------------------------------------------
CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Salary INTEGER NULL,
    RegistrationDate VARCHAR(45) NULL,
    Phone INTEGER NULL,
    Login VARCHAR(45) NULL,
    Password VARCHAR(45) NULL,
    PositionID INTEGER NOT NULL,
    FOREIGN KEY (PositionID) REFERENCES Position(PositionID)
);
CREATE INDEX IX_Employee_Position ON Employee(PositionID);
-- -----------------------------------------------------
-- Table `Order`
-- -----------------------------------------------------
CREATE TABLE "Order" (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClientID INTEGER NOT NULL,
    OrderTypeID INTEGER NOT NULL,
    DiscountID INTEGER NOT NULL,
    OrderStatusID INTEGER NOT NULL,
    OrderDate DATE NULL,
    InvoiceNumber VARCHAR(45) NULL,
    Comment VARCHAR(45) NULL,
    EmployeeID INTEGER NOT NULL,
    FOREIGN KEY (ClientID) REFERENCES Client(ClientID),
    FOREIGN KEY (OrderTypeID) REFERENCES OrderType(OrderTypeID),
    FOREIGN KEY (DiscountID) REFERENCES Discount(DiscountID),
    FOREIGN KEY (OrderStatusID) REFERENCES OrderStatus(OrderStatusID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
CREATE INDEX IX_Order_Client ON "Order"(ClientID);
CREATE INDEX IX_Order_OrderType ON "Order"(OrderTypeID);
CREATE INDEX IX_Order_Discount ON "Order"(DiscountID);
CREATE INDEX IX_Order_OrderStatus ON "Order"(OrderStatusID);
CREATE INDEX IX_Order_Employee ON "Order"(EmployeeID);
-- -----------------------------------------------------
-- Table `PaymentType`
-- -----------------------------------------------------
CREATE TABLE PaymentType (
    PaymentTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Cash VARCHAR(45) NOT NULL,
    Card VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Payment`
-- -----------------------------------------------------
CREATE TABLE Payment (
    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PaymentTypeID INTEGER NOT NULL,
    Amount INTEGER NULL,
    PaymentDate VARCHAR(45) NULL,
    Comment VARCHAR(45) NULL,
    OrderID INTEGER NOT NULL,
    FOREIGN KEY (PaymentTypeID) REFERENCES PaymentType(PaymentTypeID),
    FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID)
);
CREATE INDEX IX_Payment_PaymentType ON Payment(PaymentTypeID);
CREATE INDEX IX_Payment_Order ON Payment(OrderID);
-- -----------------------------------------------------
-- Table `Category`
-- -----------------------------------------------------
CREATE TABLE Category (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName VARCHAR(100) NOT NULL
);
-- -----------------------------------------------------
-- Table `Product`
-- -----------------------------------------------------
CREATE TABLE Product (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName VARCHAR(45) NOT NULL,
    ProductDescription VARCHAR(45) NOT NULL,
    RegistrationDate DATETIME NOT NULL,
    CategoryID INTEGER NOT NULL,
    Photo VARCHAR(45) NULL,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);
CREATE INDEX IX_Product_Category ON Product(CategoryID);
-- -----------------------------------------------------
-- Table `DeliveryType`
-- -----------------------------------------------------
CREATE TABLE DeliveryType (
    DeliveryTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Urgent VARCHAR(45) NOT NULL,
    Contractual VARCHAR(45) NOT NULL
);
-- -----------------------------------------------------
-- Table `Supplier`
-- -----------------------------------------------------
CREATE TABLE Supplier (
    SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
    CompanyName VARCHAR(45) NULL,
    RegistrationDate DATETIME NULL,
    Comment VARCHAR(45) NULL
);
-- -----------------------------------------------------
-- Table `Delivery`
-- -----------------------------------------------------
CREATE TABLE Delivery (
    DeliveryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CompanyName VARCHAR(45) NOT NULL,
    DeliveryDate DATE NOT NULL,
    SupplierName VARCHAR(45) NOT NULL,
    Comment VARCHAR(45) NOT NULL,
    DeliveryTypeID INTEGER NOT NULL,
    InvoiceNumber INTEGER NULL,
    SupplierID INTEGER NOT NULL,
    FOREIGN KEY (DeliveryTypeID) REFERENCES DeliveryType(DeliveryTypeID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);
CREATE INDEX IX_Delivery_DeliveryType ON Delivery(DeliveryTypeID);
CREATE INDEX IX_Delivery_Supplier ON Delivery(SupplierID);
-- -----------------------------------------------------
-- Table `Warehouse`
-- -----------------------------------------------------
CREATE TABLE Warehouse (
    WarehouseID INTEGER PRIMARY KEY AUTOINCREMENT,
    WarehouseName VARCHAR(45) NULL
);
-- -----------------------------------------------------
-- Table `DeliveryList`
-- -----------------------------------------------------
CREATE TABLE DeliveryList (
    DeliveryListID INTEGER PRIMARY KEY AUTOINCREMENT,
    Quantity INTEGER NOT NULL,
    Price DECIMAL NOT NULL,
    DeliveryID INTEGER NOT NULL,
    WarehouseID INTEGER NOT NULL,
    Comment VARCHAR(45) NULL,
    ProductID INTEGER NOT NULL,
    FOREIGN KEY (DeliveryID) REFERENCES Delivery(DeliveryID),
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
CREATE INDEX IX_DeliveryList_Delivery ON DeliveryList(DeliveryID);
CREATE INDEX IX_DeliveryList_Warehouse ON DeliveryList(WarehouseID);
CREATE INDEX IX_DeliveryList_Product ON DeliveryList(ProductID);
-- -----------------------------------------------------
-- Table `PayoutType`
-- -----------------------------------------------------
CREATE TABLE PayoutType (
    PayoutTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    PayoutTypeName VARCHAR(45) NULL
);
-- -----------------------------------------------------
-- Table `Salary`
-- -----------------------------------------------------
CREATE TABLE Salary (
    SalaryID INTEGER PRIMARY KEY AUTOINCREMENT,
    SalaryAmount INTEGER NOT NULL,
    PaymentDate VARCHAR(45) NULL,
    Comment VARCHAR(45) NULL,
    Bonus INTEGER NULL,
    PayoutTypeID INTEGER NOT NULL,
    EmployeeID INTEGER NOT NULL,
    FOREIGN KEY (PayoutTypeID) REFERENCES PayoutType(PayoutTypeID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
CREATE INDEX IX_Salary_PayoutType ON Salary(PayoutTypeID);
CREATE INDEX IX_Salary_Employee ON Salary(EmployeeID);
-- -----------------------------------------------------
-- Table `OrderComposition`
-- -----------------------------------------------------
CREATE TABLE OrderComposition (
    OrderCompositionID INTEGER PRIMARY KEY AUTOINCREMENT,
    DeliveryListID INTEGER NOT NULL,
    OrderID INTEGER NOT NULL,
    Quantity INTEGER NULL,
    DiscountedPrice INTEGER NULL,
    FOREIGN KEY (DeliveryListID) REFERENCES DeliveryList(DeliveryListID),
    FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID)
);
CREATE INDEX IX_OrderComposition_DeliveryList ON OrderComposition(DeliveryListID);
CREATE INDEX IX_OrderComposition_Order ON OrderComposition(OrderID);
-- -----------------------------------------------------
-- Table `PriceList`
-- -----------------------------------------------------
CREATE TABLE PriceList (
    PriceListID INTEGER PRIMARY KEY AUTOINCREMENT,
    Comment VARCHAR(45) NOT NULL,
    Price INTEGER NOT NULL,
    ChangeDate DATETIME NULL,
    ProductID INTEGER NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
CREATE INDEX IX_PriceList_Product ON PriceList(ProductID);
-- -----------------------------------------------------
-- Table `Report`
-- -----------------------------------------------------
CREATE TABLE Report (
    ReportID INTEGER PRIMARY KEY AUTOINCREMENT,
    DateTime DATETIME NOT NULL,
    FormName VARCHAR(45) NULL,
    ReportName VARCHAR(45) NULL
);
-- -----------------------------------------------------
-- Table `Tax`
-- -----------------------------------------------------
CREATE TABLE Tax (
    TaxID INTEGER PRIMARY KEY AUTOINCREMENT,
    TaxRate INTEGER NULL,
    TaxName VARCHAR(45) NULL,
    Comment VARCHAR(45) NULL
);
-- -----------------------------------------------------
-- Table `DeliveryPayment`
-- -----------------------------------------------------
CREATE TABLE DeliveryPayment (
    DeliveryPaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
    Amount INTEGER NULL,
    PaymentTypeID INTEGER NOT NULL,
    DeliveryID INTEGER NOT NULL,
    PaymentDate DATETIME NULL,
    Comments VARCHAR(145) NULL,
    FOREIGN KEY (PaymentTypeID) REFERENCES PaymentType(PaymentTypeID),
    FOREIGN KEY (DeliveryID) REFERENCES Delivery(DeliveryID)
);
CREATE INDEX IX_DeliveryPayment_PaymentType ON DeliveryPayment(PaymentTypeID);
CREATE INDEX IX_DeliveryPayment_Delivery ON DeliveryPayment(DeliveryID);
-- -----------------------------------------------------
-- Table `ProductWriteOff`
-- -----------------------------------------------------
CREATE TABLE ProductWriteOff (
    WriteOffID INTEGER PRIMARY KEY AUTOINCREMENT,
    Comment VARCHAR(45) NULL,
    WriteOffDate VARCHAR(45) NULL,
    Quantity INTEGER NULL
);
-- Insert into ClientType
INSERT INTO ClientType (LegalEntity, Individual) 
VALUES 
('Corporation', 'Individual'),
('LLC', 'Personal');
-- Insert into ContactType
INSERT INTO ContactType (ContactTypeName)
VALUES 
('Email'),
('Phone'),
('Address');
-- Insert into District
INSERT INTO District (District)
VALUES 
('Central'),
('Northern'),
('Southern');
-- Insert into Contacts
INSERT INTO Contacts (ContactInfo, ContactTypeID)
VALUES 
('john.doe@email.com', 1),
('+1234567890', 2),
('123 Main St', 3);
-- Insert into Client
INSERT INTO Client (FirstName, LastName, ClientTypeID, ContactID, DistrictID, Discount, RegistrationDate, Workplace, Position, PassportNumber, Login, Password)
VALUES 
('John', 'Doe', 1, 1, 1, 5, '2023-01-15', 'ABC Corp', 'Manager', 'AB1234567', 'johndoe', 'password123'),
('Jane', 'Smith', 2, 2, 2, 10, '2023-02-20', 'XYZ LLC', 'Director', 'CD8910111', 'janesmith', 'securepass');
-- Insert into OrderType
INSERT INTO OrderType (Wholesale, Retail)
VALUES 
('Bulk orders', 'Single items'),
('Corporate', 'Individual');
-- Insert into DiscountType
INSERT INTO DiscountType (EventName)
VALUES 
('Seasonal Sale'),
('Loyalty Discount'),
('First Purchase');
-- Insert into EventType
INSERT INTO EventType (EventTypeName)
VALUES 
('Promotion'),
('Holiday'),
('Anniversary');
-- Insert into Events
INSERT INTO Events (EventName, EventTypeID, Comment)
VALUES 
('Summer Sale', 1, 'Annual summer promotion'),
('New Year', 2, 'Holiday discounts');
-- Insert into Discount
INSERT INTO Discount (DiscountValue, DiscountTypeID, EventID)
VALUES 
(15, 1, 1),
(20, 2, 2);
-- Insert into OrderStatus
INSERT INTO OrderStatus (InProgress, Completed)
VALUES 
('Processing', 'Delivered'),
('Packaging', 'Shipped');
-- Insert into Position
INSERT INTO Position (PositionName)
VALUES 
('Sales Manager'),
('Warehouse Staff'),
('Accountant');
-- Insert into Employee
INSERT INTO Employee (FirstName, LastName, Salary, RegistrationDate, Phone, Login, Password, PositionID)
VALUES 
('Mike', 'Johnson', 50000, '2022-05-10', 1234567890, 'mikej', 'emp123', 1),
('Sarah', 'Williams', 45000, '2022-06-15', 987654321, 'sarahw', 'emp456', 2);
-- Insert into Order
INSERT INTO "Order" (ClientID, OrderTypeID, DiscountID, OrderStatusID, OrderDate, InvoiceNumber, Comment, EmployeeID)
VALUES 
(1, 1, 1, 1, '2023-05-01', 'INV-001', 'First order', 1),
(2, 2, 2, 2, '2023-05-02', 'INV-002', 'Regular customer', 2);
-- Insert into PaymentType
INSERT INTO PaymentType (Cash, Card)
VALUES 
('Cash on delivery', 'Credit card'),
('Bank transfer', 'Debit card');
-- Insert into Payment
INSERT INTO Payment (PaymentTypeID, Amount, PaymentDate, Comment, OrderID)
VALUES 
(1, 15000, '2023-05-01', 'Full payment', 1),
(2, 20000, '2023-05-02', 'Partial payment', 2);
-- Insert into Category
INSERT INTO Category (CategoryName)
VALUES 
('Electronics'),
('Clothing'),
('Groceries');
-- Insert into Product
INSERT INTO Product (ProductName, ProductDescription, RegistrationDate, CategoryID, Photo)
VALUES 
('Laptop', 'High performance laptop', '2023-01-10 00:00:00', 1, 'laptop.jpg'),
('T-Shirt', 'Cotton t-shirt', '2023-02-15 00:00:00', 2, 'tshirt.jpg');
-- Insert into DeliveryType
INSERT INTO DeliveryType (Urgent, Contractual)
VALUES 
('24-hour', 'Monthly contract'),
('48-hour', 'Annual contract');
-- Insert into Supplier
INSERT INTO Supplier (CompanyName, RegistrationDate, Comment)
VALUES 
('Tech Supplies Inc', '2022-01-01 00:00:00', 'Main electronics supplier'),
('Fashion World', '2022-03-15 00:00:00', 'Clothing provider');
-- Insert into Warehouse
INSERT INTO Warehouse (WarehouseName)
VALUES 
('Main Warehouse'),
('Cold Storage');
-- Insert into Delivery
INSERT INTO Delivery (CompanyName, DeliveryDate, SupplierName, Comment, DeliveryTypeID, InvoiceNumber, SupplierID)
VALUES 
('Fast Delivery', '2023-04-01', 'Tech Supplies Inc', 'Electronics shipment', 1, 1001, 1),
('Standard Logistics', '2023-04-05', 'Fashion World', 'Clothing delivery', 2, 1002, 2);
-- Insert into DeliveryList
INSERT INTO DeliveryList (Quantity, Price, DeliveryID, WarehouseID, Comment, ProductID)
VALUES 
(50, 1000, 1, 1, 'Laptop batch', 1),
(200, 20, 2, 1, 'T-shirts', 2);
-- Insert into PayoutType
INSERT INTO PayoutType (PayoutTypeName)
VALUES 
('Salary'),
('Bonus'),
('Commission');
-- Insert into Salary
INSERT INTO Salary (SalaryAmount, PaymentDate, Comment, Bonus, PayoutTypeID, EmployeeID)
VALUES 
(50000, '2023-05-31', 'Monthly salary', 1000, 1, 1),
(45000, '2023-05-31', 'Monthly salary', 500, 1, 2);
-- Insert into OrderComposition
INSERT INTO OrderComposition (DeliveryListID, OrderID, Quantity, DiscountedPrice)
VALUES 
(1, 1, 1, 950),
(2, 2, 2, 38);
-- Insert into PriceList
INSERT INTO PriceList (Comment, Price, ChangeDate, ProductID)
VALUES 
('Standard price', 1000, '2023-01-01 00:00:00', 1),
('Sale price', 20, '2023-03-01 00:00:00', 2);
-- Insert into Report
INSERT INTO Report (DateTime, FormName, ReportName)
VALUES 
('2023-05-31 10:00:00', 'Sales', 'Monthly Sales Report'),
('2023-05-31 11:00:00', 'Inventory', 'Stock Level Report');
-- Insert into Tax
INSERT INTO Tax (TaxRate, TaxName, Comment)
VALUES 
(10, 'VAT', 'Value Added Tax'),
(5, 'Sales Tax', 'Local sales tax');
-- Insert into DeliveryPayment
INSERT INTO DeliveryPayment (Amount, PaymentTypeID, DeliveryID, PaymentDate, Comments)
VALUES 
(5000, 1, 1, '2023-04-02 00:00:00', 'Paid for electronics delivery'),
(2000, 2, 2, '2023-04-06 00:00:00', 'Paid for clothing delivery');
-- Insert into ProductWriteOff
INSERT INTO ProductWriteOff (Comment, WriteOffDate, Quantity)
VALUES 
('Damaged goods', '2023-04-15', 2),
('Expired items', '2023-04-20', 5);
"""