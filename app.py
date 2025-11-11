import os

from flask import Flask, render_template, request

app = Flask(__name__)

# === 1. Define your questions and answers ===
QUESTIONS = [
    {"id": "q1", "question": "What keyword is used to define a function in Python?"},
    {"id": "q2",
        "question": "How do you start a comment in Python? (just the symbol)"},
    {"id": "q3", "question": "What data type does input() return?"},
    {"id": "q4", "question": "What keyword is used to create a loop over items in a list?"},
    {"id": "q5", "question": "What keyword do you use to import a module in Python?"},
]

ANSWERS = {
    "q1": ["def"],
    "q2": ["#"],
    "q3": ["str", "string"],
    "q4": ["for"],
    "q5": ["import"],
}

# === 2. Home route (landing page) ===


@app.route("/")
def home():
    return render_template("index.html")


# === 3. Quiz route (shows form + handles answers) ===
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # These three lines MUST be inside this if-block, indented exactly like this:
        score = 0
        total = len(QUESTIONS)
        user_answers = {}

        for q in QUESTIONS:
            # Get the user's answer for each question
            user_input = request.form.get(q["id"], "").strip().lower()
            user_answers[q["id"]] = user_input

            correct_answers = ANSWERS[q["id"]]
            if user_input in correct_answers:
                score += 1

        percent = round(score / total * 100)

        return render_template(
            "result.html",
            score=score,
            total=total,
            percent=percent,
            questions=QUESTIONS,
            user_answers=user_answers,
            answers=ANSWERS,
        )

    # If it's a GET request → show the quiz form
    return render_template("quiz.html", questions=QUESTIONS)


import os  # add this at the top of the file if it's not there already

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives a PORT env var
    app.run(
        host="0.0.0.0",  # listen on all network interfaces
        port=port,
        debug=False      # debug off in production
    )

