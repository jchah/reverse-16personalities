import os


class Question:
    def __init__(self, text, trait):
        self.text = text
        self.trait = trait


def load_questions(file_name):
    questions_list = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 2:
                questions_list.append(Question(*parts))
    return questions_list


def calculate_max_scores(questions_list):
    max_scores = {}
    for question in questions_list:
        max_scores[question.trait] = max_scores.get(question.trait, 0) + 3
    return max_scores


def generate_filename(base_filename):
    base, ext = os.path.splitext(base_filename)
    counter = 1
    while os.path.exists(new_filename := f"{base}_{counter}{ext}"):
        counter += 1
    return new_filename


def read_answers(filename, questions_list):
    traits_scores = {question.trait: 0 for question in questions_list}
    with open(filename, 'r') as file:
        answers = [int(ans) for ans in file.read().strip().split(',')]

    for answer, question in zip(answers, questions_list):
        traits_scores[question.trait] += answer

    return compile_data(traits_scores, questions_list)


def compile_data(traits_scores, questions_list):
    max_scores = calculate_max_scores(questions_list)
    trait_pairs = [
        ['extroversion', 'introversion'],
        ['intuitive', 'sensing'],
        ['thinking', 'feeling'],
        ['judging', 'prospecting']
    ]
    personality_string = ""
    trait_absolutes = {}

    for first, second in trait_pairs:
        whole = max_scores[first] + max_scores[second]
        part = traits_scores[first] - traits_scores[second] + whole
        percentage = round((part / (2 * whole)) * 100)
        trait_absolutes[first] = percentage

        if percentage > 50:
            personality_string += "n" if first == "intuitive" else first[0]
        elif percentage < 50:
            personality_string += "n" if second == "intuitive" else second[0]
        else:
            personality_string += f"({first[0]}/{second[0]})"

    return trait_absolutes, personality_string
