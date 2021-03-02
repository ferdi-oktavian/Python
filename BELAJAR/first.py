class hero_abang:
    def __init__(self, inputNama, inputDarah, inputPertahanan, inputSkill):
        self.nama = inputNama
        self.darah = inputDarah
        self.pertahanan = inputPertahanan
        self.kemampuan = inputSkill
abang1 = hero_abang("ferdy", 99999, 999999, "banyak")
dira2 = hero_abang("dira", 1, 1, "lari")
jaki3 = hero_abang("jaki", 0, 0, "terbang ")
orang4 = hero_abang("people", -1, -1 , "tidak ada")

class corsair:
    def __init__(self, Born, Live, statues):
        self.lahir = Born
        self.tinggal = Live
        self.status = statues

data1 = corsair("Turkey", "Singapore", "Single")
data2 = corsair("Malaysia", "Rusia", "Date")
data3 = corsair('depok', 'jakarta', 'single')
data4 = corsair('jakarta', 'indonesia', 'single')

print(abang1.__dict__)
print(dira2.__dict__)
print(jaki3.__dict__)
print(orang4.__dict__)
print(data1.__dict__)
print(data2.__dict__)
print(data3.__dict__)
print(data4.__dict__)



