from src.memory_bank import MemoryBank
from src.planner_agent import generate_weekly_plan
from src.qa_agent import answer_question_stub
from src.tracker_agent import TrackerAgent

class Orchestrator:
    def __init__(self, user_id):
        self.mem = MemoryBank(user_id)
        self.tracker = TrackerAgent(self.mem)

    def create_plan(self, subjects, hours_per_week, constraints=None):
        plan = generate_weekly_plan(subjects, hours_per_week, constraints)
        return plan

    def ask_question(self, subject, question):
        return answer_question_stub(subject, question)

    def record(self, session_summary):
        return self.tracker.record_session(self.mem.user_id, session_summary)

    def get_memory(self):
        return self.mem.to_json()
