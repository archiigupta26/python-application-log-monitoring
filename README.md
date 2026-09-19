# Python Application Log Monitoring & Alerting Tool

## Overview

A Python-based application monitoring tool that analyzes application logs, detects errors and warnings, identifies recurring failures, performs basic root cause analysis, stores incident information in MySQL, and generates alerts and health reports.

The project is designed to support application monitoring and troubleshooting by helping identify issues from log data and organize incident information for analysis.

## Features

- Parses application log files
- Detects errors and warnings
- Identifies recurring failures
- Classifies application incidents
- Performs basic root cause analysis
- Stores incident data in MySQL
- Generates alerts for detected issues
- Generates application health reports
- Exports reports in CSV format

## Technologies

- Python
- MySQL
- SQL
- CSV
- Git
- GitHub

## Project Structure

```text
python-application-log-monitoring/
│
├── logs/
├── reports/
├── src/
│   ├── log_parser/
│   ├── database/
│   ├── incident_detector/
│   ├── alert_manager/
│   ├── report_generator/
│   └── root_cause/
│
├── main.py
├── requirements.txt
└── README.md
```

## How It Works

```text
Application Logs
       ↓
   Log Parser
       ↓
Error / Warning Detection
       ↓
Incident Detection
       ↓
Root Cause Analysis
       ↓
MySQL Storage
       ↓
Alerts & Health Reports
```

## Use Cases

- Application log monitoring
- Incident identification
- Recurring error detection
- Basic troubleshooting and root cause analysis
- Application health reporting
- Incident data management

## Future Improvements

- Add a web-based monitoring dashboard
- Add email or notification-based alerts
- Add more advanced root cause analysis
- Add automated unit and integration tests
- Add real-time log monitoring

## Author

**Archi Gupta**

GitHub: https://github.com/archiigupta26
