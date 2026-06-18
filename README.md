# 1stdreamproject (DreamNotify)

DreamNotify is a Python-based resource monitoring and notification tool. It monitors system resources (like CPU, memory, and disk usage) or specific URLs, and sends alerts to the configured email when thresholds are exceeded or services become unavailable.

## Features
- System resource monitoring (CPU, RAM, Disk).
- URL/Service availability checks.
- Email notifications based on `config.yaml` settings.
- Configurable thresholds and check intervals.

## Getting Started
### Prerequisites
- Python 3.8+
- Dependencies listed in `requirements.txt`

### Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure `config.yaml` with your notification preferences.
4. Run the application: `python src/main.py`.