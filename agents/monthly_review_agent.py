from datetime import date
from state import get_leads, get_plan

def handle(request):
    today = date.today().isoformat()

    leads = get_leads()
    plan = get_plan()

    # ---- Lead Metrics ----
    total_leads = len(leads)
    category_counts = {
        "hot": 0,
        "warm": 0,
        "cold": 0,
        "inactive": 0
    }
    escalated = 0
    stalled = 0

    for lead in leads:
        category = lead.get("category", "cold")
        flags = lead.get("flags", [])

        if category in category_counts:
            category_counts[category] += 1

        if "auto_escalated_to_hot" in flags:
            escalated += 1

        if "stalled" in flags:
            stalled += 1

    # ---- Execution Metrics ----
    planned = 0
    completed = 0

    if plan:
        for task in plan.get("tasks", []):
            planned += 1
            if task.get("status") == "done":
                completed += 1

    completion_rate = (
        round((completed / planned) * 100, 2)
        if planned > 0 else 0
    )

    # ---- Signals ----
    signals = []

    if category_counts["hot"] > category_counts["warm"]:
        signals.append("Pipeline heating up")

    if stalled > 0:
        signals.append("Attention required: stalled hot leads")

    if completion_rate < 70:
        signals.append("Execution discipline needs improvement")

    if not signals:
        signals.append("Operations stable")

    return {
        "month": today[:7],
        "lead_metrics": {
            "total": total_leads,
            "by_category": category_counts,
            "escalated": escalated,
            "stalled_hot": stalled
        },
        "execution_metrics": {
            "tasks_planned": planned,
            "tasks_completed": completed,
            "completion_rate_percent": completion_rate
        },
        "signals": signals
    }
