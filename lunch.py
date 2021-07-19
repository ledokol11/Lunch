#Launch GENERATOR
import random
Main_Lanch = [' Izgara_Köfte', ' Tavuk_Şiş', 
' Tavuk_Kanat', ' Tavuk_Pirzola',' Et_Şiş', ' Çöp_Şiş' ,' Tavuk_Bonfile']
Salata = [' Çoban_Salata', ' Ezme_Salata',' Mevsim_Salata']
Tatlilar = [' Fırın_Sütlüaç', ' Katmer_Tatlısı', ' Künefe']

print("Welcome to the Lanch  Generator!")
nr_letters= int(input("Choose please number from 1 to 7? \n")) 
nr_symbols = int(input(f"Choose please number from 1 to 3? \n"))
nr_numbers = int(input(f"Choose please from 1 to 3?\n"))

lanch = ''

for char in range(nr_letters):
  lanch += random.choice(Main_Lanch)
for char in range (nr_symbols):
  lanch += random.choice(Salata)
for char in range(nr_numbers):
  lanch +=random.choice(Tatlilar)
print(lanch)    