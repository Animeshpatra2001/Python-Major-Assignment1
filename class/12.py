{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "93de3bbd-0747-4423-a606-73cffc127d2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the result of 1th student(1==pass, 2==fail) 1\n",
      "Enter the result of 2th student(1==pass, 2==fail) 2\n",
      "Enter the result of 3th student(1==pass, 2==fail) 3\n",
      "Enter the result of 4th student(1==pass, 2==fail) 4\n",
      "Enter the result of 5th student(1==pass, 2==fail) 5\n",
      "Enter the result of 6th student(1==pass, 2==fail) 6\n",
      "Enter the result of 7th student(1==pass, 2==fail) 7\n",
      "Enter the result of 8th student(1==pass, 2==fail) 8\n",
      "Enter the result of 9th student(1==pass, 2==fail) 9\n",
      "Enter the result of 10th student(1==pass, 2==fail) 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Only 1 student have passed the exam!\n"
     ]
    }
   ],
   "source": [
    "passes = 0\n",
    "failures = 0\n",
    "for s in range(10):\n",
    "    result = int(input(f\"Enter the result of {s+1}th student(1==pass, 2==fail)\"))\n",
    "    if result == 1:\n",
    "        passes+=1\n",
    "    elif result== 2:\n",
    "        failures+=1\n",
    "if passes>8:\n",
    "    print (\"Bonus available for instructor\")\n",
    "else:\n",
    "    print  (f\"Only {passes} student have passed the exam!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef798967-ad68-43e2-ae91-2e4eccce28b1",
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
