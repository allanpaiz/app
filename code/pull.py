import json

with open('liverpool.json' , encoding='utf8') as f:
    data = json.load(f)

games = data['sports_results']['games']


for x in range(0,6):
    test = list(games[x].keys())
    print(test)


#############################
############################
###########################
##########################
######## BELOW IS TEST CODE ################
# for x in range(1,10):
#     a = x
#     print(a)
# print(type(a))
#--
# print(games[0]['tournament'])
#--
# g = list(games.keys())[0]
# print(g)
#--
# for gamess in games:
#     # if gamess[]
#     print(games.keys())
#--
# print(type(data['sports_results']) <<<<<<<<<<< this is a flippin dictionary, inside of a dictionary
#--
# for sports_results in data['sports_results']:
#     print(sports_results)