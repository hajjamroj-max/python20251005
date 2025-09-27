import datetime
import re

def clear(display_text):
    display_text.set("")

def calculate(display_text):
    try:
        expression = display_text.get()
        result = eval(expression)
        result_str = str(result)[:8]
        display_text.set(result_str)
        save_calculation(display_text, expression, result_str)
    except SyntaxError:
        display_text.set("Syntax Error")
    except ZeroDivisionError:
        display_text.set("Can't Divide by 0")
    except Exception as e:
        display_text.set("Error")
def save_calculation(display_text, expression=None, result=None):
    try:
        if expression is None:
            expression = display_text.get()
        if result is None:
            result = display_text.get()

        if expression and result and result != "Saved!" and expression != "Saved!":
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp}: {expression} = {result}\n"

            with open("calc_history.txt", "a", encoding="utf-8") as file:
                file.write(log_entry)

            display_text.set("Saved!")
    except Exception as e:
        display_text.set("Save Error")

def add_character(display_text, char):
    current_text = display_text.get()

    # Clear message if present
    if current_text in ["Saved!", "Max 8 chars!", "Save Error", "Error"]:
        display_text.set("")
        current_text = ""

    # Prevent 0.0 pattern
    if char == "0" and current_text == "0.":
        return

    # Prevent multiple leading zeros
    if char == "0" and current_text == "0":
        return

    # Check length and validate with regex
    if len(current_text) < 8:
        new_text = current_text + char
        if re.match(r'^[\d\+\-\*\/\.]{0,8}$', new_text):
            display_text.set(new_text)
    else:
        display_text.set("Max 8 chars!")