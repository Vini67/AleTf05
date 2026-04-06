CREATE TABLE metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service VARCHAR(50),
    status VARCHAR(20),
    response_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);