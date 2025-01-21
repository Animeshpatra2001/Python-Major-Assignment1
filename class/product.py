{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7a7d3fc6-18fc-4d9e-8897-4d54cb01717e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product: 120\n"
     ]
    }
   ],
   "source": [
    "list = [1, 2, 3, 4, 5]\n",
    "def prod_of_nums(*list):\n",
    "    prod=1\n",
    "    for i in list:\n",
    "        prod *= i\n",
    "    return prod\n",
    "print(f\"Product: {prod_of_nums(1, 2, 3, 4, 5)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30894b34-b920-4588-addd-74ecfd9e08eb",
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
