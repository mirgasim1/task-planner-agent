# Task Planner Assistant

Simple task planner assistant that helps students create short step-by-step plans for study-related goals.

## Step 1 – System Plan

### 1. System Description

I plan to develop a simple Task Planner Assistant using Python. The system will help students create a basic plan for study-related tasks, such as preparing for exams, finishing homework, studying math, or learning Python. The user will enter one short English goal, and the system will return a simple numbered 3-step plan. The main goal of the system is to give students a clear starting point for organizing their study tasks.

### 2. Agent-Based Approach

The system will use a simple rule-based agent approach. The agent will receive one short English text goal from the user, analyze the text, and decide what type of plan is needed. It will check for keywords such as exam, homework, study, math, or Python. Then the agent will use tools to generate a 3-step plan and return it as output.

### 3. Tools

The system will use three simple tools. These tools will be implemented as Python functions, so no external API or online service is required.

- Keyword extractor tool: identifies important keywords from the user input and returns a plan category, such as exam, homework, study, or general.
- Plan generator tool: creates a suitable 3-step plan based on the detected category.
- Output formatter tool: formats the generated plan into a clear numbered output.

### 4. Programming Concepts

The following programming concepts will be used:

- Functions: used to implement the three tools: `extract_keywords(user_input)`, `generate_plan(category)`, and `format_plan(plan_steps)`.
- Classes: a simple `Agent` class will control the workflow of the system.
- Modules: the project will be divided into files such as `main.py`, `agent.py`, and `tools.py`.
- Lists: used to store the 3 plan steps.
- Dictionaries: used to connect categories such as exam, homework, study, and general with ready-made plan steps.
- String processing: used to clean user input with methods like `lower()` and `strip()`.
- Conditional statements: used to choose the correct plan based on detected keywords.
- Basic error handling: used for empty input or unknown keywords.
