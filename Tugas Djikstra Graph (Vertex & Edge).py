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
    
    def djikstra(self, source):
        distance = {}
        for city in self.cityList:
            distance[city] = float("inf")
        distance[source] = 0

        unvisited_cities = list(self.cityList.keys())

        while unvisited_cities:
            min_distance = float("inf")
            closest_city = None

            for city in unvisited_cities:
                if distance[city] < min_distance:
                    min_distance = distance[city]
                    closest_city = city

            unvisited_cities.remove(closest_city)

            for neighbor, jarak in self.cityList[closest_city].items():
                jarakNeighbor = distance[closest_city] + jarak
                if jarakNeighbor < distance[neighbor]:
                    distance[neighbor] = jarakNeighbor
        return distance

petaIndonesia = Peta()
petaIndonesia.tambahkanKota("Bangkalan")
petaIndonesia.tambahkanKota("Lamongan")
petaIndonesia.tambahkanKota("Bojonegoro")
petaIndonesia.tambahkanKota("Gresik")
petaIndonesia.tambahkanKota("Surabaya")
petaIndonesia.tambahkanKota("Sidoarjo")
petaIndonesia.tambahkanKota("Mojokerto")
petaIndonesia.tambahkanKota("Nganjuk")
petaIndonesia.tambahkanKota("Pasuruan")
petaIndonesia.tambahkanKota("Malang")
petaIndonesia.tambahkanKota("Probolinggo")
petaIndonesia.tambahkanKota("Lumajang")
petaIndonesia.tambahkanKota("Kediri")
petaIndonesia.tambahkanKota("Blitar")

petaIndonesia.tambahkanJalan("Bangkalan", "Surabaya", 31)
petaIndonesia.tambahkanJalan("Surabaya", "Sidoarjo", 26)
petaIndonesia.tambahkanJalan("Sidoarjo", "Pasuruan", 45)
petaIndonesia.tambahkanJalan("Pasuruan", "Probolinggo", 46)
petaIndonesia.tambahkanJalan("Probolinggo", "Lumajang", 47)
petaIndonesia.tambahkanJalan("Lumajang", "Malang", 142)
petaIndonesia.tambahkanJalan("Malang", "Mojokerto", 127)
petaIndonesia.tambahkanJalan("Mojokerto", "Gresik", 52)
petaIndonesia.tambahkanJalan("Gresik", "Lamongan", 30)
petaIndonesia.tambahkanJalan("Lamongan", "Bojonegoro", 88)
petaIndonesia.tambahkanJalan("Bojonegoro", "Nganjuk", 55)
petaIndonesia.tambahkanJalan("Nganjuk", "Kediri", 35)
petaIndonesia.tambahkanJalan("Kediri", "Blitar", 40)
petaIndonesia.tambahkanJalan("Blitar", "Malang", 76)
petaIndonesia.tambahkanJalan("Surabaya", "Gresik", 20)
petaIndonesia.tambahkanJalan("Sidoarjo", "Malang", 70)
petaIndonesia.tambahkanJalan("Mojokerto", "Kediri", 80)
petaIndonesia.tambahkanJalan("Lamongan", "Surabaya", 46)
petaIndonesia.tambahkanJalan("Pasuruan", "Malang", 76)
petaIndonesia.tambahkanJalan("Sidoarjo", "Mojokerto", 30)

print('------------------------------')
jarakSemuaKotaDariBangkalan = petaIndonesia.djikstra("Surabaya")
print("Jarak kota berikut dari Surabaya adalah :")
for city,distance in jarakSemuaKotaDariBangkalan.items():
    print(city," adalah ",distance," KM")

indonesia = ["Surabaya", "Sidoarjo", "Malang"]
print(list(permutations(indonesia)))

petaIndonesia.printPeta()
print('------------------------------')
petaIndonesia.hapusKota("Bangkalan")
petaIndonesia.printPeta()
