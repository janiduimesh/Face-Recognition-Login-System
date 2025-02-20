# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from register import register_user
from login import login
import sys
from io import StringIO

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flashing messages

@app.route("/")
def home():
    """Render the homepage."""
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    """Handle user registration."""
    name = request.form["name"]
    if not name:
        flash("Please enter your name.", "error")
        return redirect(url_for("home"))

    # Redirect stdout to capture print messages
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the register_user function
    register_user(name)

    # Get the output and restore stdout
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    # Flash the output message
    flash(output.strip(), "success")
    return redirect(url_for("home"))

@app.route("/login", methods=["POST"])
def login_route():
    """Handle user login."""
    # Redirect stdout to capture print messages
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Call the login function
    login()

    # Get the output and restore stdout
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    # Flash the output message
    flash(output.strip(), "success" if "Welcome back" in output else "error")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)