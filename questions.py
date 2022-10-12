import random

def Questions():
    QUOTE_DICT = {"questions" : [["Have you ever experienced an \'attack\' of fear, anxiety, or panic?"],
                            ["How often have you felt as though your moods, or your life, were under your control?"],
                            ["How confident you have been feeling in your capabilities recently?"],
                            ["How have you been feeling about your relationships recently?"],
                            ["Are you having trouble focusing at work or school?\nCan you concentrate on the things I want to do?\nDo you find pleasure in things that usually make you happy?"],
                            ["What are 3 things are you grateful for today?"],
                            ["What are your energy levels like when you finish the day?\nAre there any significant changes in your energy?"]],
             }
    QUESTIONS = sorted(QUOTE_DICT['questions'], key=lambda k: random.random())
    num = random.randint(0, 6)
    for i in QUOTE_DICT['questions'][num]:
        return i