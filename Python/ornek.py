class Question():
    def __init__(self,question,choeses,answer):
        self.question=question
        self.choeses=choeses
        self.answer=answer
    def checkanswer(self,answer):
       return  self.answer==answer
    
class Quiz(Question):
    def __init__(self,question):
        self.question=question
        self.score=0
        self.questionİndex=0
    def getquestion(self):
        return self.question[self.questionİndex]
    
    
p1 = Question('en iyi programlama dili hangisidir',['python','java','javascript'],'python')
p2 = Question('en çok kazandıran programlama dili hangisidir',['python','java','javascript'],'python')
p3 = Question('en çok kullanılan programlama dili hangisidir',['python','java','javascript'],'python')

question=[p1,p2,p3]

quiz= Quiz(question)
question=quiz.question[quiz.questionİndex]
print(question.choeses)