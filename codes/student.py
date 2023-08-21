class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score >100:
            raise ValueError('the value must between 1 and 100!')
        
        if self.score >= 80 :
            return 'A'
        
        elif self.score >= 60 :
            return 'B'
        
        return 'C'