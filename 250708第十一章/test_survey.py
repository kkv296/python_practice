import pytest
from survey import AnonymousSurvey
@pytest.fixture
def language_survey():
    '''一个可供所有测试函数使用的AnonymousSurvey实例'''
    question='what language did you first learn to speak?'
    language_survey=AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    '''单个答案会被储存'''
    language_survey.store_response('english')
    assert 'english' in language_survey.responses
    
def test_store_three_reaponses(language_survey):
    '''三个答案会被储存'''
    responses=['english','spanish','mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses