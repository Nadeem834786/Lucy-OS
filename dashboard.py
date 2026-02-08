import json
import os

DATA_DIR = "data"

def read_json(file, default):
    path = os.path.join(DATA_DIR, file)
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def divider(title):
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)

def dashboard():
    plan = read_json("plan.json", {})
    leads = read_json("leads.json", [])
    weekly = read_json("weekly_plan.json", {})

    # ---- TODAY ----
    divider("Today – Plan & Execution")

    if not plan:
        print("No active plan.")
    else:
        for task in plan.get("tasks", []):
            status = task.get("status", "planned").upper()
            print(f"[{status}] {task['time_block']} – {task['title']}")

    # ---- REVENUE ----
    divider("Revenue Focus")

    hot = [l for l in leads if l.get("category") == "hot"]
    warm = [l for l in leads if l.get("category") == "warm"]

    print(f"Hot Leads ({len(hot)}):")
    for l in hot:
        print("-", l.get("client_name"), "| Flags:", l.get("flags", []))

    print(f"\nWarm Leads ({len(warm)}):")
    for l in warm:
        print("-", l.get("client_name"))

    # ---- ESCALATIONS ----
    divider("Escalations")

    escalations = []
    for l in leads:
        for flag in l.get("flags", []):
            escalations.append(f"{flag.upper()} – {l.get('client_name')}")

    if escalations:
        for e in escalations:
            print("-", e)
    else:
        print("No active escalations.")

    # ---- WEEKLY ----
    divider("Weekly Overview")

    if weekly:
        print("Week:", weekly.get("week_start"), "→", weekly.get("week_end"))

        print("\nTop Goals:")
        for g in weekly.get("top_5_goals", []):
            print("-", g)

        print("\nRollover Tasks:")
        for t in weekly.get("rollover_tasks", []):
            print("-", t)

    else:
        print("No weekly plan found.")

    # ---- MONTHLY SIGNALS ----
    divider("Monthly Signals")

    # Derived on the fly (read-only)
    stalled = [l for l in leads if "stalled" in l.get("flags", [])]
    if stalled:
        print("Attention required:")
        for l in stalled:
            print("-", l.get("client_name"), "(STALLED)")
    else:
        print("No stalled hot leads.")

if __name__ == "__main__":
    dashboard()
