import marshal
import pickle


class Variable:
    def __init__(self):
        super().__init__()
        #self.A={0:"Группа 1","Пременная 1":10,"Пременная 2":20.2}
        self.A = {0: "Группа 1", "Пременная 1": 1}
        self.B = {0: "Группа 2", "Пременная 1": 10, "Пременная 2": 20.2}
        print (len (self.A))
    def __str__(self, *args, **kwargs):
        str=""
        for k, v in self.A.items():
            str="{} {} = {}\n".format(str,k,v)
        for k, v in self.B.items():
            str = "{} {} = {}\n".format(str, k, v)
        return str
    def test (self):
        pass

    def save(self):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        with open('data.pickle', 'wb') as f:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        print(self)

    def load(self):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        with open('data.pickle', 'rb') as f:
            # The protocol version used is detected automatically, so we do not
            # have to specify it.
            self = pickle.load(f)
        print (self)
