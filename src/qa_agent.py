PROMPT_TEMPLATE = """
You are a concise tutor. Answer the user's question in <=200 words. Provide one short example and one practice problem with a solution. If external resources are helpful, list 1-2 recommended links.
Subject: {subject}
Question: {question}

Answer:
"""

def answer_question_stub(subject, question):
    # This is a stub for the LLM call. Replace with actual LLM when deployed.
    answer = f"(Stub) {subject}: Brief explanation of '{question}'."
    example = f"Example: simple illustration related to {subject}."
    practice = f"Practice: Try solving an easy problem on {subject}."
    solution = f"Solution: Outline steps to solve the practice problem."
    return {'answer': answer, 'example': example, 'practice': practice, 'solution': solution}
