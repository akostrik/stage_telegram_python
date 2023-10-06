class Characteristic:
    def __init__(self, score, name):
        self.name  = name.strip()
        try:
            self.score = int(score)
        except ValueError:
            self.score = int(0)
            print ("you should give integer score")
 
    def to_string(self):
        return f"{self.name}: {{if true reply {self.score}, if false reply 0, if neutral reply 0}}\n" 

    def __str__(self):
        return f"Characteristic(Name: {self.name}, Score: {self.score})"