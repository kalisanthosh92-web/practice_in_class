
IGN = input("In Game Name (IGN): ")
Rank = input("Current Rank: ")
Hero = ['Layla','Tigreal','Gusion','Kagura','Chou']
roles =['Marksman','Tank','Assassin','Mage','Fighter']
  
print()
   


print('=' * 50)
print(f'{'MOBILE LEGENDS --HERO ROSTER':^50}')
print('='*50)
for i in range(1,6):
    print(f'    {i}.  {Hero[i-1]:<20}{roles[i-1]:^10} ')
print('='*50)
print()

matches = []
matches_played = 0
wins = 0
loss = 0
best_played = 0 

for j in range(1,5):
    print()
    print(f'--- MATCH {j} ---')
    hero_number = int(input('Hero number (0 to skip): '))
    if hero_number == 0 or hero_number <1 or hero_number > 5 :
        continue
    else: 
        kills = int(input('Kills: '))
        Deaths = int(input('Deaths: '))
        Assists = int(input('Assists: '))
        Result = input('Result(W/L): ').lower()
        
        if Result == 'w':
            match_result = 'Win'
            wins += 1
        else :
            match_result = 'Loss'
            loss += 1 

        while Deaths == 0:
            KDA = (kills + Assists)/1 
        else : 
            KDA = (kills + Assists)/Deaths
            

        if KDA >= 5 and Result == 'w':
            tag = 'DOMINATION!'
        elif KDA >= 5 and Result == 'l':
            tag = "Carried Hard"
        elif KDA < 5 and Result == 'w':
            tag = 'Team Effort'
        elif KDA < 5 and Result == 'l':
            tag = 'Better Luck Next Game'
        matches_played += 1

        


        each_match = [matches_played,Hero[hero_number-1],KDA,match_result,tag]
        matches.insert(matches_played,each_match)

        if KDA > best_played:
            best_played = KDA


print()
print('=' * 50)
print(f"{str(IGN) + ' -- MATCH LOG (' + str(Rank) + ')':^50}")
print('='*50)
for i in range(len(matches)):
    #print('['+ str(matches[i][0])+']',matches[i][1]+'\t\t|',str(matches[i][2])+'\t |',matches[i][3]+'\t |',matches[i][4])
    print(f'[{matches[i][0]}] {matches[i][1]:<10}| KDA: {matches[i][2]:.2f}\t | {matches[i][3]}\t | {matches[i][4]}')

print('-'*50)

print('Matches Played : ',matches_played)
print(f'Wins : {wins}   |  Losses : {loss}')
win_rate = ((wins/matches_played)*100)
print(f'Win Rate : {win_rate:.0f}%')


for i in matches:
    if  i[2] == best_played:
        print(f'Best Match\t: [{i[0]}] {i[1]}\t (KDA:{i[2]:.2f})')
 

print('=' * 50)

















    