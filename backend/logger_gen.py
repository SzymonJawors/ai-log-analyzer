import time
import random
from datetime import datetime

LOG_FILE = "app_logs.log"

log_scenarios = {
    "INFO": [
        "User 'admin_dev' authenticated via OAuth2 provider",
        "Microservice 'payment-gateway' health check: UP (200 OK)",
        "Automatic database backup to AWS S3 completed successfully",
        "New SSL certificate deployed for domain: api.secure-logs.com",
        "Kubernetes pod 'auth-api-v2' successfully rescheduled"
    ],
    "WARNING": [
        "Unusual traffic spike detected from region: RU (12.4 requests/sec)",
        "API rate limit reached for user: guest_1029",
        "Disk latency on /dev/sdb exceeding 200ms",
        "Deprecated API endpoint /v1/login accessed by legacy-client",
        "High memory consumption in 'pdf-worker' container (82%)"
    ],
    "ERROR": [
        "SQL Injection attempt detected in query: SELECT * FROM users WHERE id = '1' OR '1'='1'",
        "SSH Brute-force attack detected from IP 45.12.88.22 (50 attempts)",
        "CRITICAL: Failed to decrypt JWT token - Invalid signature detected",
        "FATAL: Database master-slave replication sync broken",
        "Access denied: User 'test_user' tried to access '/etc/passwd' via path traversal"
    ]
}

levels = ["INFO", "WARNING", "ERROR"]

print(f"Generating logs to {LOG_FILE}")
print(f"CTRL + C to stop")

try:
    while True:
        level = random.choices(["INFO", "WARNING", "ERROR"],
                               weights=[60, 25, 15],
                               k=1)[0]
        msg = random.choice(log_scenarios[level])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {msg}\n"
        
        with open(LOG_FILE, "a", encoding="utf-8") as f:         
            f.write(log_entry)
            
        print(f"Added: {log_entry.strip()}")
        time.sleep(random.uniform(3, 7))
except KeyboardInterrupt:
    print("\nGen stopped")