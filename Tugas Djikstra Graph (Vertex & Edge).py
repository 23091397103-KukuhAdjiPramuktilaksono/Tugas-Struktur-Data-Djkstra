from itertools import permutations

class Peta: 
    def __init__(self):
        self.cityList = {}

    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
            for neighbor, distance in self.cityList[kota].items():
                print("    ->", neighbor,":",distance)

    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = {}
            return True
        return False
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            for kotalain in self.cityList:
                if kotaDihapus in self.cityList[kotalain]:
                    del self.cityList[kotalain][kotaDihapus]
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota2][kota1] = jarak
            self.cityList[kota1][kota2] = jarak
            return True
        return False
    
    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            del self.cityList[kota2][kota1]
            del self.cityList[kota1][kota2]
            return True
        return False
    
    
