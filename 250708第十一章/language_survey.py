from survey import AnonymousSurvey

question='what language did you first learn to speak?'
language_survey=AnonymousSurvey(question)

language_survey.show_question()
print("enter 'q' to quit")
while True:
    response=input('language:')
    if response == 'q':
        break
    language_survey.store_response(response)

print('thank u to everyone!')
language_survey.show_results()

