{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e32a00e2-b63b-47bb-b56f-c7b3a9e9a601",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number:  1213\n",
      "Enter the second number:  3456\n",
      "Enter the third number:  6785\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The numbers in ascending order are: 1213.0, 3456.0, 6785.0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def sort_and_display_numbers():\n",
    "    \n",
    "    num1 = float(input(\"Enter the first number: \"))\n",
    "    num2 = float(input(\"Enter the second number: \"))\n",
    "    num3 = float(input(\"Enter the third number: \"))\n",
    "    if num1 <= num2 and num1 <= num3:\n",
    "        smallest = num1\n",
    "        if num2 <= num3:\n",
    "            middle = num2\n",
    "            largest = num3\n",
    "        else:\n",
    "            middle = num3\n",
    "            largest = num2\n",
    "    elif num2 <= num1 and num2 <= num3:\n",
    "        smallest = num2\n",
    "        if num1 <= num3:\n",
    "            middle = num1\n",
    "            largest = num3\n",
    "        else:\n",
    "            middle = num3\n",
    "            largest = num1\n",
    "    else:\n",
    "        smallest = num3\n",
    "        if num1 <= num2:\n",
    "            middle = num1\n",
    "            largest = num2\n",
    "        else:\n",
    "            middle = num2\n",
    "            largest = num1\n",
    "    print(f\"The numbers in ascending order are: {smallest}, {middle}, {largest}\")\n",
    "\n",
    "sort_and_display_numbers()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4d1eade1-a7b9-432c-973e-0edbdb9a9b76",
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
