{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16155990-fc2a-4342-be4b-4bfad5d810ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randrange as rr\n",
    "def roll_dice():\n",
    "    die1 = rr(1,7)\n",
    "    die2 = rr(1,7)\n",
    "    return die1,die2\n",
    "def display_roll(dice):\n",
    "    die1,die2 =dice\n",
    "    print(f\"player has rolled {die1} + {die2} = {die1 + die2}\")\n",
    "    sum_of_outcomes = sum(roll_dice())\n",
    "    "
   ]
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
