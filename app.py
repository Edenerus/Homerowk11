from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def page_main():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def page_candidate(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    count_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, count_candidates=count_candidates)


@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    count_candidates = len(candidates)
    return render_template("skill.html", candidates=candidates, count_candidates=count_candidates, skill_name=skill_name)


app.run()
