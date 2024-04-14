question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

logo = '''
   ____        _            _____                       
  / __ \      (_)          / ____|                      
 | |  | |_   _ _ ________ | |  __  __ _ _ __ ___   ___  
 | |  | | | | | |_  /_  / | | |_ |/ _` | '_ ` _ \ / _ \ 
 | |__| | |_| | |/ / / /  | |__| | (_| | | | | | |  __/ 
  \___\_\\__,_|_/___/___|  \_____|\__,_|_| |_| |_|\___| 
                                                        
                                                         '''

# TODO 1 : Create a Class for question have to instance question and answer
class Question:
    def __init__(self,  q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# TODO 2 : Create a list have question object from Question data


Question_bank = []

for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    Question_bank.append(new_question)
print(Question_bank)

# TODO 3: Create Quiz Brain Class with functions for next_question,
#  answer_check, still_has_question, and score_calculation


class QuizzBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've complete the Quiz.")
            print(f"Your final score as:{self.score}/{self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number }:{current_question.text} .(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"To be correct answer was : {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")


print(logo)
quiz = QuizzBrain(Question_bank)

while quiz.still_has_question():

    quiz.next_question()
