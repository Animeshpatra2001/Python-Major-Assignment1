{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "11716be1-a9d0-4a8a-9168-f67d82c77a80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a five digit number:  12345\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 "
     ]
    }
   ],
   "source": [
    "n = int (input(\"Enter a five digit number: \"))#12345\n",
    "d= 10000\n",
    "while d>0:\n",
    "    digit = n//d\n",
    "    n = n%d\n",
    "    d = d//10\n",
    "    print(digit,end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5280ac04-1de4-498a-8f93-0d63a1887edc",
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
