{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a55e53e8-274e-4e1a-83ea-a80f2b95c2e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter an integer containing 1s and 0s 1011\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Decimal: 11\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"enter an integer containing 1s and 0s\"))\n",
    "dn = 0 \n",
    "p = 0 \n",
    "while n > 0:\n",
    "    bit = n%10 #to extract right most bit\n",
    "    dn = dn+bit*2**p\n",
    "    p+=1\n",
    "    n = n//10 #to extract th rightmost digit from binary\n",
    "print(f\"Decimal: {dn}\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fbe0f578-d78f-4c8f-9abf-c8c8a0d1a1e4",
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
