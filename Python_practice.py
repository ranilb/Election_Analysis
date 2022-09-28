



from atexit import register


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dicts in voting_data:
     print(f"{county_dicts['county']} county has  {county_dicts['registered_voters']:,} registered votes.") 