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
# [4] = Blue / Red Victory

# Match History (variable match length)
# 4 API Calls / match
numMatches = 2

def printMatch(nameInputNonSplit):

    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner

    match_history = summoner.match_history
    match = match_history[0]
    print("Match ID:", match.id)

    print("Blue team won?", match.blue_team.win)
    print("Red team won?", match.red_team.win)
    print()

    print("Participants on blue team:")
    BlueTeamPlayers = [p.summoner_name for p in match.blue_team.participants]
    BlueTeamChampions = [p.champion.name for p in match.blue_team.participants]
    for p in match.blue_team.participants:
        print(f"{p.summoner_name}: {p.champion.name}")
    print()

    print("Participants on red team:")
    RedTeamPlayers = [p.summoner_name for p in match.red_team.participants]
    RedTeamChampions = [p.champion.name for p in match.red_team.participants]
    
    #for p in match.red_team.participants:
    #    print(f"{p.summoner_name}: {p.champion.name}")
    #print()

    print("Keystone and stat runes for each player:")
    for p in match.participants:
        print(f"{p.champion.name}: {p.runes.keystone.name}, ({', '.join([r.name for r in p.stat_runes])})")

    # Appending all information
    MatchInfo = []
    MatchInfo.append(BlueTeamPlayers)
    MatchInfo.append(BlueTeamChampions)
    MatchInfo.append(RedTeamPlayers)
    MatchInfo.append(RedTeamChampions)
    print(BlueTeamPlayers)
    

    return MatchInfo


# Selective API Calls
def printNewestMatch():
    ...

def printPlayerRank(nameInputNonSplit):
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