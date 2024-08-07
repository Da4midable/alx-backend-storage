-- This script creates a table 'users' with the specified requirements

-- Create the 'users' table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    -- The 'id' column: an integer that is never null, auto-increments, and is the primary key
    id INT NOT NULL AUTO_INCREMENT,
    -- The 'email' column: a string with a maximum length of 255 characters, never null and unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- The 'name' column: a string with a maximum length of 255 characters
    name VARCHAR(255),
    country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    -- Set 'id' as the primary key of the table
    PRIMARY KEY (id)
);
