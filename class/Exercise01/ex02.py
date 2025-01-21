{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "572003d1-e994-4358-8c9d-6ac57f3269c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number:  1\n",
      "Enter the second number:  2\n",
      "Enter the third number:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum=  6.0 , Product=  6.0 , Avarage=  2.0 , Minimum=  1.0 , Minimum=  3.0\n"
     ]
    }
   ],
   "source": [
    "n1 = float(input(\"Enter the first number: \"))\n",
    "n2 = float(input(\"Enter the second number: \"))\n",
    "n3 = float(input(\"Enter the third number: \"))\n",
    "\n",
    "sum = n1+n2+n3\n",
    "product = n1*n2*n3\n",
    "avg = sum/3\n",
    "\n",
    "print(\"Sum= \" , sum ,\", Product= \" , product ,\", Avarage= \" , avg ,\", Minimum= \" , min(n1,n2,n3) ,\", Minimum= \" , max(n1,n2,n3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0ba49be-6b87-46ea-b227-0b220ab4370d",
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
