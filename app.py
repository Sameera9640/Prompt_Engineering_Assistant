from assistant import ask_gemini
from datetime import datetime
import os

HISTORY_FILE = "prompt_history.txt"

# ==========================================
# Save History
# ==========================================

def save_history(feature, user_input, response):

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write(f"Date : {datetime.now()}\n")
        file.write(f"Feature : {feature}\n\n")

        file.write("Input:\n")
        file.write(user_input)

        file.write("\n\nResponse:\n")
        file.write(response)

        file.write("\n\n")


# ==========================================
# Export History
# ==========================================

def export_history():

    if os.path.exists(HISTORY_FILE):

        filename = f"History_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(HISTORY_FILE, "r", encoding="utf-8") as old:

            data = old.read()

        with open(filename, "w", encoding="utf-8") as new:

            new.write(data)

        print("\nHistory exported as:", filename)

    else:
        print("\nNo history found.")


# ==========================================
# View History
# ==========================================

def view_history():

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:

            print(file.read())

    else:

        print("\nNo history available.")


# ==========================================
# Clear History
# ==========================================

def clear_history():

    if os.path.exists(HISTORY_FILE):

        os.remove(HISTORY_FILE)

        print("\nHistory Cleared Successfully!")

    else:

        print("\nHistory Already Empty.")


# ==========================================
# Prompt Templates
# ==========================================

def prompt_templates():

    print("\nAvailable Templates\n")

    templates = {

        "1": "Blog Writing",
        "2": "Python Coding",
        "3": "Resume",
        "4": "Business Idea",
        "5": "Email Writing"
    }

    for k, v in templates.items():
        print(f"{k}. {v}")

    choice = input("\nChoose Template : ")

    if choice == "1":
        topic = input("Topic : ")
        prompt = f"Write a professional blog on {topic}."

    elif choice == "2":
        topic = input("Problem : ")
        prompt = f"Write Python code for {topic} with explanation."

    elif choice == "3":
        prompt = "Create an ATS friendly resume."

    elif choice == "4":
        prompt = "Generate an innovative startup idea."

    elif choice == "5":
        prompt = "Write a professional email."

    else:
        print("Invalid")
        return

    result = ask_gemini(prompt)

    print(result)

    save_history("Prompt Template", prompt, result)


# ==========================================
# Translate Prompt
# ==========================================

def translate_prompt():

    prompt = input("\nEnter Prompt:\n")

    language = input("Translate To : ")

    instruction = f"""
Translate the following prompt into {language}.

Prompt:
{prompt}
"""

    result = ask_gemini(instruction)

    print(result)

    save_history("Translate Prompt", prompt, result)


# ==========================================
# Prompt Evaluation
# ==========================================

def evaluate_prompt():

    prompt = input("\nEnter Prompt:\n")

    instruction = f"""
Evaluate this AI prompt.

Prompt:

{prompt}

Give

1.Score out of 10

2.Strengths

3.Weaknesses

4.Suggestions
"""

    result = ask_gemini(instruction)

    print(result)

    save_history("Evaluate Prompt", prompt, result)


# ==========================================
# AI Chat
# ==========================================

def ai_chat():

    print("\nType exit to stop chatting.\n")

    while True:

        user = input("You : ")

        if user.lower() == "exit":
            break

        reply = ask_gemini(user)

        print("\nGemini:\n")
        print(reply)
        print()


# ==========================================
# Save Prompt
# ==========================================

def save_prompt():

    text = input("\nEnter Prompt:\n")

    filename = input("File name : ")

    with open(filename + ".txt", "w", encoding="utf-8") as file:

        file.write(text)

    print("Saved Successfully.")


# ==========================================
# Main Program
# ==========================================

while True:

    print("\n" + "=" * 40)
    print("      Prompt Engineering Assistant")
    print("=" * 40)

    print("1.Generate Prompt")
    print("2.Improve Prompt")
    print("3.Explain Prompt")
    print("4.Optimize Prompt")
    print("5.View History")
    print("6.Prompt Templates")
    print("7.Evaluate Prompt")
    print("8.Translate Prompt")
    print("9.Save Prompt")
    print("10.Export History")
    print("11.Clear History")
    print("12.AI Chat")
    print("13.Exit")

    choice = input("\nChoose : ")

    # ======================================

    if choice == "1":

        topic = input("Topic : ")

        prompt = f"""
Generate a high-quality AI prompt on

Topic : {topic}

The prompt should be clear, structured and detailed.
"""

        result = ask_gemini(prompt)

        print(result)

        save_history("Generate Prompt", topic, result)

    # ======================================

    elif choice == "2":

        text = input("Enter Prompt:\n")

        prompt = f"Improve this AI prompt:\n{text}"

        result = ask_gemini(prompt)

        print(result)

        save_history("Improve Prompt", text, result)

    # ======================================

    elif choice == "3":

        text = input("Enter Prompt:\n")

        prompt = f"""
Explain this prompt.

{text}

Explain:

Purpose

Role

Expected Output

Advantages
"""

        result = ask_gemini(prompt)

        print(result)

        save_history("Explain Prompt", text, result)

    # ======================================

    elif choice == "4":

        text = input("Enter Prompt:\n")

        prompt = f"""
Optimize this prompt using Prompt Engineering best practices.

{text}
"""

        result = ask_gemini(prompt)

        print(result)

        save_history("Optimize Prompt", text, result)

    # ======================================

    elif choice == "5":

        view_history()

    # ======================================

    elif choice == "6":

        prompt_templates()

    # ======================================

    elif choice == "7":

        evaluate_prompt()

    # ======================================

    elif choice == "8":

        translate_prompt()

    # ======================================

    elif choice == "9":

        save_prompt()

    # ======================================

    elif choice == "10":

        export_history()

    # ======================================

    elif choice == "11":

        clear_history()

    # ======================================

    elif choice == "12":

        ai_chat()

    # ======================================

    elif choice == "13":

        print("\nThank you for using Prompt Engineering Assistant.")
        break

    else:

        print("Invalid Choice.")