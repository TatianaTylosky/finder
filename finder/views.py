from flask import Flask, render_template

from finder import app
from .database import session
from .models import Bootcamp

@app.route("/all")
def all_bootcamps():
    list_of_all_bootcamps = session.query(Bootcamp)
    # posts = posts.all()
    return render_template("all.html",
        list_of_all_bootcamps=list_of_all_bootcamps
    )

# @app.route("/bootcamps")
# def template_test():
# 	list_of_all_bootcamps = start.get_bootcamps()
# 	return render_template('template.html', list_of_all_bootcamps=list_of_all_bootcamps)
# @app.route("/<search-term>")
# def search_term(search_term):
# 	return "search term page"

# @app.route("/bootcamps/<bootcamp-name>")
# def bootcamp_page(name):
#         return "Welcome to {}'s page!".format(name.title())

# @app.route("/<submit-review>")
# def search_term():

# @app.route("/<submit-bootcamp>")
# def search_term():

# @app.route("/admin/thinkful")
# def search_term():

# @app.route("/admin/<bootcamp-name>")
# def search_term():

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
