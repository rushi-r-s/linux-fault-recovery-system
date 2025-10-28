# Automated Linux Fault Detection & Recovery

Python daemon that tails logs, detects kernel/I/O/service faults via rules, triggers recovery actions, and stores incidents for MTTR analysis.

## Quick Start (cross-platform demo)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start the daemon (tails a demo log file)
python fault_recovery/daemon.py --rules config/rules.yaml --logfile logs/syslog_demo.log


