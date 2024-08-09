-- Step 1: Create a new test database
CREATE DATABASE IF NOT EXISTS test_db;
-- Step 2: Use the test database
USE test_db;
-- Step 3: Create a test table
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
-- Step 4: Insert some sample data into the test table
INSERT INTO test_table (name, age)
VALUES ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 22);
-- Step 5: Select the data from the test table to verify the insert
SELECT *
FROM test_table;