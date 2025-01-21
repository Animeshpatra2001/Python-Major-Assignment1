{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b04e82-4805-42f3-8c41-3c0e42d80962",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the 'Guess the Number' game!\n",
      "\n",
      "Guess my number between 1 and 1000:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  589\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  900\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  800\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  750\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  700\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  650\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too high. Try again.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your guess:  600\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Too low. Try again.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def guess_the_number():\n",
    "    print(\"Welcome to the 'Guess the Number' game!\")\n",
    "    \n",
    "    while True:\n",
    "        number_to_guess = random.randint(1, 1000)\n",
    "        guess = None\n",
    "        attempts = 0\n",
    "        \n",
    "        print(\"\\nGuess my number between 1 and 1000:\")\n",
    "        \n",
    "        while guess != number_to_guess:\n",
    "            try:\n",
    "                guess = int(input(\"Enter your guess: \"))\n",
    "                attempts += 1\n",
    "                \n",
    "                if guess < number_to_guess:\n",
    "                    print(\"Too low. Try again.\")\n",
    "                elif guess > number_to_guess:\n",
    "                    print(\"Too high. Try again.\")\n",
    "                else:\n",
    "                    print(f\"Congratulations! You guessed the number in {attempts} attempts!\")\n",
    "            except ValueError:\n",
    "                print(\"Please enter a valid integer.\")\n",
    "\n",
    "        play_again = input(\"Do you want to play again? (yes/no): \").lower()\n",
    "        if play_again != 'yes':\n",
    "            print(\"Thank you for playing! Goodbye.\")\n",
    "            break\n",
    "\n",
    "# Run the game\n",
    "guess_the_number()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2dd8e7aa-dd5f-4e7f-9a34-3d34c326eeee",
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
