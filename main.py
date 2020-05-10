import json

from Agent import Agent
from Position import Position
from Zone import Zone
from BaseGraph import BaseGraph
from AgreeablenessGraph import AgreeablenessGraph

########################## Main ###########################
def main():
    # liste agent: http://pplapi.com/
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        zone = Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
    agreeableness_graph = AgreeablenessGraph()
    agreeableness_graph.show(Zone.ZONES)

main()