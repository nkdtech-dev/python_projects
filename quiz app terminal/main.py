#Quiz Game Part2
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
Question_bank=[]
for i in question_data:
    q=i["question"]
    a=i["correct_answer"]
    ques=Question(q,a)
    Question_bank.append(ques)

quiz=QuizBrain(Question_bank)
while quiz.shq():
    quiz.nq()