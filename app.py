print('##  Program Python Menghitung Luas Segitiga  ##')
print('===============================================')
print()
 
def hitungLuasSegitiga(a,t):
  return round(0.5 * a * t,2)
 
alas = float(input('Input alas segitiga: '))
tinggi = float(input('Input tinggi segitiga: '))
print('Luas segitiga = ',hitungLuasSegitiga(alas, tinggi))

print('##  Program Python Menghitung Luas Persegi Panjang  ##')
print('======================================================')
print()
 
def hitungLuasPersegiPanjang(p,l):
  return round(p * l,2)
 
panjang = float(input('Input panjang persegi: '))
lebar = float(input('Input lebar persegi: '))
print('Luas persegi panjang = ',hitungLuasPersegiPanjang(panjang, lebar))

print('##  Program Python Menghitung Luas Lingkaran  ##')
print('================================================')
print()
 
def hitungLuasLingkaran(r):
  return round(3.14 * r * r, 2)
 
jari2 = float(input('Input jari-jari lingkaran:  '))
print('Luas lingkaran = ',hitungLuasLingkaran(jari2))