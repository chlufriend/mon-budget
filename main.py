revenue = 110
transport = 10
loisirs = 20
nourriture = 40

revenue = float(input("Veuillez enter Revenue Mensuel : $" ))
transport = float(input("Veuillez enter Transport : $" ))
loisirs = float(input("Veuillez enter Loisirs : $" ))
nourriture = float(input("Veuillez enter nourriture : $" ))

depense = transport + loisirs + nourriture
reste = revenue - depense

if reste > 80 :
  print("Very good budget!")
elif reste > 0:
  print("Moyen budget!")
else:
  print("Faire attention a votre budget!")

expenses = {
  "transport": 10, 
  "loisirs": 20, 
  "nourriture": 40
           }
for category, amount in expenses.item():
  print(category, amount)
  
total = sum(expenses)
print(total)

def ajouter_depense():
  categorie = input("Categorie: ")
  amount = input("Amount")


print("----------------------------------")
print("   Mon budget Question Algebre")
print("----------------------------------")

nom = input("Nom du joueur: ")
revenue = float(input("Veuillez enter Revenue Mensuel : $" ))

argent = revenue
print("Bienvenue", nom "!")
print("Ton revenu est de $", revenue)

nombre = random.randint(10,50)
print("Resous l'equation : ")
print("")
