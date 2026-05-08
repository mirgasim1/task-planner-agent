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

## Step 2 – Implementation Progress

### 1. Updated System Description

The Task Planner Assistant is now planned as a simple Python command-line program. The system receives one short English study goal from the user, such as “prepare for exam”, “finish homework”, “study math”, or “learn Python”. Based on the input, the system detects keywords and returns a numbered 3-step plan.

The first implementation will use simple rule-based logic. No external API, database, or online service is required. The goal is to keep the system easy to run, easy to understand, and easy to test.

### 2. Programming Concepts Actually Used

The project uses the following programming concepts:

- Functions
- One simple Agent class
- Modules
- Lists
- Dictionaries
- String processing
- Conditional statements
- Basic error handling

### 3. How These Concepts Are Applied

Functions are used to build the three main tools of the system. The keyword extractor function checks the user input. The plan generator function creates the correct 3-step plan. The output formatter function displays the plan clearly.

A simple Agent class is used to control the workflow. The agent receives the user input, calls the keyword extractor tool, sends the result to the plan generator tool, and then sends the plan to the formatter tool.

Modules are used to organize the project. main.py handles user input and output. agent.py contains the Agent class. tools.py contains the tool functions.

Lists are used to store the 3 plan steps. Dictionaries are used to connect categories such as exam, homework, study, and general with ready-made plans.

String processing is used to clean the input with lower() and strip(). Conditional statements are used to decide which plan category should be selected. Basic error handling is used when the user enters empty input or when no known keyword is found.

### 4. Tool Integration

The system uses three simple tools, implemented as Python functions.

1. Keyword extractor tool  
This tool receives the user input as a string. It converts the text to lowercase, removes unnecessary spaces, and checks for keywords such as exam, homework, study, math, and Python. It returns a category such as exam, homework, study, or general.

2. Plan generator tool  
This tool receives the category from the keyword extractor. It uses a dictionary to choose the correct 3-step plan. For example, if the category is exam, it returns an exam preparation plan.

3. Output formatter tool  
This tool receives the plan as a list of steps. It formats the list into a numbered output and returns the final text shown to the user.

The workflow is:

User input → Agent → Keyword extractor → Plan generator → Output formatter → Final 3-step plan
