import urllib.request, json 
from collections import defaultdict
import sys

def download_json():
    with urllib.request.urlopen("https://mach-eight.uc.r.appspot.com/") as url:
        data = json.loads(url.read().decode())
        return data['values']

def search_heights(sum_goal, player_list):
    heights = defaultdict(list)
    output = ""
    for player in player_list:
        player_1_name = (player['first_name'], player['last_name'])
        heights[int(player['h_in'])].append(player_1_name)
        if heights[sum_goal - int(player['h_in'])]:
            for player_2_name in heights[sum_goal - int(player['h_in'])]:
                if player_1_name[1] <  player_2_name[1]:
                    #Added some spacing for that the two columns look good
                    output += '{0:30} {1}'.format(f"-{player_1_name[0]} {player_1_name[1]}",f"{player_2_name[0]} {player_2_name[1]}\n")
                else:
                    output += '{0:30} {1}'.format(f"-{player_2_name[0]} {player_2_name[1]}",f"{player_1_name[0]} {player_1_name[1]}\n")
    if output == "":
        output = "No matches found\n"
    return output[:-1]
def main():
    sum_goal = int(sys.argv[1])
    player_list = download_json()
    print(search_heights(sum_goal, player_list))

if __name__ == "__main__":
    main()
