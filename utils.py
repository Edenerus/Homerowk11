import json


def load_candidates_from_json():
    with open("candidates.json", encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(candidate_id: int):
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name):
    candidates = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate["name"].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill_name):
    candidates_for_skill = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate["skills"].lower():
            candidates_for_skill.append(candidate)
    return candidates_for_skill

print(get_candidate(2)["picture"])