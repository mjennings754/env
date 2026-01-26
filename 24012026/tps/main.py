"""
Travel Planner System - Make a system that allows users to put together their own little travel itinerary and keep track of the airline / hotel arrangements, points of interest, budget and schedule.
"""
destination = input("Where are you traveling to? ")
flight_date = input("When are you flying out? ")
airline = input("What airline are you flying with? ")
budget = int(input("What is your budget? "))
itinerary = []
itinerary_input = input("What are your plans? ")
itinerary.append(itinerary_input.split(','))
print(f'{destination} | {flight_date} | {airline} | {budget}')
print(itinerary)

