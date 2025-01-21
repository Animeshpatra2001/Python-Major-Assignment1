{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4b698f6f-5de6-4a34-a997-9d0c271a0163",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a num:  10\n",
      "Enter a num:  12\n",
      "Enter a num:  13\n",
      "Enter a num:  1\n",
      "Enter a num:  34\n",
      "Enter a num:  23\n",
      "Enter a num:  412\n",
      "Enter a num:  323\n",
      "Enter a num:  2\n",
      "Enter a num:  3334\n",
      "Enter a num:  12\n",
      "Enter a num:  22\n",
      "Enter a num:  33\n",
      "Enter a num:  2\n",
      "Enter a num:  3\n",
      "Enter a num:  33\n",
      "Enter a num:  23\n",
      "Enter a num:  3\n",
      "Enter a num:  4\n",
      "Enter a num:  2\n",
      "Enter a num:  3\n",
      "Enter a num:  \n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 5\u001b[0m\n\u001b[1;32m      2\u001b[0m count, largest, second_largest \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m-\u001b[39mm\u001b[38;5;241m.\u001b[39minf, m\u001b[38;5;241m.\u001b[39minf\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m count \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m10\u001b[39m:\n\u001b[0;32m----> 5\u001b[0m \tx \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter a num: \u001b[39m\u001b[38;5;124m\"\u001b[39m))\n\u001b[1;32m      7\u001b[0m \t\u001b[38;5;28;01mif\u001b[39;00m x \u001b[38;5;241m>\u001b[39m largest:\n\u001b[1;32m      8\u001b[0m \t\tlargest \u001b[38;5;241m=\u001b[39m x;\n",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "import math as m \n",
    "count, largest, second_largest = 0, -m.inf, m.inf\n",
    "\n",
    "while count < 10:\n",
    "\tx = int(input(\"Enter a num: \"))\n",
    "\t\n",
    "\tif x > largest:\n",
    "\t\tlargest = x;\n",
    "\telif x < largest and x > second_largest:\n",
    "\t\tsecond_largest = x\n",
    "\t\n",
    "print(f\"Largest: {largest}, Second Largest: {second_largest}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50321e8f-7d83-49bc-a832-8790de67abcd",
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
