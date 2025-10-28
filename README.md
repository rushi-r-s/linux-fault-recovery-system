# Linux Fault Detection & Recovery System

This project is a small Python-based daemon that watches Linux system logs and automatically reacts to faults.  
It detects kernel crashes, I/O errors, and service failures, then tries to recover from them (for example, restarting a failed service or remounting a disk).  
All detected events are stored in a small SQLite database for later review or MTTR analysis.

---

## Why I built this

While experimenting with Linux monitoring scripts, I realized that detecting recurring system issues manually takes too much time.  
This tool is a lightweight “self-healing” process that can run in the background and take immediate recovery actions instead of waiting for human intervention.

---

## Features

- Monitors `/var/log/syslog` or `journalctl -f` in real time  
- Detects kernel panics, I/O errors, or service-related crashes using regex rules  
- Runs recovery actions like:
  - Restarting systemd services  
  - Remounting affected volumes  
  - Isolating unstable network interfaces  
- Saves all detected incidents in an SQLite file (`events.db`)  
- Includes demo mode with fake logs to run on any OS

---

## How to run

```bash
# set up environment
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
To start the demo:

bash
Copy code
# start daemon using sample log
python fault_recovery/daemon.py --rules config/rules.yaml --logfile logs/syslog_demo.log

# in another terminal, simulate faults
bash scripts/generate_demo_logs.sh
Detected issues will appear in the console and get recorded in events.db.

Example output
less
Copy code
[INFO] Monitoring started (rules: 3)
[DETECT] I/O error found in log
[ACTION] remount_volume on /data
[DETECT] Kernel panic detected
[ACTION] restart_service critical-daemon.service
Config file (config/rules.yaml)
Example:

yaml
Copy code
rules:
  - id: kernel_panic
    match: "kernel panic|BUG:"
    action: restart_service
    service: critical-daemon.service

  - id: io_error
    match: "I/O error"
    action: remount_volume
    mount: /data

  - id: service_failed
    match: "Unit .* failed"
    action: restart_service
    service: target.service
You can add or edit these rules anytime — the daemon will reload them automatically on restart.

Future ideas
Add email or Slack alerts for critical events

Add Prometheus exporter for monitoring metrics

Build a small dashboard to visualize recovery statistics

Try anomaly detection over historical logs

Author
Rushikesh Rajendra Suryawanshi
Linux | Python | Monitoring | Automation
github.com/rushi-r-s

