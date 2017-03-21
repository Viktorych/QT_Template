class Variable:
    def __init__(self):
        super().__init__()
        self.A={0:"Группа 1","Пременная 1":10,"Пременная 2":20.2}
        self.B = {"Группа 2": "Группа 2", "Пременная 1": 10, "Пременная 2": 20.2}
    def __str__(self, *args, **kwargs):
        str=""
        for k, v in self.A.items():
            str="{} {} = {}\n".format(str,k,v)
        for k, v in self.B.items():
            str = "{} {} = {}\n".format(str, k, v)
        return str
    def test (self):
        pass
