{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a8f9f8c0-4af3-4021-8369-93270ec2f67f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pythagorean triples with sides no larger than 20:\n",
      "(3, 4, 5)\n",
      "(5, 12, 13)\n",
      "(6, 8, 10)\n",
      "(8, 15, 17)\n",
      "(9, 12, 15)\n",
      "(12, 16, 20)\n"
     ]
    }
   ],
   "source": [
    "def find_pythagorean_triples(max_side):\n",
    "    triples = []\n",
    "    for a in range(1, 21):\n",
    "        for b in range(a, 21):  \n",
    "            for c in range(b, 21):  \n",
    "                if a**2 + b**2 == c**2:\n",
    "                    triples.append((a, b, c))\n",
    "    return triples\n",
    "pythagorean_triples = find_pythagorean_triples(max_side_length)\n",
    "print(\"Pythagorean triples with sides no larger than 20:\")\n",
    "for triple in pythagorean_triples:\n",
    "    print(triple)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e03df89d-9900-48fb-b2fa-7f13d7676a05",
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
