from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store comments in a list
comments = []

@app.route("/")
def index():
    return render_template("index.html", comments=comments)

@app.route("/project", methods=["POST"])
def project():
    selected_project = request.form.get("project")
    if selected_project == "Spam Mail Detection Project":
        return redirect("https://github.com/sunilgiri7/Spam-Mail-Detection_Project")
    elif selected_project == "Movie Recommendation Project":
        return redirect("https://github.com/sunilgiri7/Movie_Recommendation_End_To_End_Project")
    elif selected_project == "Flight Fare Project":
        return redirect("https://github.com/sunilgiri7/Flight-Fare-Prediction-Project")
    elif selected_project == "Attandance Project":
        return redirect("https://github.com/sunilgiri7/Attandance-Project")
    elif selected_project == "Deep Learning Repo":
        return redirect("https://github.com/sunilgiri7/deep-learning")
    elif selected_project == "Machine Learning Repo":
        return redirect("https://github.com/sunilgiri7/Machine-Learning")
    elif selected_project == "Data Structure Repo":
        return redirect("https://github.com/sunilgiri7/DATA_STRUCTURE-DSA-")
    else:
        return "Invalid project selected."

@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    comment = request.form.get("comment")
    # Save the comment to a database or a list
    comments.append(comment)
    return redirect("/")


if __name__ == "__main__":
    app.run()
