from state import CURRENT_PLAN

def handle(request):
    if CURRENT_PLAN is None:
        return {
            "digest_type": request.get("digest_type"),
            "date": "03-Feb-2026",
            "notes": "No plan available for today."
        }

    tasks = CURRENT_PLAN.get("tasks", [])
    digest_type = request.get("digest_type")

    if digest_type == "AM":
        return {
            "digest_type": "AM",
            "date": CURRENT_PLAN.get("date_range"),
            "top_focus": [task["title"] for task in tasks[:3]],
            "schedule_blocks": [
                f'{task["time_block"]} {task["title"]}' for task in tasks
            ],
            "notes": "Day planned from active schedule."
        }

    if digest_type == "PM":
        completed = [t["title"] for t in tasks if t["status"] == "done"]
        pending = [t["title"] for t in tasks if t["status"] != "done"]

        return {
            "digest_type": "PM",
            "date": CURRENT_PLAN.get("date_range"),
            "completed": completed,
            "pending": pending,
            "notes": "End-of-day summary generated from plan."
        }

    return None
