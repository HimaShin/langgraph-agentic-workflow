from app import call_gpt

def solve_task(task):
    prompt = f"Solve this task: {task}"
    return call_gpt(prompt)
