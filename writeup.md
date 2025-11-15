Study Planner + Learning Assistant Agent

Problem.
Many learners struggle to plan study time, maintain consistency, and adapt based on performance. This project builds an agent-native solution combining planning, tutoring, and tracking to automate and personalize learning.

Solution.
A multi-agent system: Planner Agent (creates schedules), QA Agent (answers questions and creates micro-exercises), Tracker Agent (records progress and updates Memory Bank). The orchestrator routes requests, keeps session state, and aggregates outputs for the user.

Features.
- Multi-agent orchestration
- Tools: Python execution for planning logic; stubs for web search and LLM calls
- Sessions & long-term memory with context compaction
- Observability: logs + simple metrics
- Evaluation: simulated user scenarios and unit tests

How to run.
1. Open the notebook `notebooks/01_build_agent.ipynb` on Kaggle or locally.
2. Install requirements from `requirements.txt`.
3. Replace LLM stubs with actual calls when running in secure environment.

Future work.
- Integrate Gemini for QA and planner refinement
- Add spaced repetition and collaborative features
- Deploy orchestrator to Agent Engine or Cloud Run
