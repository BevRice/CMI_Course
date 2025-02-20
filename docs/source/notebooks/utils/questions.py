# questions.py
import ipywidgets as widgets
from IPython.display import display, clear_output

def normalize_input(user_input):
    """Normalize input by converting to lowercase and stripping whitespace."""
    return user_input.lower().strip()

def create_fill_in_the_blank(question_text, correct_answer):
    """
    Creates a fill-in-the-blank question with a submit and reset button.
    
    Parameters:
    - question_text (str): The question to display.
    - correct_answer (str): The correct answer (case insensitive).
    """
    answer = widgets.Text(placeholder="Type your answer here...")
    submit_button = widgets.Button(description="Submit", button_style="success")
    reset_button = widgets.Button(description="Reset", button_style="warning")
    output = widgets.Output()

    def check_answer(_):
        with output:
            output.clear_output()
            if normalize_input(answer.value) == normalize_input(correct_answer):
                print("✅ Correct! Great job!")
            else:
                print(f"❌ Incorrect. Try again! Hint: Think about '{question_text.split()[0]}'.")

    def reset_question(_):
        output.clear_output()
        answer.value = ""

    submit_button.on_click(check_answer)
    reset_button.on_click(reset_question)

    display(widgets.HTML(f"<b>Fill in the blank:</b> {question_text}"), answer,
            widgets.VBox([submit_button, reset_button, output]))

def create_multiple_choice(question_text, choices, correct_answer):
    """
    Creates a resettable multiple-choice question with a submit button.
    
    Parameters:
    - question_text (str): The question to display.
    - choices (list): A list of answer choices.
    - correct_answer (str): The correct answer (case insensitive).
    """
    answer = widgets.RadioButtons(options=choices, description="",
                                  style={'description_width': 'initial'},
                                  layout=widgets.Layout(width='auto'))
    answer.value=None
    submit_button = widgets.Button(description="Submit", button_style="success")
    reset_button = widgets.Button(description="Reset", button_style="warning")
    output = widgets.Output()

    def check_answer(_):
        with output:
            output.clear_output()
            if normalize_input(answer.value) == normalize_input(correct_answer):
                print("✅ Correct! Well done!")
            else:
                print(f"❌ Incorrect. The correct answer is '{correct_answer}'.")

    def reset_question(_):
        output.clear_output()
        answer.value = None  

    submit_button.on_click(check_answer)
    reset_button.on_click(reset_question)

    display(widgets.HTML(f"<b>Multiple Choice:</b> {question_text}"), 
            widgets.VBox([answer, submit_button, reset_button, output]))

