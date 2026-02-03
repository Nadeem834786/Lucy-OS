def route_request(request):
    intent = request.get("classified_intent")

    if intent == "finance":
        return {
            "agent": "finance_logging_agent",
            "schema": "schemas/finance_log.schema.json"
        }

    if intent == "planning":
        return {
            "agent": "planning_agent",
            "schema": "schemas/planning.schema.json"
        }

    if intent == "lead":
        return {
            "agent": "lead_intelligence_agent",
            "schema": "schemas/lead_intelligence.schema.json"
        }

    if intent == "daily_digest":
        return {
            "agent": "daily_digest_agent",
            "schema": "schemas/daily_digest.schema.json"
        }

    return {
        "agent": None,
        "schema": None
    }

