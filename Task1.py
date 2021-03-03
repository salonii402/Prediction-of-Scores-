{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# GRIP - The Sparks Foundation\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NAME : SALONI JAIN"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# DATA SCIENCE AND BUSINESS ANALYTICS INTERN\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "TASK 1 : Predict the percentage of an student based on the no. of study hours."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The task is to predict score if a student studies for 9.25 hrs/ day. It is implemented using simple linear regression model. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Import librarires"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Import the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://bit.ly/w-data\"\n",
    "data = pd.read_csv(url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Overview"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30\n",
       "5    1.5      20\n",
       "6    9.2      88\n",
       "7    5.5      60\n",
       "8    8.3      81\n",
       "9    2.7      25"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>25.000000</td>\n",
       "      <td>25.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5.012000</td>\n",
       "      <td>51.480000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2.525094</td>\n",
       "      <td>25.286887</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.100000</td>\n",
       "      <td>17.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.700000</td>\n",
       "      <td>30.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.800000</td>\n",
       "      <td>47.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7.400000</td>\n",
       "      <td>75.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.200000</td>\n",
       "      <td>95.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Hours     Scores\n",
       "count  25.000000  25.000000\n",
       "mean    5.012000  51.480000\n",
       "std     2.525094  25.286887\n",
       "min     1.100000  17.000000\n",
       "25%     2.700000  30.000000\n",
       "50%     4.800000  47.000000\n",
       "75%     7.400000  75.000000\n",
       "max     9.200000  95.000000"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Check if there is any null data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Hours     0\n",
       "Scores    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Plot the data in a 2D graph and check if there is any relationship between hours studied and marks scored."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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rMq1tsJ++8Hrr6952yLVbOIHnPRL+Lswq37/9E/w4INw0UWVjaOmE7+ZWS3o3x8kuOoq+PDDbCpl6yvBiX8tXXzxxWy//fbstNNOjBkzhkceeaTSIZlZlXnxRTj2WBiQxjobMACOOw5eeqky8dRs425PtLbCuHEweTJs0tGgft300EMPcffddzNr1izWWWcd3njjDd5///0eH2/16tX07dtQ/yRmDWHYMBg4EFauhKambDpwYO/koZ5oqBJ/b9evtba2MnjwYNZZJxscafDgwXz+85/nscceY++992b06NHsvvvuLF26lJUrV3LSSSex4447svPOO/OHP/wBgOuvv56jjz6aww47jIMPPph3332Xb3zjG+y2227svPPO3HnnnQA888wz7L777owZM4addtqJuXPn9s6HMLOyWLAATj0VHn44m1a0gTciqv616667RnvPPvvsp9Z1pqkpAj79amrKfYgOLV26NEaPHh0jR46M0047LWbMmBHvvfdebLnllvHoo49GRMTbb78dq1atissuuyxOPPHEiIiYM2dObL755rFixYq47rrrYtNNN43FixdHRMQPf/jDuOGGGyIiYsmSJTFy5MhYtmxZfOc734lJkyZFRMR7770Xy5cv/1Q83flOzKz+AS3RQU5tiBJ/UfVr6623HjNnzmTChAkMGTKEY445hquvvpphw4ax2267ATBw4ED69u3Lgw8+yPHHHw/AF77wBbbYYgteeOEFAA466CAGDRoEwNSpU7nkkksYM2YMY8eOZeXKlcybN4+99tqLn/70p1x66aW88sor9K9Uq5CZ1byGqFAusn6tT58+jB07lrFjx7LjjjtyxRVXdHhrZXQx4M266677ie1uvfVWtt32k+N0jxo1ij322IN77rmHQw45hGuuuYb9999/7T+AmTWchijxQzH1a88///wn6tpnz57NqFGjeO2113jssccAWLp0KatXr2bfffflxhtvBOCFF15g3rx5n0ruAIcccgi/+MUvPvqhePzxbBS8F198ka222oozzzyTww8/nCeffHLtP4CZNaSGKPED3Hbbx/NXXNE7x1y2bBlnnHEGb731Fn379mWbbbZhwoQJnHTSSZxxxhmsWLGC/v37c99993H66adz6qmnsuOOO9K3b1+uv/76jxqFS/34xz/m7LPPZqeddiIiGDFiBHfffTeTJ09m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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.plot(x='Hours',y='Scores',style='*',color='blue')\n",
    "plt.title('Hours vs Percentage')\n",
    "plt.xlabel('Hours Studied')\n",
    "plt.ylabel('Percentage Scored')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The graph shows a linear relationship between the hours studied and percentage scored. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Divide the data into attributes(inputs) and labels(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data.iloc[:,:-1].values\n",
    "y = data.iloc[:,1].values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Next Step is to further divide the data into test and train data using train_test_split() method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  Next step is to train our model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "training Completed\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "r = LinearRegression()\n",
    "r.fit(X_train,y_train)\n",
    "print('training Completed')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "line = r.coef_ * X+r.intercept_\n",
    "plt.title('linear regression vs trained model')\n",
    "plt.scatter(X,y,color='blue')\n",
    "plt.xlabel('Hours Studied')\n",
    "plt.ylabel('Scored pecentages')\n",
    "plt.plot(X,line)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1.5]\n",
      " [3.2]\n",
      " [7.4]\n",
      " [2.5]\n",
      " [5.9]]\n"
     ]
    }
   ],
   "source": [
    "print(X_test)\n",
    "y_pred = r.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Predicted</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.884145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.732261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.357018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.794801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.491033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual  Predicted\n",
       "0      20  16.884145\n",
       "1      27  33.732261\n",
       "2      69  75.357018\n",
       "3      30  26.794801\n",
       "4      62  60.491033"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({'Actual':y_test,'Predicted':y_pred})\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Score:  0.9515510725211553\n",
      "Testing Score:  0.9454906892105355\n"
     ]
    }
   ],
   "source": [
    "print(\"Training Score: \",r.score(X_train,y_train))\n",
    "print(\"Testing Score: \",r.score(X_test,y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Actual vs Predicted values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot(kind='bar',figsize=(7,7),color=('red','blue'))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No. of hours = 9.25\n",
      "Predicted Score = 96.16939660753593 \n"
     ]
    }
   ],
   "source": [
    "hours = 9.25\n",
    "test = np.array([hours])\n",
    "test = test.reshape(-1,1)\n",
    "pred = r.predict([[9.5]])\n",
    "print(\"No. of hours = {}\".format(hours))\n",
    "print(\"Predicted Score = {} \".format(pred[0]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# # Model Evaluation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error:  4.18385989900298\n",
      "Mean squared Error:  21.598769307217413\n",
      "Root mean squared Error:  4.647447612100368\n",
      "Explained variance score:  0.9482829156738146\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "print(\"Mean Absolute Error: \",metrics.mean_absolute_error(y_test,y_pred))\n",
    "print(\"Mean squared Error: \",metrics.mean_squared_error(y_test,y_pred))\n",
    "print(\"Root mean squared Error: \",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))\n",
    "print(\"Explained variance score: \",metrics.explained_variance_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Result as per our prediction, student will score - 96.16\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Accuracy - 95%(0.95)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
