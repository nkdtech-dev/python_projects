#Quiz Game Part3
class QuizBrain:
    def __init__(self,ql):
        """Contains variable"""
        self.qn=0
        self.ql=ql
        self.score=0
    def nq(self):
        """Ask questions"""
        qq=self.ql[self.qn]
        self.qn+=1
        aa=input(f"Q.{self.qn}: {qq.question} (True/False)?: ").lower()
        self.ca(aa,qq.correct_answer)
    #Quiz Game Part4
    def shq(self):
        """Check if there are still questions"""
        if self.qn>=len(self.ql):
            print(f"You have completed the quiz\nYour final score is: {self.score}/{self.qn}")
            return False
        else:
            return True
    def ca(self,aa,an):
        """Checks if answer is correct"""
        if aa==an.lower():
            self.score+=1
            print(f"Your got it right")
        else:
            print(f"Your got it wrong")
        print(f"The correct answer was: {an}")
        print(f"Your scores is: {self.score}/{self.qn}")
        print("\n")