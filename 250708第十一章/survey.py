class AnonymousSurvey:
    def __init__(self,question):
        self.question=question
        self.responses=[]

    def show_question(self):
        print(self.question)

    def store_response(self,new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print('survey results:')
        for response in self.responses:
            print(f"-{response}")
