'''14. Write a Python program that calculates the final cost of a hotel booking based on the room type
(Standard: $100/night, Deluxe: $150/night, Suite: $250/night), the length of stay (10% discount for
>3 nights, 20% discount for >7 nights), the season (20% increase during peak season, 15% decrease
during the off-season), and whether the customer is a loyalty member (5% additional discount). The
program should output the final booking cost after applying all relevant discounts and adjustments.'''

room_type = input("Enter room type('Standard' or 'Deluxe' or 'Suite'): ")
duration_of_stay = int(input("Enter no. of nights: "))
season = input("Enter the season('Winter' or 'Other'): ")
is_loyalty_member = input("Are you a loyalty member('Y' or 'N'): ")

room_cost = 0
match room_type.lower():
    case 'standard':
        room_cost = 100
    case 'deluxe':
        room_cost = 150
    case 'suite':
        room_cost = 250
    case _:
        print("Invalid room type")
        exit()

duration_discount = 0
if duration_of_stay > 7:
    duration_discount = room_cost * 0.20
elif duration_of_stay > 3:
    duration_discount = room_cost * 0.10

season_discount = 0
if season.lower() == 'winter':
    season_discount = -room_cost * 0.20
else :
    season_discount = room_cost * 0.15

loyalty_member_discount = 0
if is_loyalty_member.lower() == 'y':
    loyalty_member_discount = room_cost * 0.05

final_cost = room_cost - duration_discount - season_discount - loyalty_member_discount
print(f"The final booking will cost you ${final_cost} only.")

'''
Output
Enter room type('Standard' or 'Deluxe' or 'Suite'): suite
Enter no. of nights: 3
Enter the season('Winter' or 'Other'): winter
Are you a loyalty member('Y' or 'N'): y
The final booking will cost you $287.5 only.
'''