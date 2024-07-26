-- USE alx_book_store;
-- SELECT 
--     COLUMN_NAME, 
--     DATA_TYPE, 
--     IS_NULLABLE, 
--     COLUMN_DEFAULT, 
--     CHARACTER_MAXIMUM_LENGTH, 
--     NUMERIC_PRECISION 
-- FROM 
--     INFORMATION_SCHEMA.COLUMNS 
-- WHERE 
--     TABLE_SCHEMA = 'alx_book_store' 
--     AND TABLE_NAME = 'customers';

INSERT INTO customers (customer_id, customer_name, email, address)
VALUES 
('1',  'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');