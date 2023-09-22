from content import Question_data
from question_model import question
from Quiz_Fuctioning import Fuctioning
bank = []
for q in question_data:
    text = q["question"]
    question_answer = q["answer"]
    new = question(text,question_answer)
    bank.append(new)

test = Fuctioning(bank)
while test.still_has_question():
    test.next()


