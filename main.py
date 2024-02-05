import json

with open('ethereum.json', 'r') as file:
    data = json.load(file)

polygon_data = {
    "official_links": data["official_links"],
    "social_platforms": data["social_platforms"],
    "data_aggregator": data["data_aggregator"],
    "explorers": data["explorers"],
    "bridges": data["bridges"],
    "bounty": data["bounty"],
    "grants": data["grants"],
    "faucets": data["faucets"],
    "rpcs": data["rpcs"],
    "wallets": data["wallets"],
    "oracles": data["oracles"]
}

file_name = 'polygon.json'

with open(file_name, 'w') as file:
    json.dump(polygon_data, file, indent=4)

