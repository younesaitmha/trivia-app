import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app('testing')
        self.client = self.app.test_client

        setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_category = {
            'type': 'Artificial Intelligence'
        }
        self.new_question = {
            'question': 'when python is created?',
            'answer': '1991',
            'difficulty': 3,
            'category': 1,
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        ''' test getting categories '''

        res = self.client().get('/api/v1.0/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertGreater(len(data['categories']), 0)

    def test_get_paginated_questions(self):
        ''' test getting questions paginated '''

        # specify page 1
        response = self.client().get('/api/v1.0/questions?page=1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertGreater(len(data['questions']), 0)
        self.assertEqual(type(data['total_questions']), int)
        self.assertGreater(data['total_questions'], 0)

    def test_404_paginated_questions(self):
        ''' testing 404 error with invalid page's number '''

        # get the valid number of pages
        questions = Question.query.all()
        # give a number out of range
        invalid_page = len(questions) // 10 + 10
        res = self.client().get(f'/api/v1.0/questions?page={invalid_page}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)

    def test_get_questions_by_category(self):
        ''' test getting questions by a specific category '''

        # get a random category attributes
        category = Category.query.order_by(func.random()).first()
        # query all questions of this category
        questions = Question.query.filter(
            Question.category == str(category.id)
        ).all()

        response = self.client().get(
            f'/api/v1.0/categories/{category.id}/questions'
        )
        data = json.loads(response.data)

        # test if this category has no questions, request will return error 404
        if len(questions) == 0:
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['success'], False)
        else:
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['success'])
            self.assertEqual(len(data['questions']), len(questions))
            self.assertEqual(data['total_questions'], len(questions))
            self.assertEqual(data['current_category'], category.type)

    def test_404_get_questions_by_category(self):
        ''' test error 404 by passing in the request nonexisting category id'''

        # query the last id in the table of categories
        id_not_in_db = Category.query.order_by(
            Category.id.desc()).first().id + 2
        response = self.client().get(
            f'/api/v1.0/categories/{id_not_in_db}/questions')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_delete_question(self):
        ''' test deleting a question by inserting one and delete it '''

        question = Question(
            question=self.new_question['question'],
            answer=self.new_question['answer'],
            difficulty=self.new_question['difficulty'],
            category=self.new_question['category']
        )

        # insert a question
        question.insert()

        # query the inserted question
        question_to_delete = Question.query.order_by(
            Question.id.desc()).first()
        res = self.client().delete(
            f'/api/v1.0/questions/{question_to_delete.id}')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], question_to_delete.id)

    def test_404_delete_question(self):
        ''' test error 404 in delete question by passing to the URI
            nonexisting question's id '''

        # query the last id in the table of questions
        question_id_not_in_db = Question.query.order_by(
            Question.id.desc()).first().id
        res = self.client().delete(
            f'/api/v1.0/questions/{question_id_not_in_db+2}')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'not found')

    def test_create_question(self):
        ''' test create question '''

        res = self.client().post('/api/v1.0/questions', json=self.new_question)
        questions = Question.query.order_by(Question.id.desc()).all()
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['question'], self.new_question['question'])
        self.assertEqual(data['id'], questions[0].id)
        self.assertEqual(data['total_questions'], len(questions))

    def test_400_not_created_question(self):
        ''' test creating question by passing bad request '''

        # make the question none
        self.new_question['question'] = None
        res = self.client().post('/api/v1.0/questions', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "bad request")
        self.assertEqual(data['error'], 400)

    def test_search_question(self):
        ''' test searching questions by inserting a question
            and search by this question '''

        question = Question(
            question=self.new_question['question'],
            answer=self.new_question['answer'],
            difficulty=self.new_question['difficulty'],
            category=self.new_question['category']
        )

        # insert a question
        question.insert()

        # search by inserted question
        response = self.client().post('/api/v1.0/questions/search',
                                      json={'searchTerm': question.question})

        data = json.loads(response.data)

        # query the questions that has the inserted question in the question
        # attribute
        search_results = Question.query.filter(
            Question.question.ilike(f'%{question.question}%')).all()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), len(search_results))
        self.assertEqual(data['total_questions'], len(search_results))

    def test_play_quiz(self):
        ''' tests playing a quiz '''

        # query db for 2 random questions
        questions = Question.query.order_by(func.random()).limit(2).all()
        previous_questions = [question.id for question in questions]
        # post response json, then load the data
        response = self.client().post('/api/v1.0/quizzes', json={
            'previous_questions': previous_questions,
            'quiz_category': {'id': 1}
        })
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['question'])

    def test_failed_play_quiz(self):
        ''' tests playing a quiz with empty json '''

        # post bad data json response json, then load the data
        response = self.client().post(
            '/api/v1.0/quizzes', json={'pip8': 'null'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], 400)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
