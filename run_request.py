from orchestrator import route_request
from agents.planning_agent import handle as planning_handle
from agents.lead_intelligence_agent import handle as lead_handle
from agents.task_update_agent import handle as task_update_handle
from agents.daily_digest_agent import handle as digest_handle
from utils.schema_validator import validate_schema
from agents.weekly_planning_agent import handle as weekly_handle
from agents.lead_aging_agent import handle as lead_aging_handle
from agents.monthly_review_agent import handle as monthly_review_handle

# STEP 1 — Create today's plan
planning_handle({
    "request_id": "req-plan",
    "classified_intent": "planning"
})

# STEP 2 — New lead comes in
lead_request = {
    "request_id": "req-lead-001",
    "classified_intent": "lead",
    "lead_id": "lead-001",
    "client_name": "Ramesh",
    "source": "instagram",
    "budget_range": "30-35L",
    "timeline_days": 20
}

lead_route = route_request(lead_request)
lead_result = lead_handle(lead_request)

is_valid, message = validate_schema(
    lead_route["schema"],
    lead_result
)

print("\nQualified Lead:", lead_result)
print("Validation:", message)

# STEP 3 — AM Digest
am_request = {
    "request_id": "req-am",
    "classified_intent": "daily_digest",
    "digest_type": "AM"
}

am_route = route_request(am_request)
am_result = digest_handle(am_request)

print("\nAM Digest:", am_result)

# STEP 4 — PM Digest
pm_request = {
    "request_id": "req-pm",
    "classified_intent": "daily_digest",
    "digest_type": "PM"
}

pm_route = route_request(pm_request)
pm_result = digest_handle(pm_request)

print("\nPM Digest:", pm_result)

# STEP 5 — Weekly Planning
weekly_request = {
    "request_id": "req-weekly",
    "classified_intent": "weekly_planning"
}

weekly_result = weekly_handle(weekly_request)

print("\nWEEKLY PLAN:")
print("Week:", weekly_result["week_start"], "to", weekly_result["week_end"])
print("Top 5 Goals:")
for g in weekly_result["top_5_goals"]:
    print("-", g)

print("\nRollover Tasks:")
for t in weekly_result["rollover_tasks"]:
    print("-", t)

print("\nRevenue Focus:")
for r in weekly_result["revenue_focus"]:
    print("-", r)

# STEP — Lead Aging & Escalation
aging_request = {
    "request_id": "req-aging",
    "classified_intent": "lead_aging"
}

aging_result = lead_aging_handle(aging_request)

print("\nLEAD AGING RESULT:")
print("Checked Date:", aging_result["checked_date"])
print("Escalations:")
for e in aging_result["escalations"]:
    print("-", e)

# STEP — Monthly Review
monthly_request = {
    "request_id": "req-monthly",
    "classified_intent": "monthly_review"
}

monthly_result = monthly_review_handle(monthly_request)

print("\nMONTHLY REVIEW")
print("Month:", monthly_result["month"])

print("\nLead Metrics:")
print("Total:", monthly_result["lead_metrics"]["total"])
print("By Category:", monthly_result["lead_metrics"]["by_category"])
print("Escalated:", monthly_result["lead_metrics"]["escalated"])
print("Stalled Hot:", monthly_result["lead_metrics"]["stalled_hot"])

print("\nExecution Metrics:")
print("Tasks Planned:", monthly_result["execution_metrics"]["tasks_planned"])
print("Tasks Completed:", monthly_result["execution_metrics"]["tasks_completed"])
print("Completion Rate:",
      monthly_result["execution_metrics"]["completion_rate_percent"], "%")

print("\nSignals:")
for s in monthly_result["signals"]:
    print("-", s)