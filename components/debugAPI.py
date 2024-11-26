# Debug API Calls
import cassiopeia as cass
from cassiopeia import Champion, Champions

# API Key, resets daily
cass.set_riot_api_key("RGAPI-f26574d4-6650-4e4f-be8f-979ca47d57d0")

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

if __name__ == "__main__":
    get_champions()