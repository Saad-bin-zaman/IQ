print("Welcome to the IQ Game!")
print("Answer 10 questions to determine your IQ.")
print("You need to score 70% or more to have an IQ above 110.")
print("Let's get started!\n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0
total_questions = 10

def ask_question(question, correct_answer):
    global score
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was:", correct_answer)

questions = [
    ("What does G.K. stand for?", "general knowledge"),
    ("What is ChatGPT?", "ai chat system"),
    ("What does A.S.I stand for?", "artificial super intelligence"),
    ("What is the most demanding programming language in the world?", "python"),
    ("What does M.L. stand for?", "machine learning"),
    ("Who invented space X?", "elon musk"),
    ("which animal is the biggest on this planet?", "blue whale"),
    ("which animal is the king of the jungle?", "lion"),
    ("which language is most famous on this planet?", "English"),
    ("who is the most famous person on this planet?", "cristiano ronaldo")
]

for question, answer in questions:
    ask_question(question, answer)

percentage_correct = (score / total_questions) * 100
print("\nYou've got", score, "out of", total_questions, "questions correct.")
print("You've got", percentage_correct, "%")

if percentage_correct >= 70:
    print("Congratulations! Your IQ is above 110.")
else:
    print("Your IQ is under 100.")
