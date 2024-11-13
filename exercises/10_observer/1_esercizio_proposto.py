"""
Scrivere una classe LaureaT_Student che possa essere osservata e che possieda i seguenti attributi che ne determinano lo stato:
total_cfu: numero di CFU acquisiti.
english_r: valore booleano impostato su False (valore predefinito) se e solo se lo studente non ha superato la prova di inglese.
grades: dizionario degli esami sostenuti, in cui le chiavi corrispondono ai nomi degli esami e i valori ai voti ottenuti (nome dell'esame, voto).
exam: una tupla del tipo definito di seguito:
Exam = collections.namedtuple("Exam", "name cfu").
Gli attributi total_cfu ed english_r sono accessibili direttamente tramite il loro nome e possono essere modificati con l'operatore =. L'attributo grades, invece, è modificabile attraverso il metodo add_grades, che accetta come primo argomento un oggetto di tipo Exam e come secondo argomento un intero che rappresenta il voto. Inoltre, è necessario implementare due observer: HistoryView e LiveView.
HistoryView mantiene una lista di triple della forma (dizionario degli esami sostenuti, booleano che indica se l'esame di inglese è stato superato, data del cambiamento di stato). Ogni tripla viene creata quando l'oggetto LaureaT_Student cambia stato.
LiveView esegue le seguenti stampe:
print("Cambio stato: lo studente ha appena superato la prova di Inglese\n") se il cambiamento di stato è dovuto al superamento della prova di inglese.
print("Cambio stato: lo studente ha superato un nuovo esame").
print("Cambio stato: il numero di CFU è: ", student.total_cfu, "\n") se il cambiamento di stato è dovuto al superamento di un nuovo esame.
"""
import collections
import time
import datetime
import itertools

# Definizione del tipo Exam
Exam = collections.namedtuple("Exam", "name cfu")

# Classe osservabile LaureaT_Student
class LaureaT_Student:
    def __init__(self):
        self.__observers = set()
        self.total_cfu = 0
        self.english_r = False
        self.grades = {}

    def observers_add(self, observer, *observers):
        for obs in itertools.chain((observer,), observers):
            self.__observers.add(obs)
            obs.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)

    def add_grades(self, exam, grade):
        self.grades[exam.name] = grade
        self.total_cfu += exam.cfu
        self.observers_notify()

    def pass_english(self):
        if not self.english_r:
            self.english_r = True
            self.observers_notify()

# Classe HistoryView (osservatore)
class HistoryView:
    def __init__(self):
        self.data = []

    def update(self, student):
        state = (dict(student.grades), student.english_r, time.time())
        self.data.append(state)

# Classe LiveView (osservatore)
class LiveView:
    def update(self, student):
        if student.english_r:
            print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")
        else:
            print("Cambio stato: il numero di CFU è:", student.total_cfu, "\n")
        print("Cambio stato: lo studente ha superato un nuovo esame.\n")

# Esempio di utilizzo
def main():
    # Creazione degli osservatori
    history_view = HistoryView()
    live_view = LiveView()

    # Creazione dell'oggetto osservato
    student = LaureaT_Student()
    student.observers_add(history_view, live_view)

    # Aggiunta di esami e cambiamenti di stato
    exams = [Exam("Matematica", 8), Exam("Fisica", 6)]
    for exam in exams:
        student.add_grades(exam, 28)  # Aggiunge l'esame con voto 28

    # Superamento della prova di Inglese
    student.pass_english()

    # Stampa la cronologia dei cambiamenti
    for state in history_view.data:
        grades, english_passed, timestamp = state
        print("Esami sostenuti:", grades)
        print("Prova di Inglese superata:", english_passed)
        print("Data del cambiamento:", datetime.datetime.fromtimestamp(timestamp), "\n")

if __name__ == "__main__":
    main()
