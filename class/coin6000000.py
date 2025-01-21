{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "faeaee58-32d7-4e0a-a42d-db43ffa1242b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The frequency of ls is =999885\n",
      "The frequency of ls is =1000308\n",
      "The frequency of ls is =999586\n",
      "The frequency of ls is =999820\n",
      "The frequency of ls is =999984\n",
      "The frequency of ls is =1000417\n"
     ]
    }
   ],
   "source": [
    "from random import randrange as rr\n",
    "f_1, f_2, f_3, f_4, f_5, f_6 = 0,0,0,0,0,0\n",
    "for t in range(6000000):\n",
    "    outcome = rr(1,7)\n",
    "    if outcome== 1:\n",
    "        f_1+=1\n",
    "    elif outcome== 2:\n",
    "        f_2+=1\n",
    "    elif outcome== 3:\n",
    "        f_3+=1\n",
    "    elif outcome== 4:\n",
    "        f_4+=1\n",
    "    elif outcome== 5:\n",
    "        f_5+=1\n",
    "    else: \n",
    "        f_6+=1\n",
    "print(f\"The frequency of ls is ={f_1}\")\n",
    "print(f\"The frequency of ls is ={f_2}\")\n",
    "print(f\"The frequency of ls is ={f_3}\")\n",
    "print(f\"The frequency of ls is ={f_4}\")\n",
    "print(f\"The frequency of ls is ={f_5}\")\n",
    "print(f\"The frequency of ls is ={f_6}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3741f75-fece-4631-9d0e-9bcaae40624a",
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
