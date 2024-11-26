# Python wrapper of the Riot API
import cassiopeia as cass

# API Key, resets daily
cass.set_riot_api_key("RGAPI-f26574d4-6650-4e4f-be8f-979ca47d57d0")

def printSummoner():
    account = cass.get_account(name="Destly", tagline="NA1", region="NA")
    summoner = account.summoner
    print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return

# Primitive
def printSummonerV2(nameInputNonSplit):
    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner

    # Load statistics
    print(summoner.level)
    good_with = summoner.champion_masteries
    # Champion mastery variables
    # cm.points
    # cm.champion.name
    # cm.level
    print([cm.points for cm in good_with])
    #summoner.match_history

    print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return account.name_with_tagline

# Selective API Calls