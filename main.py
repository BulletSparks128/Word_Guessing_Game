import random

# Lista de nomes de Pokémon da primeira geração da região Kanto
words = ['BULBASSAURO', 'IVYSSAURO', 'VENUSAURO', 
         'CHARMANDER', 'CHARMELEON', 'CHARIZARD', 
         'SQUIRTLE', 'WARTORTLE', 'BLASTOISE', 
         'CATERPIE', 'METAPOD', 'BUTTERFREE', 
         'WEEDLE', 'KAKUNA', 'BEEDRILL', 
         'PIDGEY', 'PIDGEOTTO', 'PIDGEOT', 
         'RATTATA', 'RATICATE', 'SPEAROW', 
         'FEAROW', 'EKANS', 'ARBOK', 
         'PIKACHU', 'RAICHU', 'SANDSHREW', 
         'SANDSLASH', 'NIDORANA', 'NIDORINA', 
         'NIDOQUEEN', 'NIDORANO', 'NIDORINO', 
         'NIDOKING', 'CLEFAIRY', 'CLEFABLE', 
         'VULPIX', 'NINETALES', 'JIGGLYPUFF', 
         'WIGGLYTUFF', 'ZUBAT', 'GOLBAT', 
         'ODDISH', 'GLOOM', 'VILEPLUME', 
         'PARAS', 'PARASECT', 'VENONAT', 
         'VENOMOTH', 'DIGLETT', 'DUGTRIO', 
         'MEOWTH', 'PERSIAN', 'PSYDUCK', 
         'GOLDUCK', 'MANKEY', 'PRIMEAPE', 
         'GROWLITHE', 'ARCANINE', 'POLIWAG', 
         'POLIWHIRL', 'POLIWRATH', 'ABRA', 
         'KADABRA', 'ALAKAZAM', 'MACHOP', 
         'MACHOKE', 'MACHAMP', 'BELLSPROUT', 
         'WEEPINBELL', 'VICTREEBEL', 'TENTACOOL', 
         'TENTACRUEL', 'GEODUDE', 'GRAVELER', 
         'GOLEM', 'PONYTA', 'RAPIDASH', 
         'SLOWPOKE', 'SLOWBRO', 'MAGNEMITE', 
         'MAGNETON', 'FARFETCHD', 'DODUO', 
         'DODRIO', 'SEEL', 'DEWGONG', 
         'GRIMER', 'MUK', 'SHELLDER', 
         'CLOYSTER', 'GASTLY', 'HAUNTER', 
         'GENGAR', 'ONIX', 'DROWZEE', 
         'HYPNO', 'KRABBY', 'KINGLER', 
         'VOLTORB', 'ELECTRODE', 'EXEGGCUTE', 
         'EXEGGUTOR', 'CUBONE', 'MAROWAK', 
         'HITMONLEE', 'HITMONCHAN', 'LICKITUNG', 
         'KOFFING', 'WEEZING', 'RHYHORN', 
         'RHYDON', 'CHANSEY', 'TANGELA', 
         'KANGASKHAN', 'HORSEA', 'SEADRA', 
         'GOLDEEN', 'SEAKING', 'STARYU', 
         'STARMIE', 'MRMIME', 'SCYTHER', 
         'JYNX', 'ELECTABUZZ', 'MAGMAR', 
         'PINSIR', 'TAUROS', 'MAGIKARP', 
         'GYARADOS', 'LAPRAS', 'DITTO', 
         'EEVEE', 'VAPOREON', 'JOLTEON', 
         'FLAREON', 'PORYGON', 'OMANYTE', 
         'OMASTAR', 'KABUTO', 'KABUTOPS', 
         'AERODACTYL', 'SNORLAX', 'ARTICUNO', 
         'ZAPDOS', 'MOLTRES', 'DRATINI', 
         'DRAGONAIR', 'DRAGONITE', 'MEWTWO', 
         'MEW']

# Escolhe um nome de Pokémon aleatório da lista
word = random.choice(words)
word = word.replace(' ', '')

name = input("Qual seu nome? ")

print("Boa Sorte,", name, "!")

if __name__ == '__main__':
    print("Adivinhe qual a palavra! Dica: é um Pokémon de 1ª Geração da Região Kanto.")

    guessed_letters = set()
    max_wrong_attempts = 6  # Defina o número máximo de tentativas erradas
    wrong_attempts = 0
    flag = False

    while not flag and wrong_attempts < max_wrong_attempts:
        print()
        for char in word:
            if char in guessed_letters:
                print(char, end=' ')
            else:
                print('_', end=' ')
        
        print()

        if all(char in guessed_letters for char in word):
            print('Parabéns, você acertou a palavra!')
            break

        try:
            guess = input('Digite uma letra: ').upper()

            if len(guess) != 1 or not guess.isalpha():
                print('Digite apenas uma LETRA!')
                continue

            if guess in guessed_letters:
                print('Você já tentou esta letra.')
                continue

            guessed_letters.add(guess)

            if guess in word:
                print('Letra correta!')
            else:
                print('Letra incorreta.')
                wrong_attempts += 1

        except KeyboardInterrupt:
            print()
            print('Tchau!')
            exit()

    if wrong_attempts == max_wrong_attempts:
        print('Você atingiu o limite de tentativas erradas. A palavra era:', word)