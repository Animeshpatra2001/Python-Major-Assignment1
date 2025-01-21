{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d7a2a3c7-c56a-408f-82ea-d11d545d81f4",
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
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "n = int (input(\"Enter a five digit number: \"))\n",
    "digits = []\n",
    "for _ in range(5):\n",
    "    digit = n % 10\n",
    "    digits.append(digit)\n",
    "    n //= 10\n",
    "        \n",
    "digits.reverse()\n",
    "print(digits) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47a1a433-0ace-4012-8591-497f36845923",
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
