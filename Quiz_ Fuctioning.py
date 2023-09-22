class Fuctioning:
    def __init__(self,list) :
        self.q_no = 0
        self.marks = 0
        self.question_list = list

    def still_has_question(self):
        return self.q_no < len(self.question_list)
    
    def next(self):
        current = self.question_list[self.q_no]
        self.q_no += 1
        user_uttar = input(f"Q.(self.q_no): (current.que): (True/false)")
        self.check(user_uttar,current.answer)

    def check(self,user_uttar,answer):
        if user_uttar.lower() == answer.lower():
         self.marks +=2

        else:
            self.marks -= 1
        
