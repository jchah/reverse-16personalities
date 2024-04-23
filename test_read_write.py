import os
import random


class Question:
    def __init__(self, text, trait):
        self.text = text
        self.trait = trait


def ask_questions(file_name, generate, new_file):
    questions = load_questions(file_name)
    answers = []
    for question in questions:
        while True:
            try:
                if generate:
                    response = random.randint(-3, 3) if generate else int(input("Answer (-3 to 3):"))
                else:
                    print(question.text)
                    response = int(input("Response from -3 to 3: "))
                if not -3 <= response <= 3:
                    raise ValueError("Response must be between -3 and 3.")
                answers.append(response)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    if new_file:
        filename = generate_filename('responses.txt')
    else:
        filename = "response_1"
    with open(filename, 'w') as file:
        file.write(','.join(map(str, answers)))
    return filename


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
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    return f"{base}_{counter}{ext}"


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
        ['intuition', 'sensing'],
        ['thinking', 'feeling'],
        ['judging', 'prospecting'],
        ['assertive', 'turbulent']
    ]
    personality_string = ""
    trait_absolutes = {}
    for first, second in trait_pairs:
        whole = max_scores[first] + max_scores[second]
        part = traits_scores[first] - traits_scores[second] + whole
        percentage = round((part / (2 * whole)) * 100)
        trait_absolutes[first] = percentage
        if first == "assertive" or first == "turbulent":
            personality_string += "-"
        if percentage > 50:
            personality_string += "n" if first == "intuition" else first[0]
        elif percentage < 50:
            personality_string += "n" if second == "intuition" else second[0]
        else:
            personality_string += f"({first[0]}/{second[0]})"
    return trait_absolutes, personality_string


def main():
    personality_strings = []
    responses_filename = ask_questions('questions.txt', 1, 0)
    questions = load_questions('questions.txt')
    traits_scores, personality_string = read_answers(responses_filename, questions)
    personality_strings.append(personality_string)


if __name__ == "__main__":
    main()
