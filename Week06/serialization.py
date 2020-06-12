import requests
import json
import pickle


class Question:
    """
    Properties:
    - category
    - type
    - difficulty
    - question
    - correct_answer
    - incorrect_answers
    """
    # REFACTORING

    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers


#def __init__(self, *args, **kwargs):
    #self.category = kwargs.get('category')
        #self.type = kwargs.get('type')
        #self.difficulty = kwargs.get('difficulty')
        #self.question = kwargs.get('question')
        #self.correct_answer = kwargs.get('correct_answer')
        #self.incorrect_answers = kwargs.get('incorrect_answers')

    #def __str__(self):
    #    return f'<Question: {self.question} - {self.correct_answer}>'
    def __str__(self):
        return f'Q: {self.question}? A: {self.correct_answer}'

#q = Question('General Knowledge', 'boolean', 'a', 'ISCG5421 the best course you\'ve ever taken.', 'True', 'd')
#print(q)


url = 'https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean'

response = requests.get(url)  # Response Class
#print(response.status_code)
#print(response.text)
response_text = json.loads(response.text)  # Converting from bytes string to dictionary
#print(response_text.keys())
#print(response_text.get('results'))
results = response_text.get('results')

#print(results[0])
#print(results[0].keys())
question_list = []

for result in results:
    question = Question(result['category'], result['type'], result['difficulty'], result['question'], result['correct_answer'], result['incorrect_answers'])
    print(question)
    question_list.append(question)
    #print(type(result))

#f = open('my_questions.txt', 'w')
#for q in question_list:
#    f.write(str(q))
#    f.write('\n')
#f.close()

#with open('my_questions.txt') as f:
#    my_questions = f.readlines()

#f = open('my_questions.txt')
#my_questions = f.readlines()
#print(my_questions)

#def my_function(school, city, *args, **kwargs):
#    print(f'args: {args} - kwargs: {kwargs}')
#
#my_function(1, 2, 3, name='Shea', age=22)
#
#def say_hello(name='Guy', age=25, height='200', weight='120', dob='1969', eye_color='red', hair_color='pink'):  # Keyword Arguments aka kwargs
#    print(f'hello {name}')
#    print(f'age: {age}')
#    print(f'height {height}')
#    print(f'weight {weight}')
#    print(f'dob {dob}')
#    print(f'eye color: {eye_color}')
#    print(f'hair color: {hair_color}')


#say_hello(weight=300, height=150, dob='1905', age=22, name='Shea')

