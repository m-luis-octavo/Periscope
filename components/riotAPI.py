# Python wrapper of the Riot API
import cassiopeia as cass

# API Key, resets daily
cass.set_riot_api_key("RGAPI-e0d91437-cc22-4611-a028-5d8962eaf8f6")

def printSummoner():
    account = cass.get_account(name="Destly", tagline="NA1", region="NA")
    summoner = account.summoner
    print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return


# RIOT API Results Guide
# [n] implies it is a list within a list

# [0] = Summoner name with tagline
# [1] = Summoner Level
# [2] = Summoner Profile Icon URL
# [3][n] = Top 3 Mastery (Name)
# [4][n] = Top 3 Mastery (Value)

# Primitive
# 1 API Call
def printSummonerV2(nameInputNonSplit):
    print("Print Summoner Called".center(100, "-"))
    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner

    # Load statistics
    #print(summoner.level)
    good_with = summoner.champion_masteries
    # Champion mastery variables
    # cm.points
    # cm.champion.name
    # cm.level
    #print([cm.points for cm in good_with])
    #summoner.match_history

    # Gather top 3 mastery data
    masteryTop3Names = ([cm.champion.name for cm in good_with[:3]])
    masteryTop3Points = ([cm.points for cm in good_with[:3]])
    masteryTop3Points = [f"{num:,}" for num in masteryTop3Points]

    #print(masteryTop3Names)
    #print(masteryTop3Points)

    # Appending all the data to be sent back
    SummonerInfo = []
    SummonerInfo.append(account.name_with_tagline)
    SummonerInfo.append(summoner.level)
    SummonerInfo.append(summoner.profile_icon.url)
    SummonerInfo.append(masteryTop3Names)
    SummonerInfo.append(masteryTop3Points)

    #print(summoner.profile_icon.url)
    #print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return SummonerInfo

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# RIOT API Results Guide
# [n] implies it is a list within a list

# [0][n] = Blue Players
# [1][n] = Blue Champions
# [2][n] = Red Players
# [3][n] = Red Champions
# [4][n] = Player Statistics
# [5] = Blue / Red Victory

# Match History (variable match length)
# 4 API Calls / match
numMatches = 2

def printMatch(nameInputNonSplit):
    print("Print Match Called".center(100, "-"))
    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner

    match_history = summoner.match_history
    match = match_history[0]
    #pprint(vars(match))
    #print("Match ID:", match.id)

    print("Blue team won?", match.blue_team.win)
    print("Red team won?", match.red_team.win)

    # All available data points, for the purpose of our app, we will only need a few of these
    '''
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
    '''

    #print("Participants on blue team:")
    # Blue team players and champion fetch
    BlueTeamPlayers = [p.summoner_name for p in match.blue_team.participants]
    BlueTeamChampions = [p.champion.name for p in match.blue_team.participants]
    print(BlueTeamPlayers)

    #print("Participants on red team:")
    # Red team players and champion fetch
    RedTeamPlayers = [p.summoner_name for p in match.red_team.participants]
    RedTeamChampions = [p.champion.name for p in match.red_team.participants]
    print(RedTeamPlayers)

    PlayerStats = []
    PlayerGameOutcome = ''
    # Search for our specific summoner and log its statistics
    if (nameInput in BlueTeamPlayers):
        print("Destly was here on Blue")
        # log statistics
        for p in match.blue_team.participants:
            #print(p.summoner_name)
            if p.summoner_name == nameInput:
                PlayerStats.append(p.summoner_name)
                PlayerStats.append(p.champion.name)
                PlayerStats.append(p.runes.keystone.name)
                PlayerStats.append(p.stats.kills)
                PlayerStats.append(p.stats.deaths)
                PlayerStats.append(p.stats.assists)
                PlayerStats.append(round(p.stats.kda, 2))

                if (match.blue_team.win == True):
                    PlayerGameOutcome = 'Victory'
                else:
                    PlayerGameOutcome = 'Defeat'
            
    if (nameInput in RedTeamPlayers):
        # log statistics
        for p in match.blue_team.participants:
            #print(p.summoner_name)
            if p.summoner_name == nameInput:
                PlayerStats.append(p.summoner_name)
                PlayerStats.append(p.champion.name)
                PlayerStats.append(p.runes.keystone.name)
                PlayerStats.append(p.stats.kills)
                PlayerStats.append(p.stats.deaths)
                PlayerStats.append(p.stats.assists)
                PlayerStats.append(round(p.stats.kda, 2))

                if (match.red_team.win == True):
                    PlayerGameOutcome = 'Victory'
                else:
                    PlayerGameOutcome = 'Defeat'

    print(PlayerStats)

    # Appending all information
    MatchInfo = []
    MatchInfo.append(BlueTeamPlayers)
    MatchInfo.append(BlueTeamChampions)
    MatchInfo.append(RedTeamPlayers)
    MatchInfo.append(RedTeamChampions)
    MatchInfo.append(PlayerStats)
    MatchInfo.append(PlayerGameOutcome)
    #print(BlueTeamPlayers)
    

    return MatchInfo

def printPlayerRank(nameInputNonSplit):
    print("Print Rank Called".center(100, "-"))
    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner

    #entries = summoner.league_entries

    entries = cass.get_league_entries(summoner=summoner)
    RankInfo = []
    for entry in entries:
        RankInfo.append(str(entry.tier))
        RankInfo.append(str(entry.division))
    #print(PlayerRanks)
    return RankInfo

