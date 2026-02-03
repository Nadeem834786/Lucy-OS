from state import CURRENT_PLAN

def handle(request):
    """
    Deterministic planning agent.
    No AI. No guessing. Fixed structure.
    """
    plan = {
        "plan_id": "plan-demo-001",
        "plan_type": "daily",
        "date_range": "03-Feb-2026",
        "owner": "Nadeem Ahmed",

        "tasks": [
            {
                "task_id": "t-001",
                "title": "Morning lead follow-ups",
                "time_block": "10:00–11:00 IST",
                "priority": "P1",
                "dependency": "",
                "buffer_minutes": 10,
                "expected_outcome": "Reconnect with warm leads",
                "status": "planned"
            },
            {
                "task_id": "t-002",
                "title": "Site visit – Project review",
                "time_block": "12:00–14:00 IST",
                "priority": "P1",
                "dependency": "",
                "buffer_minutes": 30,
                "expected_outcome": "Client walkthrough completed",
                "status": "planned"
            }
        ],

        "assumptions": [
            "No meetings before 10:00 IST",
            "Travel time between locations is 30 minutes"
        ]
    }

    # publish plan to shared state
    global CURRENT_PLAN
    CURRENT_PLAN = plan

    return plan