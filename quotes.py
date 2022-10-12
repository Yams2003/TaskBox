import random

def Quotes():
    QUOTE_DICT = {"patience" : [["\"Patience, grasshopper\", said Maia. \"Good things come to those who wait.\" \"I always thought that was \'Good things come to those who do the wave\'\", said Simon. \"No wonder I\'ve been so confused all my life.\"",
                            "Cassandra Clare",
                            "City of Glass"],
                            ["He that can have patience can have what he will.",
                            "Benjamin Franklin",
                            ""],
                            ["Patience is bitter, but its fruit is sweet.",
                            "Aristotle",
                            ""],
                            ["Why is patience so important? Because it makes us pay attention.",
                            "Paulo Coelho",
                            ""],
                            ["Patience, he thought. So much of this was patience - waiting, and thinking and doing things right. So much of all this, so much of all living was patience and thinking.",
                            "Gary Paulsen",
                            "Hatchet"],
                            ["Waiting and hoping is a hard thing to do when you've already been waiting and hoping for almost as long as you can bear it.",
                            "Jenny Nimmo",
                            "Charlie Bone and the Time Twister"],
                            ["But if we hope for what we do not see, we wait for it with patience.",
                            "",
                            "The Bible, Romans 8, 25"]],
             }
    QUOTES = sorted(QUOTE_DICT['patience'], key=lambda k: random.random())
    num = random.randint(0, 6)
    for i in QUOTE_DICT['patience'][num]:
        return i