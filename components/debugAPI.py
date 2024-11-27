# Debug API Calls
import cassiopeia as cass
from cassiopeia import Champion, Champions, Account
from cassiopeia.data import Queue
from collections import Counter

# API Key, resets daily
cass.set_riot_api_key("RGAPI-3cff7a4c-f72e-46cf-bb93-e464a6d35d9f")

def get_champions():
    champions = Champions(region="NA")
    for champion in champions:
        print(champion.name, champion.id)
    print()

    annie = Champion(name="Annie", region="NA")
    print(annie.name)
    print(annie.title)
    for spell in annie.spells:
        print(spell.name, spell.keywords)

    print(annie.info.difficulty)
    print(annie.passive.name)

def get_participant_data(participants):
    team_participant_data = []
    for p in participants:
        p_data = {
            "summoner": p.summoner_name,
            "champion": p.champion.name,
            "runes": p.runes.keystone.name,
            "d_spell": p.summoner_spell_d.name,
            "f_spell": p.summoner_spell_f.name,
            "kills": p.stats.kills,
            "assist": p.stats.assists,
            "deaths": p.stats.deaths,
            "kda_ratio": round(p.stats.kda, 2),
            "damage_dealt": p.stats.total_damage_dealt,
            "creep_score": p.stats.total_minions_killed,
            "vision_score": p.stats.vision_score,
        }

        p_items = []
        number_of_item_slots = 6
        for i in range(number_of_item_slots):
            try:
                p_items.append(p.stats.items[i].name)
            except AttributeError:
                p_items.append("None")
        p_data["items"] = p_items
        team_participant_data.append(p_data)
    return team_participant_data


def print_match_history(summoner, num_matches):
    for i, match in enumerate(summoner.match_history[0:num_matches], start=1):
        match_num = f"MATCH {i}"
        print(match_num.center(100, "#"))

        blue_team = match.blue_team.participants
        print("BLUE SIDE".center(100, "-"))
        for p_data in get_participant_data(blue_team):
            print(p_data)

        red_team = match.red_team.participants
        print("RED SIDE".center(100, "-"))
        for p_data in get_participant_data(red_team):
            print(p_data)


def main():
    name = "Destly"
    tagline = "NA1"
    region = "NA"
    account = Account(name=name, tagline=tagline, region=region)
    summoner = account.summoner
    print_match_history(summoner, 2)

def print_newest_match(name: str, tagline: str, region: str):

    # Notice how this function never makes a call to the summoner endpoint because we provide all the needed data!

    account = Account(name=name, tagline=tagline, region=region)
    summoner = account.summoner

    # A MatchHistory is a lazy list, meaning it's elements only get loaded as-needed.

    match_history = cass.get_match_history(
        continent=summoner.region.continent,
        puuid=summoner.puuid,
        queue=Queue.ranked_solo_fives,
    )
    # match_history = summoner.match_history

    match = match_history[0]
    print("Match ID:", match.id)
    

    print("\nNow pull the full match data by iterating over all the participants:")
    for p in match.participants:
        print(f"{p.summoner_name} with ID {p.summoner.id} played {p.champion.name}")
    print()
    print("Iterate over all the participants again and note the data is not repulled:")
    for p in match.participants:
        print(f"{p.summoner_name} with ID {p.summoner.id} played {p.champion.name}")
    print()

    print("Blue team won?", match.blue_team.win)
    print("Red team won?", match.red_team.win)
    print()

    print("Participants on blue team:")
    for p in match.blue_team.participants:
        print(f"{p.summoner_name}: {p.champion.name}")
    print()

    print("Keystone and stat runes for each player:")
    for p in match.participants:
        print(f"{p.champion.name}: {p.runes.keystone.name}, ({', '.join([r.name for r in p.stat_runes])})")


if __name__ == "__main__":
    #get_champions()
    #main()
    print_newest_match(name="Destly", tagline="NA1", region="NA")