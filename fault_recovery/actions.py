import platform, subprocess

def _is_linux():
    return platform.system().lower() == "linux"

def perform_action(rule: dict):
    action = rule.get("action")
    if action == "restart_service":
        restart_service(rule.get("service"))
    elif action == "remount_volume":
        remount_volume(rule.get("mount"))
    elif action == "isolate_nic":
        isolate_nic(rule.get("nic"))
    else:
        print(f"[INFO] no-op action for rule={rule.get('id')}")

def restart_service(service: str|None):
    if not service:
        print("[INFO] restart_service (no service specified)"); return
    if _is_linux():
        subprocess.call(["systemctl", "restart", service])
    print(f"[ACTION] restart_service {service}")

def remount_volume(mount: str|None):
    if not mount:
        print("[INFO] remount_volume (no mount specified)"); return
    if _is_linux():
        subprocess.call(["mount", "-o", "remount", mount])
    print(f"[ACTION] remount_volume {mount}")

def isolate_nic(nic: str|None):
    if not nic:
        print("[INFO] isolate_nic (no nic specified)"); return
    if _is_linux():
        subprocess.call(["ip", "link", "set", nic, "down"])
    print(f"[ACTION] isolate_nic {nic}")
