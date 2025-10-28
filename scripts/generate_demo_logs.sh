#!/usr/bin/env bash
set -euo pipefail
LOG=logs/syslog_demo.log
mkdir -p logs
: > "$LOG"
echo "kernel: everything nominal" >> "$LOG"
sleep 0.2
echo "systemd[1]: Starting target service..." >> "$LOG"
sleep 0.2
echo "nvme0n1: I/O error, dev nvme0n1, sector 12345 op 0x0:(READ)" >> "$LOG"
sleep 0.2
echo "kernel: BUG: soft lockup - CPU#3 stuck for 22s!" >> "$LOG"
sleep 0.2
echo "systemd[1]: Failed to start target.service - Unit target.service failed." >> "$LOG"
echo "[OK] Demo faults appended to $LOG"
