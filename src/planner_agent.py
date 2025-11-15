from datetime import datetime, timedelta
import math

def generate_weekly_plan(subjects, hours_per_week, constraints=None):
    # Allocate hours proportional to subject weights (equal by default)
    days = 7
    subject_weights = {s: 1 for s in subjects}
    total_weight = sum(subject_weights.values())
    daily = hours_per_week / days
    plan = {}
    today = datetime.today()
    for i in range(days):
        day = str((today + timedelta(days=i)).date())
        plan[day] = []
        for s, w in subject_weights.items():
            hours = round(daily * (w/total_weight), 2)
            if hours <= 0: continue
            micro = [f"Learn core concepts of {s}", f"1 practice problem on {s}", f"Review notes for 10 minutes"]
            plan[day].append({'subject': s, 'hours': hours, 'micro_tasks': micro})
    return plan

# helper to pretty-print hours total
def total_planned_hours(plan):
    return round(sum(task['hours'] for tasks in plan.values() for task in tasks),2)
