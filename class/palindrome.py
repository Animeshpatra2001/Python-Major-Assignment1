{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8c89a380-943a-4bea-98ae-88fb51d994c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a num:  12321\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Palindrome\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Enter a num: \"))\n",
    "y = x\n",
    "r =0\n",
    "while x>0:\n",
    "    rev = x%10\n",
    "    r = (r*10) + rev\n",
    "    x //= 10\n",
    "if r == y:\n",
    "    print(\"Palindrome\")\n",
    "else:\n",
    "    print(\"Not Palindrome\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa587869-4d9b-4e4b-a17c-0700600794c9",
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
