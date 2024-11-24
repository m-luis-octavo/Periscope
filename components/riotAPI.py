# Python wrapper of the Riot API
import cassiopeia as cass

# API Key, resets daily
cass.set_riot_api_key("RGAPI-25fe1569-5421-475c-889a-5776a2aa728e")

def printSummoner():
    account = cass.get_account(name="Destly", tagline="NA1", region="NA")
    summoner = account.summoner
    print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return

def printSummonerV2(nameInputNonSplit):
    # Separate the player name and tagline
    nameInput, taglineInput = nameInputNonSplit.split("#")

    account = cass.get_account(name=nameInput, tagline=taglineInput, region="NA")
    summoner = account.summoner
    print("{name} is a level {level} summoner on the {region} server.".format(name=account.name_with_tagline, level=summoner.level, region=summoner.region))
    return