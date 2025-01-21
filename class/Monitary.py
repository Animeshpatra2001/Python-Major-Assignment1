{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "74590da8-ab80-45d6-b61a-fadb619d9d23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1050.00\n",
      "2 1102.5000\n",
      "3 1157.625000\n",
      "4 1215.50625000\n",
      "5 1276.2815625000\n",
      "6 1340.095640625000\n",
      "7 1407.10042265625000\n",
      "8 1477.4554437890625000\n",
      "9 1551.328215978515625000\n",
      "10 1628.89462677744140625000\n"
     ]
    }
   ],
   "source": [
    "from decimal import Decimal as d \n",
    "p = d('1000')\n",
    "r = d('0.05')\n",
    "for x in range (1,11):\n",
    "    a = p*(1+r)**x\n",
    "    print(x,a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53273b1d-3210-4e20-99de-36e6246f39d1",
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
