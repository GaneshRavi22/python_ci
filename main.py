import random

buzz = ['continuous testing', 'continuous integration','continuous deployment', 'continuous improvement', 'dev ops']
adjectives = ['complete', 'modern', 'self-service', 'integrated', 'end-to-end']
adverbs = ['remarkably', 'enormously', 'substantially', 'significantly','seriously']
verbs = ['accelerates', 'improves', 'enhances', 'revamps', 'boosts']

class Main():

    def getString(self):
        return " ".join([random.choice(buzz), random.choice(adjectives), random.choice(adverbs), random.choice(verbs)])