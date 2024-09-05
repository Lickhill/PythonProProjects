class QuizBrain:
    count = 0

    def __init__(self, ques):
        self.questionnumber = 0
        self.questionlist = ques

    def nextquestion(self):
        current_question = self.questionlist[self.questionnumber]
        myanswer = input(
            f"Q.{self.questionnumber+1}: {current_question.text} (True/Flase)?:"
        )
        self.questionnumber += 1
        self.checkanswer(myanswer, current_question.ans)

    def still_has_questions(self):
        if self.questionnumber < len(self.questionlist):
            self.nextquestion()

    def checkanswer(self, myanswer, correctanswer):
        if myanswer == correctanswer:
            print("You got it right")
            QuizBrain.count += 1
        else:
            print("you got it wrong")
        print(f"The correct answer was {correctanswer}")
        self.score(myanswer, correctanswer)

    def score(self, myanswer, correctanswer):
        if myanswer == correctanswer:
            print(f"Your score is {QuizBrain.count}/{self.questionnumber}\n")
        else:
            print(f"Your score is {QuizBrain.count}/{self.questionnumber}\n")

    def finalscore(self):
        print(
            f"You have completed the QUIZ.\nYour final score is: {QuizBrain.count}/{len(self.questionlist)}\n"
        )
