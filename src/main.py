import yaml
import psutil
import time
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def check_resources(config: Dict[str, Any]):
    monitoring = config.get('monitoring', {})
    cpu_limit = monitoring.get('cpu_threshold', 90)
    mem_limit = monitoring.get('memory_threshold', 90)

    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    logging.info(f"CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")

    if cpu_usage > cpu_limit:
        send_notification(config, f"High CPU usage detected: {cpu_usage}%")

    if mem_usage > mem_limit:
        send_notification(config, f"High Memory usage detected: {mem_usage}%")

def send_notification(config: Dict[str, Any], message: str):
    email = config.get('notification', {}).get('email')
    logging.warning(f"NOTIFICATION to {email}: {message}")
    # In a real app, this would use an SMTP library or API to send an actual email.

def main():
    config = load_config('config.yaml')
    interval = config.get('monitoring', {}).get('check_interval', 60)

    logging.info("DreamNotify started.")
    try:
        while True:
            check_resources(config)
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("DreamNotify stopped.")

if __name__ == "__main__":
    main()
