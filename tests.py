import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id is not None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_empty_title():
    with pytest.raises(Exception):
        Question(title='')

def test_create_question_with_wrong_title():
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        question = Question(title='q1', points=-1)
    with pytest.raises(Exception):
        question = Question(title='q1', points=101)

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_access_invalid_choice():
    with pytest.raises(Exception):
        question = Question(title='q1')
        choice = question.choices[0]
    with pytest.raises(Exception):
        question = Question(title='q1')
        question.add_choice('a', False)
        choice = question.choices[1]

def test_access_correct_choice():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', True)

    choice = question.choices[1]
    assert choice.text == 'b'
    assert choice.is_correct

def test_create_multiple_choices():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', False)

    choice = question.choices[2]
    assert len(question.choices) == 3
    assert choice.text == 'c'
    assert not choice.is_correct

def test_create_choice_with_wrong_title():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('a'*201, False)

def test_create_choice_without_title():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)

def test_question_with_multiples_selections():
    question = Question(title='q1', max_selections= 2)
    assert question.max_selections == 2

def test_question_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)

    assert len(question.choices) == 2
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_find_test_by_id():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)

    choice = question.choices[0]
    id = choice.id
    assert question._find_choice_by_id(id) == choice

@pytest.fixture
def test_question():
    question = Question(title='q1')
    question.add_choice('a', False)
    question.add_choice('b', False)
    question.add_choice('c', True)
    return question

def test_create_test_question(test_question):
    assert test_question is not None

def test_test_question_length(test_question):
    assert len(test_question.choices) == 3


def correct_choice(test_question):
    choice = test_question.choices[0]
    assert choice.text == 'a'
    assert not choice.is_correct

    choice = test_question.choices[2]
    assert choice.text == 'c'
    assert choice.is_correct







