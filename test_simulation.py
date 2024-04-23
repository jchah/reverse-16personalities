import random
from collections import Counter


class Question:
    def __init__(self, text, trait):
        self.text = text
        self.trait = trait


def generate_questions():
    # Updated list of questions and their associated traits
    return [
        Question("You regularly make new friends.", "extroversion"),
        Question("You feel comfortable just walking up to someone you find interesting and striking up a conversation.",
                 "extroversion"),
        Question("You enjoy participating in team-based activities.", "extroversion"),
        Question("You usually prefer to be around others rather than on your own.", "extroversion"),
        Question("Your friends would describe you as lively and outgoing.", "extroversion"),
        Question("You can easily connect with people you have just met.", "extroversion"),
        Question("You feel more drawn to busy, bustling atmospheres than to quiet, intimate places.", "extroversion"),
        Question("Complex and novel ideas excite you more than simple and straightforward ones.", "intuition"),
        Question("You enjoy experimenting with new and untested approaches.", "prospecting"),
        Question("You enjoy debating ethical dilemmas.", "intuition"),
        Question("You are drawn to various forms of creative expression, such as writing.", "intuition"),
        Question("You enjoy exploring unfamiliar ideas and viewpoints.", "intuition"),
        Question(
            "You prefer tasks that require you to come up with creative solutions rather than follow concrete steps.",
            "prospecting"),
        Question("You usually feel more persuaded by what resonates emotionally with you than by factual arguments.",
                 "feeling"),
        Question("People's stories and emotions speak louder to you than numbers or data.", "feeling"),
        Question("You prioritize being sensitive over being completely honest.", "feeling"),
        Question("When facts and feelings conflict, you usually find yourself following your heart.", "feeling"),
        Question(
            "When making decisions, you focus more on how the affected people might feel than on what is most logical "
            "or efficient.",
            "feeling"),
        Question("You are not too interested in discussions about various interpretations of creative works.",
                 "sensing"),
        Question("You become bored or lose interest when the discussion gets highly theoretical.", "sensing"),
        Question("You are not too interested in discussing theories on what the world could look like in the future.",
                 "sensing"),
        Question("You believe that pondering abstract philosophical questions is a waste of time.", "sensing"),
        Question("You prioritize facts over people's feelings when determining a course of action.", "thinking"),
        Question("You favor efficiency in decisions, even if it means disregarding some emotional aspects.",
                 "thinking"),
        Question("You are not easily swayed by emotional arguments.", "thinking"),
        Question("You usually base your choices on objective facts rather than emotional impressions.", "thinking"),
        Question("In disagreements, you prioritize proving your point over preserving the feelings of others.",
                 "thinking"),
        Question("You usually wait for others to introduce themselves first at social gatherings.", "introversion"),
        Question("You enjoy solitary hobbies or activities more than group ones.", "introversion"),
        Question("You would love a job that requires you to work alone most of the time.", "introversion"),
        Question("You find the idea of networking or promoting yourself to strangers very daunting.", "introversion"),
        Question("You avoid making phone calls.", "introversion"),
        Question("You rarely worry about whether you make a good impression on people you meet.", "assertive"),
        Question("You rarely second-guess the choices that you have made.", "assertive"),
        Question("You rarely feel insecure.", "assertive"),
        Question("You usually stay calm, even under a lot of pressure.", "assertive"),
        Question("You feel confident that things will work out for you.", "assertive"),
        Question("Your mood can change very quickly.", "turbulent"),
        Question("You are prone to worrying that things will take a turn for the worse.", "turbulent"),
        Question("You find it challenging to maintain a consistent work or study schedule.", "turbulent"),
        Question("You are still bothered by mistakes that you made a long time ago.", "turbulent"),
        Question("You often feel overwhelmed.", "turbulent"),
        Question("Even a small mistake can cause you to doubt your overall abilities and knowledge.", "turbulent"),
        Question("You often allow the day to unfold without any schedule at all.", "prospecting"),
        Question("You often end up doing things at the last possible moment.", "prospecting"),
        Question("You struggle with deadlines.", "prospecting"),
        Question(
            "Your personal work style is closer to spontaneous bursts of energy than organized and consistent efforts.",
            "prospecting"),
        Question("You like to have a to-do list for each day.", "judging"),
        Question("You prefer to do your chores before allowing yourself to relax.", "judging"),
        Question("If your plans are interrupted, your top priority is to get back on track as soon as possible.",
                 "judging"),
        Question("You complete things methodically without skipping over any steps.", "judging"),
        Question("Your living and working spaces are clean and organized.", "judging"),
        Question("You prioritize and plan tasks effectively, often completing them well before the deadline.",
                 "judging"),
        Question("You like to use organizing tools like schedules and lists.", "judging"),
    ]


def ask_questions(questions, generate=True):
    answers = []
    for question in questions:
        response = random.randint(-3, 3) if generate else int(input(f"{question.text} (Response from -3 to 3): "))
        answers.append(response)
    return answers


def calculate_max_scores(questions):
    max_scores = {}
    for question in questions:
        max_scores[question.trait] = max_scores.get(question.trait, 0) + 3
    return max_scores


def compile_data(answers, questions):
    traits_scores = {question.trait: 0 for question in questions}
    for answer, question in zip(answers, questions):
        traits_scores[question.trait] += answer

    max_scores = calculate_max_scores(questions)

    trait_pairs = [
        ["extroversion", "introversion"],
        ["intuition", "sensing"],
        ["thinking", "feeling"],
        ["judging", "prospecting"],
        ["assertive", "turbulent"]
    ]

    personality_string = ""
    for first, second in trait_pairs:
        whole = max_scores[first] + max_scores[second]
        part = traits_scores[first] - traits_scores[second] + whole
        percentage = round((part / (2 * whole)) * 100)

        if first == "assertive" or first == "turbulent":
            personality_string += "-"

        if percentage > 50:
            personality_string += "n" if first == "intuition" else first[0]
        else:
            personality_string += "n" if second == "intuition" else second[0]

    return personality_string


def main():
    questions = generate_questions()
    personality_strings = []

    for _ in range(1000000):
        answers = ask_questions(questions)  # Simulate 100 sets of responses
        personality_string = compile_data(answers, questions)
        personality_strings.append(personality_string)

    # Count occurrences of each personality type
    personality_counts = Counter(personality_strings)

    # Print the count of each personality type
    for personality, count in personality_counts.items():
        print(f"{personality}: {count}")

    # Most common personality type
    most_common_personality = personality_counts.most_common(1)[0][0]
    print(f"Most common personality type: {most_common_personality}")


if __name__ == "__main__":
    main()
