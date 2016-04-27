from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)



@app.route("/student_search")   
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student_info")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", 
                            first = first, 
                            last=last,
                            github=github)
    


@app.route("/new_student")   
def get_new_student_form():
    """Show form for adding a student."""

    return render_template("new_student.html")


@app.route("/student_add", methods=["POST"])
def student_add():
    """Add a student."""
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    github_acct = request.form.get("github_acct")

    return render_template("new_student_info.html", first_name=first_name, last_name=last_name, github_acct=github_acct)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
