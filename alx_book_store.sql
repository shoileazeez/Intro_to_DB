CREATE DATABASE IF NOT EXISTS alx_book_store

CREATE TABLE Books (
    bookID INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors_table(author_id),
    price FLOAT,
     publication_date DATE
);

CREATE TABLE example_table (
    id INT PRIMARY KEY,
    value FLOAT
);


CREATE TABLE Authors(
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);


CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);

CREATE TABLE Order_Details(
    order_details_id INT PRIMARY KEY,
    order_id INT,
    Foreign Key (order_id) REFERENCES Orders_table(order_id),
    book_id INT,
    Foreign Key (book_id) REFERENCES Books_table(book_id),
    quantity FLOAT 
);
