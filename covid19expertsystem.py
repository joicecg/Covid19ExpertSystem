from experta import *
import sys


class Disease(Fact):
    """Informasi Mengenai Penyakit Gejala Covid-19"""

def SUMFIELDS(p, *fields):
    return sum([p.get(x, 0) for x in fields])

class DiseaseRobot(KnowledgeEngine):
    @Rule(Disease(when_start_sick=P(lambda x: x <= 14)))
    def is_sick(self):
        self.declare(Fact(sick=True))

    @Rule(Fact(sick=True),
        Disease(cough=True),
        Disease(fever=True),
        Disease(muscle_pain=True),
        Disease(vomiting=True),
        Disease(headache=True),
        Disease(short_of_breath=False),
        Disease(loss_of_taste_smell=False),
        Disease(sore_throat=False),
        Disease(diare=False),
        Disease(fatigue=False),
        Disease(travel_last_14=False),
        Disease(health_care_worker=False),
        Disease(interacted_with_covid=False))
    def malaria(self):
        print("Anda terindikasi diserang penyakit malaria dikarenakan anda tidak memiliki gejala kesulitan bernapas, diare, kecapekan dan hilang penciuman")
        print("Silahkan segera pergi ke pusat kesehatan terdekat untuk diberi obat antimalaria dan kombinasi obat ACT untuk diobati")
        self.declare(Fact(malaria=True))

    @Rule(Fact(sick=True),
        AS.p << Disease(), TEST(lambda p: SUMFIELDS(p, 'cough','fever','headache', 'short_of_breath','loss_of_taste_smell','sore_throat','diare','fatigue') > 4))
    def covid_positive(self, p):
        self.declare(Fact(covid_positive=True))
    
    @Rule(Fact(sick=True),
        AS.p << Disease(), TEST(lambda p: SUMFIELDS(p, 'cough','fever','headache', 'short_of_breath','loss_of_taste_smell','sore_throat','diare','fatigue') < 4))
    def general_syn(self, p):
        self.declare(Fact(general_syn=True))
    
    @Rule(Fact(sick=True),
        AS.p << Disease(), TEST(lambda p: SUMFIELDS(p, 'cough', 'fever', 'headache','vomiting','muscle_pain','short_of_breath', 'loss_of_taste_smell', 'sore_throat', 'diare', 'fatigue', 'travel_last_14', 'health_care_worker', 'interacted_with_covid') == 0 ))
    def covid_negative(self, p):
        self.declare(Fact(covid_negative=True))

    @Rule(Fact(sick=True),
        AS.p << Disease(), TEST(lambda p: SUMFIELDS(p, 'travel_last_14','health_care_worker','interacted_with_covid') < 1))
    def severe_covid(self, p):
        self.declare(Fact(severe_covid=True))

    @Rule(Fact(sick=True),
        AS.p << Disease(), TEST(lambda p: SUMFIELDS(p, 'travel_last_14','health_care_worker','interacted_with_covid') > 1))
    def interacted_with_covid(self, p):
        self.declare(Fact(interact_with_covid=True))

    @Rule(Fact(sick=True),Fact(covid_positive=True),Fact(severe_covid=True))
    def high_risk(self):
        print("\nAnda memiliki resiko covid-19 yang tinggi dikarenakan anda memiliki gejala covid yang tinggi dan kamu tidak ada histori perjalanan dan keluarga yang terserang penyakit corona, sehingga kemungkinan anda terkena dari lingkungan \n")
        print("Jauhi orang-orang sekitar dan segera pergi ke dokter untuk lakukan pengecekan lebih lanjut")
        self.declare(Fact(high_risk=True))

    @Rule(Fact(sick=True),Fact(covid_positive=True),Fact(interact_with_covid=True))
    def high_risk_interact(self):
        print("\nAnda memiliki resiko Covid-19 yang amat tinggi dikarenakan anda memiliki gejala covid dan kamu mungkin pernah melakukan perjalanan keluar negeri, keluarga terkena covid-19 dan lingkunganmu terkontaminasi \n")
        print("Segera kerumah sakit untuk diperiksa karena tingkat kemungkinan anda terserang amat tinggi")
        self.declare(Fact(high_risk_interact=True))

    @Rule(Fact(sick=True),Fact(covid_negative=True))
    def no_risk(self):
        print("Anda tidak memiliki gejala covid-19 maupun maleria, silahkan konsultasi penyakit anda ke rumah sakit terdekat")
        self.declare(Fact(no_risk=True))
    
    @Rule(Fact(sick=True),Fact(general_syn=True),Fact(severe_covid=True))
    def no_risk_covid(self):
        print("Anda tidak memiliki gejala covid-19 maupun maleria, silahkan konsultasi penyakit anda ke rumah sakit terdekat")
        self.declare(Fact(no_risk_covid=True))


engine = DiseaseRobot()
engine.reset()

print("Expert System Covid-19, Silahkan jawab pertanyaan ini dengan 'Ya' atau 'Tidak'")
val1 = input(
    "Sejak kapan anda merasa sakit? (Silahkan jawab dalam jumlah hari 1-30 hari) :")
val2 = input("Apakah anda memiliki gejala batuk? :")
if val2 == "Ya":
    val2 = True
else:
    val2 = False
val3 = input("Apakah anda memiliki gejala demam? :")
if val3 == "Ya":
    val3 = True
else:
    val3 = False
val4 = input("Apakah anda memiliki gejala sakit terhadap otot? :")
if val4 == "Ya":
    val4 = True
else:
    val4 = False
val5 = input("Apakah anda memiliki gejala muntah-muntah? :")
if val5 == "Ya":
    val5 = True
else:
    val5 = False
val6 = input("Apakah anda memiliki gejala sakit kepala? :")
if val6 == "Ya":
    val6 = True
else:
    val6 = False
val7 = input("Apakah anda memiliki gejala kesulitan bernapas? :")
if val7 == "Ya":
    val7 = True
else:
    val7 = False
val8 = input("Apakah anda memiliki gejala kehilangan cita rasa makanan dan perciuman? :")
if val8 == "Ya":
    val8 = True
else:
    val8 = False
val9 = input("Apakah anda memiliki gejala tengorokan kering? :")
if val9 == "Ya":
    val9 = True
else:
    val9 = False
val10 = input("Apakah anda memiliki gejala diare? :")
if val10 == "Ya":
    val10 = True
else:
    val10 = False
val11 = input ("Apakah anda memiliki gejala kecapekan? :")
if val11 == "Ya":
    val11 = True
else:
    val11 = False
val12 = input("Apakah anda memiliki riwayat perjalanan keluar negeri dalam 14 hari belakangan? :")
if val12 == "Ya":
    val12 = True
else:
    val12 = False
val13 = input("Apakah anda merupakan pekerja medis? :")
if val13 == "Ya":
    val13 = True
else:
    val13 = False
val14 = input("Apakah keluarga anda ada yang sudah pernah terjangkit oleh Covid-19 dalam 14 hari belakangan? :")
if val14 == "Ya":
    val14 = True
else:
    val14 = False

engine.declare(Disease(when_start_sick=int(val1),cough=val2,fever=val3,muscle_pain=val4,vomiting=val5,headache=val6,short_of_breath=val7,loss_of_taste_smell=val8,sore_throat=val9,diare=val10,fatigue=val11,travel_last_14=val12,health_care_worker=val13,interacted_with_covid=val14))

engine.run()

    




    
    

