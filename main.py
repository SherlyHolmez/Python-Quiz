quiz = {
    "question1":{
        "question" : "What is the capital of Pakistan",
        "answer":"Islamabad"
    },
    "question2":{
        "question":"What is the capital of China",
        "answer":"Beijing"
    },
    "question3":{
        "question":"What is the capital of Germany",
        "answer": "Berlin"
    },
    "question4":{
        "question":"What is the capital of Spain",
        "answer": "Madrid"
    },
    "question5":{
        "question":"What is the capital of Portugal",
        "answer": "Lisbon"
    },
    "question6":{
        "question":"What is the capital of Switzerland",
        "answer": "Bern"
    },
    "question7":{
        "question":"What is the capital of Austria",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Your Answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score += 1
        print("Your score is: ", str(score))
        print('')
        print('')
    else:
        print('Wrong!')
        print('The correct answer is: ',value['answer'])
        print("Your score is: ", str(score))
        print('')
        print('')

print("Your final score is "+ str(score) +"/7")
print("Your percentage is " + str(int(score/7 * 100)) + "%")