players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]
    def show_stats(self):
        print(f"Name: {self.name} \n Age: {self.age}\n Position: {self.position} \n Team: {self.team}")
        return self
    @classmethod
    def get_team(cls, team_list_of_dict):
        new_team=[]
        for player_dict in team_list_of_dict:
            print("           fluffy bunny          ")
            player=Player(player_dict)
            new_team.append(player)
            player.show_stats()



kevin= Player(kevin)
jason=Player(jason)
kyrie=Player(kyrie)

kevin.show_stats()
jason.show_stats()
kyrie.show_stats()

#list- uses Indexes insode brackets to access info 
#Dictionaries- uses Keys inside brackets to access info 
#Calling class methods- uses Dot notation to call functions

new_team=[]
for player_dict in players:
    print("           fluffy bunny          ")
    player=Player(player_dict)
    new_team.append(player)
    player.show_stats()

print(new_team)
