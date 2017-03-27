
import pickle

from PyQt5.QtWidgets import QFileDialog


class Property():
    def __init__(self, key, name, value, ed_izm, types):
        super().__init__()
        self.Key=key
        self.Name=name
        self.Value=value
        self.Ed_izm=ed_izm#"m<sup>3</sup>"
        self.Type=types # 0-группа, 1-переменная
    def __str__(self):
        return "key={}, Name={}, Value={}, Ed_izm={}, Тип={}".format(self.Key,self.Name,self.Value, self.Ed_izm, self.Type)

class Variables:
    def __init__(self):
        super().__init__()
        self.List = [\
            Property(0,"Входные данные к расчету",0,"",0),\
                Property(1,"Угол подачи, β",20,"гр.",1),\
            #"г/сm<sup>3</sup>
                Property(2, "Средний угол наклона образующей \nвалка к оси прокатки, ɑ", 12, "гр.", 1), \
                Property(3, "Длина калибрующего участка, lк", 8, "mm", 1), \
                Property(4, "Частота вращения валков, n", 180, "мин<sup>-1</sup>", 1), \
                Property(5, "Отношение коэффициентов осевой и \nтангенциальной скорости на выходе \nиз очага деформации, η0/ηТ",0.9, "", 1), \
                Property(4, "Kоэфицент использования стана, K", 1, "", 1), \


            Property(4, "Группа 2", 0, "", 0), \
                Property(5, "Переменная 1", 10, "m<sup>3</sup>", 1), \
                Property(6, "Переменная 2", 10, "m<sup>3</sup>", 1), \
                Property(7, "Переменная 2", 10, "m<sup>3</sup>", 1),
                     ]
    def __str__(self, *args, **kwargs):
        str=""
        for k in self.List:
            str="{} {}\n".format (str, k)
        return str
    def info (self):
        str=""
        for k in self.List:
            str="{} {}<br>".format (str, k)
        return str

    def save(self, file):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        with file:
            # Pickle the 'data' dictionary using the highest protocol available.
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)
        #print(self)

    def load(self, file):
        #ouf = open('datafile.dat', 'w')
        #marshal.dump(self, ouf,1)
        #ouf.close()
        # fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        #
        # if fname[0]:
        #     # #f = open(fname[0], 'r')
        #     #
        #     # with f:
        #     #     data = f.read()
        #     #     self.textEdit.setText(data)
        #     f = open(fname[0], 'rb')
        with  file:
                # The protocol version used is detected automatically, so we do not
                # have to specify it.
            #print (file)
            new = pickle.load(file)
        self.List=new.List
        #print (self)


