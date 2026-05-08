def extract_keywords(user_input):
    text = user_input.lower().strip()

    if text == "":
        return "empty"

    if "exam" in text:
        return "exam"
    elif "homework" in text:
        return "homework"
    elif "study" in text or "math" in text or "python" in text or "learn" in text:
        return "study"
    else:
        return "general"


def generate_plan(category):
    plans = {
        "exam": [
            "Review lecture notes",
            "Practice sample questions",
            "Revise weak topics"
        ],
        "homework": [
            "Read the homework task carefully",
            "Divide the work into smaller parts",
            "Check the final answer before submitting"
        ],
        "study": [
            "Choose the topic you want to study",
            "Read or watch learning material",
            "Practice with small exercises"
        ],
        "general": [
            "Write down the main task",
            "Divide it into smaller steps",
            "Start with the easiest step"
        ]
    }

    return plans.get(category, plans["general"])


def format_plan(plan_steps):
    result = "Your task plan:\n"

    for index, step in enumerate(plan_steps, start=1):
        result += f"{index}. {step}\n"

    return result
