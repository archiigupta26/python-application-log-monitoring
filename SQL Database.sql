CREATE DATABASE log_monitoring;
USE log_monitoring;

CREATE TABLE incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    level VARCHAR(20),
    message TEXT,
    severity VARCHAR(20),
    occurrence_count INT DEFAULT 1
);

SHOW TABLES;
DESCRIBE incidents;

USE log_monitoring;
SELECT * FROM incidents;

USE log_monitoring;
ALTER TABLE incidents
ADD COLUMN fingerprint VARCHAR(64);
ALTER TABLE incidents
ADD UNIQUE (fingerprint);

DESCRIBE incidents;
SELECT * FROM incidents;

USE log_monitoring;

ALTER TABLE incidents
ADD COLUMN root_cause VARCHAR(255);

SELECT
    id,
    message,
    severity,
    occurrence_count,
    root_cause
FROM incidents;

USE log_monitoring;

TRUNCATE TABLE incidents;
SELECT COUNT(*) FROM incidents;

SELECT COUNT(*) FROM incidents;

SELECT
    message,
    severity,
    occurrence_count,
    root_cause
FROM incidents;


