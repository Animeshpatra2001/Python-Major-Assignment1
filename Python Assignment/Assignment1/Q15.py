'''
15. Assume you start investing in Mutual Funds with Rs. 1000 and plan to leave your money invested.
Calculate and display how much money you will have after 10, 20 and 30 years. Use the following
formula for determining these amounts:
a = p(1 + r)^n
where p (principal) = Rs. 1000,
r (annual rate of return) = 12
n (number of years) = 10, 20, 30,
a (amount on deposit at the end of the nth year).
Disclaimer: Investing in Mutual Funds is subject to Market Risks. Do your due diligence before investing.
'''

p = 1000
n1 = 10 
n2 = 20
n3 = 30
r = 12

a1 = p * (1 + r)**n1
a2 = p * (1 + r)**n2
a3 = p * (1 + r)**n3

print(f"After 10 years deposit: {a1}\nAfter 20 years deposit: {a2}\nAfter 30 years deposit: {a3}")

'''
Output
After 10 years deposit: 137858491849000
After 20 years deposit: 19004963774880799438801000
After 30 years deposit: 2619995643649944960380551432833049000
'''