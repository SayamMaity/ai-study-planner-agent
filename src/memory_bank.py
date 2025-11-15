import json, time

class MemoryBank:
    def __init__(self, user_id):
        self.user_id = user_id
        self.store = {"preferences": {}, "history": [], "skills": {}, "stats": {}}

    def save_preference(self, k, v):
        self.store['preferences'][k] = v

    def add_session_entry(self, entry):
        entry['timestamp'] = time.time()
        self.store['history'].append(entry)

    def update_skill(self, topic, score_delta):
        self.store['skills'].setdefault(topic, 0)
        self.store['skills'][topic] += score_delta

    def get_summary(self, n=10):
        # Return compacted summary
        return self.store['history'][-n:]

    def compact_context(self, max_items=20):
        # Keep only the most recent items and aggregate older ones
        if len(self.store['history']) <= max_items:
            return
        self.store['history'] = self.store['history'][-max_items:]

    def to_json(self):
        return json.dumps(self.store, indent=2)
