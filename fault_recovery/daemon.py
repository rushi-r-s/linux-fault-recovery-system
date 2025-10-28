import argparse, time, yaml
from pathlib import Path
from fault_recovery.filters import compile_rules, evaluate_line
from fault_recovery.actions import perform_action
from fault_recovery.storage import EventStore

def tail_file(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    with path.open("r", errors="ignore") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.25); continue
            yield line.rstrip("\n")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules", default="config/rules.yaml")
    ap.add_argument("--logfile", default="logs/syslog_demo.log")
    args = ap.parse_args()

    with open(args.rules, "r") as f:
        rules_cfg = yaml.safe_load(f)
    rules = compile_rules(rules_cfg.get("rules", []))
    store = EventStore("events.db")
    print(f"[INFO] Loaded {len(rules)} rules. Tailing: {args.logfile}")

    for line in tail_file(Path(args.logfile)):
        hit = evaluate_line(line, rules)
        if hit:
            rid, rule = hit
            print(f"[DETECT] rule={rid} line={line[:160]}")
            store.record(rid, line)
            try:
                perform_action(rule)
            except Exception as e:
                print(f"[WARN] action failed for rule={rid}: {e}")
