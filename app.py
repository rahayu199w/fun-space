print('##  Program Python Menghitung Luas Segitiga  ##')
print('===============================================')
print()
 
def hitungLuasSegitiga(a,t):
  return round(0.5 * a * t,2)
 
alas = float(input('Input alas segitiga: '))
tinggi = float(input('Input tinggi segitiga: '))
print('Luas segitiga = ',hitungLuasSegitiga(alas, tinggi))