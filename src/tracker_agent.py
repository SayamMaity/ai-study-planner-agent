class TrackerAgent:
    def __init__(self, memory_bank):
        self.memory = memory_bank

    def record_session(self, user_id, session_summary):
        entry = {'user': user_id, 'summary': session_summary}
        self.memory.add_session_entry(entry)
        # Simple skill update heuristic
        topic = session_summary.get('topic')
        if topic and session_summary.get('completed'):
            self.memory.update_skill(topic, 1)
        return True

    def get_history(self, n=10):
        return self.memory.get_summary(n)
