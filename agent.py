from tools import extract_keywords, generate_plan, format_plan


class Agent:
    def run(self, user_input):
        category = extract_keywords(user_input)

        if category == "empty":
            return "Please enter a goal."

        plan = generate_plan(category)
        formatted_plan = format_plan(plan)

        return formatted_plan
