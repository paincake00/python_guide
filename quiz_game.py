dict_questions = {}

with open("files/quiz_game_ques.txt") as file:
    value = ""
    for line in file:
        if line.startswith('#'):
            dict_questions.update({value:line[1:].rstrip()})
            value=""
        else:
            value += line

while True:
    correct_count = 0
    for question in dict_questions:
        print(question)
        if input("Your answer: ").upper() == dict_questions[question]:
            correct_count += 1

    print("Your score: {}%".format(100 * correct_count // len(dict_questions)))

    command = ""
    while command not in {"y", "n"}:
        command = input("Do you want to repeat? (y/n)\n").lower()
    if (command == "n"):
        print("bye!")
        break    