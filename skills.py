# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

# Explain each concept.
# 1. Encapsulation: Allows programs to group and contain like concepts together in
# manageable packages.
#
# 2. Abstraction: Lets confusing details be hidden while providind enough
# high-level information for a program to be used successfully. In order to use
# a class, a programer does not need to know every detail of how that class is
# constructed. Understanding the abstract, high-level idea is more helpful.
#
# 3. Polymorphism: different objects can easily be treated interchangeably using
# the power of inheritance.

# 1. What is a class?
# A class is a set of data objects and functions that act on those objects.
# It is a blueprint for an object that serves a purpose and can be manipulated
# as described by the class methods.

# 2. What is an instance attribute?
# An instance attribute is a characteristic of an instance (or object) of a
# class. It is connected to the actual object, and not the class blueprint.

# 3. What is a method?
# A method is a function that is defined in a class. The methods of a class
# typically provide ways to interact with objects of the same class.

# 4. What is an instance in object orientation?
# An instance is a single copy of an item created from the class "blueprint."

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
# A class attribute pertains to the class and every instance created of that
# class unless explicity over-written by an instance attribute. An instance
# attribute applies exclusively to the instance it is associated with.
# For example, if I created a class Fruit, has_seeds might be a useful class
# attribute because all fruits should have seeds (I think). fruit_color would be
# a better instance attribute because fruits come in a variety of colors.

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Stores name and address information for student."""
    def __init__(self, first_name, last_name, address=""):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.score = 0


class Question(object):
    """Question object contains a question and the correct answer."""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Questions user and returns true or false depending on answer."""
        guess = raw_input(self.question + " > ")
        if guess == self.answer:
            return True
        else:
            return False


class Exam(object):
    """Contains questions and name. Executes exam."""
    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question, answer):
        """Adds a question object to the list of questions in the exam"""
        question = Question(question, answer)
        self.questions.append(question)

    def administer(self):
        """Runs through exam questions and asks user.
           Returns number of correct answers.
        """
        score = 0
        for question in self.questions:
            right_guess = question.ask_and_evaluate()
            if right_guess:
                score += 1
        return score


class Quiz(Exam):
    """Quizzes are exactly like exam except all results are pass/fail"""
    def administer(self):
        number_correct = super(Quiz, self).administer()
        total_questions = len(self.questions)
        if float(number_correct)/total_questions > 0.5:
            return True
        else:
            return False


def take_test(student, exam):
    """Adds the exam score to the student object"""
    score = exam.administer()
    student.score = score


def example():
    """Example use of Exam, Student, and Question"""
    exam = Exam("Midterm")
    exam.add_question("What does MRO stand for in Python jargon?",
                      "Method Resolution Order")
    exam.add_question("What is the principle of OOP closely related to Inheritance?",
                      "Polymorphism")
    exam.add_question("A dictionary key can be mutable. True or False?",
                      "False")
    student = Student("Auden", "TheCat", "123 Joel's Place")
    take_test(student, exam)
    # Added print line to test functionality. Looked good.
    # print student.score


def quiz_example():
    """Example use of Exam, Student, and Question"""
    quiz = Quiz("Midterm")
    quiz.add_question("What does MRO stand for in Python jargon?",
                      "Method Resolution Order")
    quiz.add_question("What is the principle of OOP closely related to Inheritance?",
                      "Polymorphism")
    quiz.add_question("A dictionary key can be mutable. True or False?",
                      "False")
    student = Student("Auden", "TheCat", "123 Joel's Place")
    take_test(student, quiz)
    # Added print line to test functionality. Looked good.
    print student.score

# Run example to test if this works.
quiz_example()
