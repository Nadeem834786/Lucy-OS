from orchestrator import route_request
from agents.planning_agent import handle as planning_handle
from agents.daily_digest_agent import handle as digest_handle
from utils.schema_validator import validate_schema

# STEP 1 — Generate today's plan
planning_request = {
    "request_id": "req-plan-001",
    "classified_intent": "planning"
}

planning_route = route_request(planning_request)
plan = planning_handle(planning_request)

print("Planning Output:", plan)

# STEP 2 — Generate AM Digest
am_request = {
    "request_id": "req-am-001",
    "classified_intent": "daily_digest",
    "digest_type": "AM"
}

am_route = route_request(am_request)
am_result = digest_handle(am_request)

is_valid, message = validate_schema(
    am_route["schema"],
    am_result
)

print("\nAM Digest:", am_result)
print("Validation:", message)

# STEP 3 — Generate PM Digest
pm_request = {
    "request_id": "req-pm-001",
    "classified_intent": "daily_digest",
    "digest_type": "PM"
}

pm_route = route_request(pm_request)
pm_result = digest_handle(pm_request)

is_valid, message = validate_schema(
    pm_route["schema"],
    pm_result
)

print("\nPM Digest:", pm_result)
print("Validation:", message)
