import json
import random
from datetime import datetime, timedelta

EVENT_TYPES = ["commit", "pull_request", "build", "deployment", "issue"]

def generate_events(n=10000):
    events = []
    start_time = datetime.now() - timedelta(days=30)

    for i in range(n):
        event_type = random.choice(EVENT_TYPES)
        timestamp = start_time + timedelta(minutes=random.randint(0, 60*24*30))

        event = {
            "event_id": i,
            "event_type": event_type,
            "timestamp": timestamp.isoformat(),
            "service": random.choice(["auth", "payments", "api", "frontend"]),
            "status": random.choice(["success", "failure"]) if event_type in ["build", "deployment"] else "ok",
            "latency_ms": random.randint(50, 2000)
        }

        events.append(event)

    return events


def save_events(path="data/raw_events.json", n=10000):
    events = generate_events(n)

    with open(path, "w") as f:
        json.dump(events, f, indent=2)

    print(f"Generated {n} events → {path}")


if __name__ == "__main__":
    save_events()