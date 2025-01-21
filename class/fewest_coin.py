{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb7c4af2-7e0a-40a6-a8fa-cc9ddbae8abe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the purchase price in cents (0-100):  76\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your change is: 2 dimes, 4 pennies\n"
     ]
    }
   ],
   "source": [
    "def calculate_change(purchase_price):\n",
    "    change = 100 - purchase_price\n",
    "\n",
    "    # Define the coin values\n",
    "    quarters = change // 25\n",
    "    change %= 25\n",
    "    dimes = change // 10\n",
    "    change %= 10\n",
    "    nickels = change // 5\n",
    "    change %= 5\n",
    "    pennies = change\n",
    "\n",
    "    # Create the output message\n",
    "    result = []\n",
    "    if quarters:\n",
    "        result.append(f\"{quarters} quarter{'s' if quarters > 1 else ''}\")\n",
    "    if dimes:\n",
    "        result.append(f\"{dimes} dime{'s' if dimes > 1 else ''}\")\n",
    "    if nickels:\n",
    "        result.append(f\"{nickels} nickel{'s' if nickels > 1 else ''}\")\n",
    "    if pennies:\n",
    "        result.append(f\"{pennies} penn{'y' if pennies == 1 else 'ies'}\")\n",
    "\n",
    "    return \"Your change is: \" + ', '.join(result)\n",
    "\n",
    "# Input purchase price in cents\n",
    "purchase_price = int(input(\"Enter the purchase price in cents (0-100): \"))\n",
    "if 0 <= purchase_price <= 100:\n",
    "    print(calculate_change(purchase_price))\n",
    "else:\n",
    "    print(\"Please enter a valid price between 0 and 100 cents.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d49c4817-7660-48c2-b6c6-805669545e59",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
