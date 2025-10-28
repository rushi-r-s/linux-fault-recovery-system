import re

def compile_rules(rules):
    compiled = []
    for r in rules:
        rx = re.compile(r.get("match", ""), re.IGNORECASE)
        compiled.append((r["id"], r, rx))
    return compiled

def evaluate_line(line, compiled_rules):
    for rid, rule, rx in compiled_rules:
        if rx.search(line):
            return rid, rule
    return None
