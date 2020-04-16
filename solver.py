{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "toc": true
   },
   "source": [
    "<h1>Table of Contents<span class=\"tocSkip\"></span></h1>\n",
    "<div class=\"toc\"><ul class=\"toc-item\"></ul></div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:34.215535Z",
     "start_time": "2020-04-12T05:26:34.152629Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "train = pd.read_csv(\"../big_mart_sales/train.csv\")\n",
    "test = pd.read_csv(\"../big_mart_sales/test.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:35.879989Z",
     "start_time": "2020-04-12T05:26:35.834442Z"
    }
   },
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
       "      <th>Item_Identifier</th>\n",
       "      <th>Item_Weight</th>\n",
       "      <th>Item_Fat_Content</th>\n",
       "      <th>Item_Visibility</th>\n",
       "      <th>Item_Type</th>\n",
       "      <th>Item_MRP</th>\n",
       "      <th>Outlet_Identifier</th>\n",
       "      <th>Outlet_Establishment_Year</th>\n",
       "      <th>Outlet_Size</th>\n",
       "      <th>Outlet_Location_Type</th>\n",
       "      <th>Outlet_Type</th>\n",
       "      <th>Item_Outlet_Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>FDA15</td>\n",
       "      <td>9.300</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.016047</td>\n",
       "      <td>Dairy</td>\n",
       "      <td>249.8092</td>\n",
       "      <td>OUT049</td>\n",
       "      <td>1999</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Tier 1</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>3735.1380</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>DRC01</td>\n",
       "      <td>5.920</td>\n",
       "      <td>Regular</td>\n",
       "      <td>0.019278</td>\n",
       "      <td>Soft Drinks</td>\n",
       "      <td>48.2692</td>\n",
       "      <td>OUT018</td>\n",
       "      <td>2009</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Tier 3</td>\n",
       "      <td>Supermarket Type2</td>\n",
       "      <td>443.4228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>FDN15</td>\n",
       "      <td>17.500</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.016760</td>\n",
       "      <td>Meat</td>\n",
       "      <td>141.6180</td>\n",
       "      <td>OUT049</td>\n",
       "      <td>1999</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Tier 1</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>2097.2700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>FDX07</td>\n",
       "      <td>19.200</td>\n",
       "      <td>Regular</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>Fruits and Vegetables</td>\n",
       "      <td>182.0950</td>\n",
       "      <td>OUT010</td>\n",
       "      <td>1998</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tier 3</td>\n",
       "      <td>Grocery Store</td>\n",
       "      <td>732.3800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NCD19</td>\n",
       "      <td>8.930</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>Household</td>\n",
       "      <td>53.8614</td>\n",
       "      <td>OUT013</td>\n",
       "      <td>1987</td>\n",
       "      <td>High</td>\n",
       "      <td>Tier 3</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>994.7052</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8518</th>\n",
       "      <td>FDF22</td>\n",
       "      <td>6.865</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.056783</td>\n",
       "      <td>Snack Foods</td>\n",
       "      <td>214.5218</td>\n",
       "      <td>OUT013</td>\n",
       "      <td>1987</td>\n",
       "      <td>High</td>\n",
       "      <td>Tier 3</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>2778.3834</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8519</th>\n",
       "      <td>FDS36</td>\n",
       "      <td>8.380</td>\n",
       "      <td>Regular</td>\n",
       "      <td>0.046982</td>\n",
       "      <td>Baking Goods</td>\n",
       "      <td>108.1570</td>\n",
       "      <td>OUT045</td>\n",
       "      <td>2002</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tier 2</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>549.2850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8520</th>\n",
       "      <td>NCJ29</td>\n",
       "      <td>10.600</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.035186</td>\n",
       "      <td>Health and Hygiene</td>\n",
       "      <td>85.1224</td>\n",
       "      <td>OUT035</td>\n",
       "      <td>2004</td>\n",
       "      <td>Small</td>\n",
       "      <td>Tier 2</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>1193.1136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8521</th>\n",
       "      <td>FDN46</td>\n",
       "      <td>7.210</td>\n",
       "      <td>Regular</td>\n",
       "      <td>0.145221</td>\n",
       "      <td>Snack Foods</td>\n",
       "      <td>103.1332</td>\n",
       "      <td>OUT018</td>\n",
       "      <td>2009</td>\n",
       "      <td>Medium</td>\n",
       "      <td>Tier 3</td>\n",
       "      <td>Supermarket Type2</td>\n",
       "      <td>1845.5976</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8522</th>\n",
       "      <td>DRG01</td>\n",
       "      <td>14.800</td>\n",
       "      <td>Low Fat</td>\n",
       "      <td>0.044878</td>\n",
       "      <td>Soft Drinks</td>\n",
       "      <td>75.4670</td>\n",
       "      <td>OUT046</td>\n",
       "      <td>1997</td>\n",
       "      <td>Small</td>\n",
       "      <td>Tier 1</td>\n",
       "      <td>Supermarket Type1</td>\n",
       "      <td>765.6700</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8523 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Item_Identifier  Item_Weight Item_Fat_Content  Item_Visibility  \\\n",
       "0              FDA15        9.300          Low Fat         0.016047   \n",
       "1              DRC01        5.920          Regular         0.019278   \n",
       "2              FDN15       17.500          Low Fat         0.016760   \n",
       "3              FDX07       19.200          Regular         0.000000   \n",
       "4              NCD19        8.930          Low Fat         0.000000   \n",
       "...              ...          ...              ...              ...   \n",
       "8518           FDF22        6.865          Low Fat         0.056783   \n",
       "8519           FDS36        8.380          Regular         0.046982   \n",
       "8520           NCJ29       10.600          Low Fat         0.035186   \n",
       "8521           FDN46        7.210          Regular         0.145221   \n",
       "8522           DRG01       14.800          Low Fat         0.044878   \n",
       "\n",
       "                  Item_Type  Item_MRP Outlet_Identifier  \\\n",
       "0                     Dairy  249.8092            OUT049   \n",
       "1               Soft Drinks   48.2692            OUT018   \n",
       "2                      Meat  141.6180            OUT049   \n",
       "3     Fruits and Vegetables  182.0950            OUT010   \n",
       "4                 Household   53.8614            OUT013   \n",
       "...                     ...       ...               ...   \n",
       "8518            Snack Foods  214.5218            OUT013   \n",
       "8519           Baking Goods  108.1570            OUT045   \n",
       "8520     Health and Hygiene   85.1224            OUT035   \n",
       "8521            Snack Foods  103.1332            OUT018   \n",
       "8522            Soft Drinks   75.4670            OUT046   \n",
       "\n",
       "      Outlet_Establishment_Year Outlet_Size Outlet_Location_Type  \\\n",
       "0                          1999      Medium               Tier 1   \n",
       "1                          2009      Medium               Tier 3   \n",
       "2                          1999      Medium               Tier 1   \n",
       "3                          1998         NaN               Tier 3   \n",
       "4                          1987        High               Tier 3   \n",
       "...                         ...         ...                  ...   \n",
       "8518                       1987        High               Tier 3   \n",
       "8519                       2002         NaN               Tier 2   \n",
       "8520                       2004       Small               Tier 2   \n",
       "8521                       2009      Medium               Tier 3   \n",
       "8522                       1997       Small               Tier 1   \n",
       "\n",
       "            Outlet_Type  Item_Outlet_Sales  \n",
       "0     Supermarket Type1          3735.1380  \n",
       "1     Supermarket Type2           443.4228  \n",
       "2     Supermarket Type1          2097.2700  \n",
       "3         Grocery Store           732.3800  \n",
       "4     Supermarket Type1           994.7052  \n",
       "...                 ...                ...  \n",
       "8518  Supermarket Type1          2778.3834  \n",
       "8519  Supermarket Type1           549.2850  \n",
       "8520  Supermarket Type1          1193.1136  \n",
       "8521  Supermarket Type2          1845.5976  \n",
       "8522  Supermarket Type1           765.6700  \n",
       "\n",
       "[8523 rows x 12 columns]"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:36.898137Z",
     "start_time": "2020-04-12T05:26:36.881314Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 8523 entries, 0 to 8522\n",
      "Data columns (total 12 columns):\n",
      "Item_Identifier              8523 non-null object\n",
      "Item_Weight                  7060 non-null float64\n",
      "Item_Fat_Content             8523 non-null object\n",
      "Item_Visibility              8523 non-null float64\n",
      "Item_Type                    8523 non-null object\n",
      "Item_MRP                     8523 non-null float64\n",
      "Outlet_Identifier            8523 non-null object\n",
      "Outlet_Establishment_Year    8523 non-null int64\n",
      "Outlet_Size                  6113 non-null object\n",
      "Outlet_Location_Type         8523 non-null object\n",
      "Outlet_Type                  8523 non-null object\n",
      "Item_Outlet_Sales            8523 non-null float64\n",
      "dtypes: float64(4), int64(1), object(7)\n",
      "memory usage: 799.2+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:39.650875Z",
     "start_time": "2020-04-12T05:26:39.606670Z"
    }
   },
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
       "      <th>Item_Weight</th>\n",
       "      <th>Item_Visibility</th>\n",
       "      <th>Item_MRP</th>\n",
       "      <th>Outlet_Establishment_Year</th>\n",
       "      <th>Item_Outlet_Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>7060.000000</td>\n",
       "      <td>8523.000000</td>\n",
       "      <td>8523.000000</td>\n",
       "      <td>8523.000000</td>\n",
       "      <td>8523.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>12.857645</td>\n",
       "      <td>0.066132</td>\n",
       "      <td>140.992782</td>\n",
       "      <td>1997.831867</td>\n",
       "      <td>2181.288914</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.643456</td>\n",
       "      <td>0.051598</td>\n",
       "      <td>62.275067</td>\n",
       "      <td>8.371760</td>\n",
       "      <td>1706.499616</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>4.555000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.290000</td>\n",
       "      <td>1985.000000</td>\n",
       "      <td>33.290000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>8.773750</td>\n",
       "      <td>0.026989</td>\n",
       "      <td>93.826500</td>\n",
       "      <td>1987.000000</td>\n",
       "      <td>834.247400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>12.600000</td>\n",
       "      <td>0.053931</td>\n",
       "      <td>143.012800</td>\n",
       "      <td>1999.000000</td>\n",
       "      <td>1794.331000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>16.850000</td>\n",
       "      <td>0.094585</td>\n",
       "      <td>185.643700</td>\n",
       "      <td>2004.000000</td>\n",
       "      <td>3101.296400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>21.350000</td>\n",
       "      <td>0.328391</td>\n",
       "      <td>266.888400</td>\n",
       "      <td>2009.000000</td>\n",
       "      <td>13086.964800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Item_Weight  Item_Visibility     Item_MRP  Outlet_Establishment_Year  \\\n",
       "count  7060.000000      8523.000000  8523.000000                8523.000000   \n",
       "mean     12.857645         0.066132   140.992782                1997.831867   \n",
       "std       4.643456         0.051598    62.275067                   8.371760   \n",
       "min       4.555000         0.000000    31.290000                1985.000000   \n",
       "25%       8.773750         0.026989    93.826500                1987.000000   \n",
       "50%      12.600000         0.053931   143.012800                1999.000000   \n",
       "75%      16.850000         0.094585   185.643700                2004.000000   \n",
       "max      21.350000         0.328391   266.888400                2009.000000   \n",
       "\n",
       "       Item_Outlet_Sales  \n",
       "count        8523.000000  \n",
       "mean         2181.288914  \n",
       "std          1706.499616  \n",
       "min            33.290000  \n",
       "25%           834.247400  \n",
       "50%          1794.331000  \n",
       "75%          3101.296400  \n",
       "max         13086.964800  "
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:41.522071Z",
     "start_time": "2020-04-12T05:26:41.517893Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn import preprocessing \n",
    "from sklearn.metrics import mean_squared_error\n",
    "from tpot import TPOTRegressor\n",
    "from sklearn.model_selection import train_test_split \n",
    "import xgboost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:42.576414Z",
     "start_time": "2020-04-12T05:26:42.559255Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Item_Identifier                 0\n",
       "Item_Weight                  1463\n",
       "Item_Fat_Content                0\n",
       "Item_Visibility                 0\n",
       "Item_Type                       0\n",
       "Item_MRP                        0\n",
       "Outlet_Identifier               0\n",
       "Outlet_Establishment_Year       0\n",
       "Outlet_Size                  2410\n",
       "Outlet_Location_Type            0\n",
       "Outlet_Type                     0\n",
       "Item_Outlet_Sales               0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:48.444981Z",
     "start_time": "2020-04-12T05:26:48.432165Z"
    }
   },
   "outputs": [],
   "source": [
    "## preprocessing \n",
    "### mean imputations \n",
    "train['Item_Weight'].fillna((train['Item_Weight'].mean()), inplace=True)\n",
    "test['Item_Weight'].fillna((test['Item_Weight'].mean()), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:49.513849Z",
     "start_time": "2020-04-12T05:26:49.502274Z"
    }
   },
   "outputs": [],
   "source": [
    "train['Outlet_Establishment_Year'] = 2013 - train['Outlet_Establishment_Year'] \n",
    "test['Outlet_Establishment_Year'] = 2013 - test['Outlet_Establishment_Year'] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:50.511753Z",
     "start_time": "2020-04-12T05:26:50.503704Z"
    }
   },
   "outputs": [],
   "source": [
    "train['Item_Visibility'] = np.sqrt(train['Item_Visibility'])\n",
    "test['Item_Visibility'] = np.sqrt(test['Item_Visibility'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:51.671415Z",
     "start_time": "2020-04-12T05:26:51.654650Z"
    }
   },
   "outputs": [],
   "source": [
    "train.loc[train['Item_Fat_Content'].isin(['reg','Regular']), 'Item_Fat_Content'] = 'Regular'\n",
    "train.loc[train['Item_Fat_Content'].isin(['LF','Low Fat','low fat']), 'Item_Fat_Content'] = 'Low Fat'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:52.853168Z",
     "start_time": "2020-04-12T05:26:52.840939Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Low Fat', 'Regular'], dtype=object)"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['Item_Fat_Content'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:54.017354Z",
     "start_time": "2020-04-12T05:26:54.001295Z"
    }
   },
   "outputs": [],
   "source": [
    "test.loc[test['Item_Fat_Content'].isin(['reg','Regular']), 'Item_Fat_Content'] = 'Regular'\n",
    "test.loc[test['Item_Fat_Content'].isin(['LF','Low Fat','low fat']), 'Item_Fat_Content'] = 'Low Fat'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:55.368316Z",
     "start_time": "2020-04-12T05:26:55.356654Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Low Fat', 'Regular'], dtype=object)"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test['Item_Fat_Content'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:26:56.513662Z",
     "start_time": "2020-04-12T05:26:56.498405Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Item_Identifier                 0\n",
       "Item_Weight                     0\n",
       "Item_Fat_Content                0\n",
       "Item_Visibility                 0\n",
       "Item_Type                       0\n",
       "Item_MRP                        0\n",
       "Outlet_Identifier               0\n",
       "Outlet_Establishment_Year       0\n",
       "Outlet_Size                  2410\n",
       "Outlet_Location_Type            0\n",
       "Outlet_Type                     0\n",
       "Item_Outlet_Sales               0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:04.168911Z",
     "start_time": "2020-04-12T05:27:04.148565Z"
    }
   },
   "outputs": [],
   "source": [
    "train.loc[train['Outlet_Identifier'].isin(['OUT045','OUT017']), 'Outlet_Size'] = 'Small'\n",
    "train.loc[train['Outlet_Identifier'].isin(['OUT010']), 'Outlet_Size'] = 'Medium'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:05.160221Z",
     "start_time": "2020-04-12T05:27:05.147944Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Medium', 'High', 'Small'], dtype=object)"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['Outlet_Size'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:06.367588Z",
     "start_time": "2020-04-12T05:27:06.355157Z"
    }
   },
   "outputs": [],
   "source": [
    "test.loc[test['Outlet_Identifier'].isin(['OUT045','OUT017']), 'Outlet_Size'] = 'Small'\n",
    "test.loc[test['Outlet_Identifier'].isin(['OUT010']), 'Outlet_Size'] = 'Medium'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:07.083377Z",
     "start_time": "2020-04-12T05:27:07.073591Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Medium', 'Small', 'High'], dtype=object)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test['Outlet_Size'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:08.894664Z",
     "start_time": "2020-04-12T05:27:08.878665Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Item_Identifier              0\n",
       "Item_Weight                  0\n",
       "Item_Fat_Content             0\n",
       "Item_Visibility              0\n",
       "Item_Type                    0\n",
       "Item_MRP                     0\n",
       "Outlet_Identifier            0\n",
       "Outlet_Establishment_Year    0\n",
       "Outlet_Size                  0\n",
       "Outlet_Location_Type         0\n",
       "Outlet_Type                  0\n",
       "Item_Outlet_Sales            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:15.737292Z",
     "start_time": "2020-04-12T05:27:15.725131Z"
    }
   },
   "outputs": [],
   "source": [
    "target = train['Item_Outlet_Sales']\n",
    "train.drop('Item_Outlet_Sales',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:21.829260Z",
     "start_time": "2020-04-12T05:27:21.804274Z"
    }
   },
   "outputs": [],
   "source": [
    "# convert fat_content variable to integer\n",
    "fat_content_dict = {'Regular':0, 'Low Fat':1}\n",
    "train[\"Item_Fat_Content\"] = train[\"Item_Fat_Content\"].apply(lambda x: fat_content_dict[x])\n",
    "test[\"Item_Fat_Content\"] = test[\"Item_Fat_Content\"].apply(lambda x: fat_content_dict[x])\n",
    "\n",
    "# convert variable to integer\n",
    "train['Item_Fat_Content'] = np.array(train['Item_Fat_Content']).astype('int')\n",
    "test['Item_Fat_Content'] = np.array(test['Item_Fat_Content']).astype('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:25.262835Z",
     "start_time": "2020-04-12T05:27:25.239746Z"
    }
   },
   "outputs": [],
   "source": [
    "# convert size variable to integer\n",
    "out_size_dict = {'High':0, 'Medium':1, 'Small':2}\n",
    "train[\"Outlet_Size\"] = train[\"Outlet_Size\"].apply(lambda x: out_size_dict[x])\n",
    "test[\"Outlet_Size\"] = test[\"Outlet_Size\"].apply(lambda x: out_size_dict[x])\n",
    "\n",
    "# convert variable to integer\n",
    "train['Outlet_Size'] = np.array(train['Outlet_Size']).astype('int')\n",
    "test['Outlet_Size'] = np.array(test['Outlet_Size']).astype('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:27.105890Z",
     "start_time": "2020-04-12T05:27:27.077365Z"
    }
   },
   "outputs": [],
   "source": [
    "# convert loc variable to integer\n",
    "out_loc_type_dict = {'Tier 1':0, 'Tier 2':1, 'Tier 3':2}\n",
    "train[\"Outlet_Location_Type\"] = train[\"Outlet_Location_Type\"].apply(lambda x: out_loc_type_dict[x])\n",
    "test[\"Outlet_Location_Type\"] = test[\"Outlet_Location_Type\"].apply(lambda x: out_loc_type_dict[x])\n",
    "\n",
    "# convert variable to integer\n",
    "train['Outlet_Location_Type'] = np.array(train['Outlet_Location_Type']).astype('int')\n",
    "test['Outlet_Location_Type'] = np.array(test['Outlet_Location_Type']).astype('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:29.119154Z",
     "start_time": "2020-04-12T05:27:29.101851Z"
    }
   },
   "outputs": [],
   "source": [
    "# convert type variable to integer\n",
    "out_type_dict = {'Supermarket Type1':0, 'Supermarket Type2':1, 'Supermarket Type3':2, 'Grocery Store': 3}\n",
    "train[\"Outlet_Type\"] = train[\"Outlet_Type\"].apply(lambda x: out_type_dict[x])\n",
    "test[\"Outlet_Type\"] = test[\"Outlet_Type\"].apply(lambda x: out_type_dict[x])\n",
    "\n",
    "# convert variable to integer\n",
    "train['Outlet_Type'] = np.array(train['Outlet_Type']).astype('int')\n",
    "test['Outlet_Type'] = np.array(test['Outlet_Type']).astype('int')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:31.412437Z",
     "start_time": "2020-04-12T05:27:31.401104Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027',\n",
       "       'OUT035', 'OUT045', 'OUT046', 'OUT049'], dtype=object)"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "le = LabelEncoder()\n",
    "le.fit(train['Outlet_Identifier'])\n",
    "\n",
    "le.classes_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:33.670605Z",
     "start_time": "2020-04-12T05:27:33.658606Z"
    }
   },
   "outputs": [],
   "source": [
    "train['Outlet_Identifier'] = le.transform(train['Outlet_Identifier'])\n",
    "test['Outlet_Identifier'] = le.transform(test['Outlet_Identifier'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:35.267551Z",
     "start_time": "2020-04-12T05:27:35.255338Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Baking Goods', 'Breads', 'Breakfast', 'Canned', 'Dairy',\n",
       "       'Frozen Foods', 'Fruits and Vegetables', 'Hard Drinks',\n",
       "       'Health and Hygiene', 'Household', 'Meat', 'Others', 'Seafood',\n",
       "       'Snack Foods', 'Soft Drinks', 'Starchy Foods'], dtype=object)"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "item_type = LabelEncoder()\n",
    "item_type.fit(train['Item_Type'])\n",
    "\n",
    "item_type.classes_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:36.349341Z",
     "start_time": "2020-04-12T05:27:36.337546Z"
    }
   },
   "outputs": [],
   "source": [
    "train['Item_Type'] = item_type.transform(train['Item_Type'])\n",
    "test['Item_Type'] = item_type.transform(test['Item_Type'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:37.690990Z",
     "start_time": "2020-04-12T05:27:37.678337Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['DRA12', 'DRA24', 'DRA59', ..., 'NCZ42', 'NCZ53', 'NCZ54'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "item_id = LabelEncoder()\n",
    "item_id.fit(train['Item_Identifier'])\n",
    "\n",
    "item_id.classes_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:39.133350Z",
     "start_time": "2020-04-12T05:27:39.121410Z"
    }
   },
   "outputs": [],
   "source": [
    "train['Item_Identifier'] = item_id.transform(train['Item_Identifier'])\n",
    "test['Item_Identifier'] = item_id.transform(test['Item_Identifier'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:43.672828Z",
     "start_time": "2020-04-12T05:27:43.635620Z"
    },
    "scrolled": true
   },
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
       "      <th>Item_Identifier</th>\n",
       "      <th>Item_Weight</th>\n",
       "      <th>Item_Fat_Content</th>\n",
       "      <th>Item_Visibility</th>\n",
       "      <th>Item_Type</th>\n",
       "      <th>Item_MRP</th>\n",
       "      <th>Outlet_Identifier</th>\n",
       "      <th>Outlet_Establishment_Year</th>\n",
       "      <th>Outlet_Size</th>\n",
       "      <th>Outlet_Location_Type</th>\n",
       "      <th>Outlet_Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>156</td>\n",
       "      <td>9.300</td>\n",
       "      <td>1</td>\n",
       "      <td>0.126678</td>\n",
       "      <td>4</td>\n",
       "      <td>249.8092</td>\n",
       "      <td>9</td>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8</td>\n",
       "      <td>5.920</td>\n",
       "      <td>0</td>\n",
       "      <td>0.138846</td>\n",
       "      <td>14</td>\n",
       "      <td>48.2692</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>662</td>\n",
       "      <td>17.500</td>\n",
       "      <td>1</td>\n",
       "      <td>0.129461</td>\n",
       "      <td>10</td>\n",
       "      <td>141.6180</td>\n",
       "      <td>9</td>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1121</td>\n",
       "      <td>19.200</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>6</td>\n",
       "      <td>182.0950</td>\n",
       "      <td>0</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1297</td>\n",
       "      <td>8.930</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9</td>\n",
       "      <td>53.8614</td>\n",
       "      <td>1</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8518</th>\n",
       "      <td>370</td>\n",
       "      <td>6.865</td>\n",
       "      <td>1</td>\n",
       "      <td>0.238293</td>\n",
       "      <td>13</td>\n",
       "      <td>214.5218</td>\n",
       "      <td>1</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8519</th>\n",
       "      <td>897</td>\n",
       "      <td>8.380</td>\n",
       "      <td>0</td>\n",
       "      <td>0.216754</td>\n",
       "      <td>0</td>\n",
       "      <td>108.1570</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8520</th>\n",
       "      <td>1357</td>\n",
       "      <td>10.600</td>\n",
       "      <td>1</td>\n",
       "      <td>0.187580</td>\n",
       "      <td>8</td>\n",
       "      <td>85.1224</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8521</th>\n",
       "      <td>681</td>\n",
       "      <td>7.210</td>\n",
       "      <td>0</td>\n",
       "      <td>0.381078</td>\n",
       "      <td>13</td>\n",
       "      <td>103.1332</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8522</th>\n",
       "      <td>50</td>\n",
       "      <td>14.800</td>\n",
       "      <td>1</td>\n",
       "      <td>0.211845</td>\n",
       "      <td>14</td>\n",
       "      <td>75.4670</td>\n",
       "      <td>8</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>8523 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Item_Identifier  Item_Weight  Item_Fat_Content  Item_Visibility  \\\n",
       "0                 156        9.300                 1         0.126678   \n",
       "1                   8        5.920                 0         0.138846   \n",
       "2                 662       17.500                 1         0.129461   \n",
       "3                1121       19.200                 0         0.000000   \n",
       "4                1297        8.930                 1         0.000000   \n",
       "...               ...          ...               ...              ...   \n",
       "8518              370        6.865                 1         0.238293   \n",
       "8519              897        8.380                 0         0.216754   \n",
       "8520             1357       10.600                 1         0.187580   \n",
       "8521              681        7.210                 0         0.381078   \n",
       "8522               50       14.800                 1         0.211845   \n",
       "\n",
       "      Item_Type  Item_MRP  Outlet_Identifier  Outlet_Establishment_Year  \\\n",
       "0             4  249.8092                  9                         14   \n",
       "1            14   48.2692                  3                          4   \n",
       "2            10  141.6180                  9                         14   \n",
       "3             6  182.0950                  0                         15   \n",
       "4             9   53.8614                  1                         26   \n",
       "...         ...       ...                ...                        ...   \n",
       "8518         13  214.5218                  1                         26   \n",
       "8519          0  108.1570                  7                         11   \n",
       "8520          8   85.1224                  6                          9   \n",
       "8521         13  103.1332                  3                          4   \n",
       "8522         14   75.4670                  8                         16   \n",
       "\n",
       "      Outlet_Size  Outlet_Location_Type  Outlet_Type  \n",
       "0               1                     0            0  \n",
       "1               1                     2            1  \n",
       "2               1                     0            0  \n",
       "3               1                     2            3  \n",
       "4               0                     2            0  \n",
       "...           ...                   ...          ...  \n",
       "8518            0                     2            0  \n",
       "8519            2                     1            0  \n",
       "8520            2                     1            0  \n",
       "8521            1                     2            1  \n",
       "8522            2                     0            0  \n",
       "\n",
       "[8523 rows x 11 columns]"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T05:27:54.572042Z",
     "start_time": "2020-04-12T05:27:54.531477Z"
    }
   },
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
       "      <th>Item_Identifier</th>\n",
       "      <th>Item_Weight</th>\n",
       "      <th>Item_Fat_Content</th>\n",
       "      <th>Item_Visibility</th>\n",
       "      <th>Item_Type</th>\n",
       "      <th>Item_MRP</th>\n",
       "      <th>Outlet_Identifier</th>\n",
       "      <th>Outlet_Establishment_Year</th>\n",
       "      <th>Outlet_Size</th>\n",
       "      <th>Outlet_Location_Type</th>\n",
       "      <th>Outlet_Type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1114</td>\n",
       "      <td>20.750000</td>\n",
       "      <td>1</td>\n",
       "      <td>0.086976</td>\n",
       "      <td>13</td>\n",
       "      <td>107.8622</td>\n",
       "      <td>9</td>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1078</td>\n",
       "      <td>8.300000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.196030</td>\n",
       "      <td>4</td>\n",
       "      <td>87.3198</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1420</td>\n",
       "      <td>14.600000</td>\n",
       "      <td>1</td>\n",
       "      <td>0.315555</td>\n",
       "      <td>11</td>\n",
       "      <td>241.7538</td>\n",
       "      <td>0</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>817</td>\n",
       "      <td>7.315000</td>\n",
       "      <td>1</td>\n",
       "      <td>0.124050</td>\n",
       "      <td>13</td>\n",
       "      <td>155.0340</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1197</td>\n",
       "      <td>12.695633</td>\n",
       "      <td>0</td>\n",
       "      <td>0.344383</td>\n",
       "      <td>4</td>\n",
       "      <td>234.2300</td>\n",
       "      <td>5</td>\n",
       "      <td>28</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5676</th>\n",
       "      <td>233</td>\n",
       "      <td>10.500000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.116174</td>\n",
       "      <td>13</td>\n",
       "      <td>141.3154</td>\n",
       "      <td>8</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5677</th>\n",
       "      <td>308</td>\n",
       "      <td>7.600000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.378141</td>\n",
       "      <td>15</td>\n",
       "      <td>169.1448</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5678</th>\n",
       "      <td>1426</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0.271162</td>\n",
       "      <td>8</td>\n",
       "      <td>118.7440</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5679</th>\n",
       "      <td>521</td>\n",
       "      <td>15.300000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3</td>\n",
       "      <td>214.6218</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5680</th>\n",
       "      <td>997</td>\n",
       "      <td>9.500000</td>\n",
       "      <td>0</td>\n",
       "      <td>0.323605</td>\n",
       "      <td>3</td>\n",
       "      <td>79.7960</td>\n",
       "      <td>7</td>\n",
       "      <td>11</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5681 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Item_Identifier  Item_Weight  Item_Fat_Content  Item_Visibility  \\\n",
       "0                1114    20.750000                 1         0.086976   \n",
       "1                1078     8.300000                 0         0.196030   \n",
       "2                1420    14.600000                 1         0.315555   \n",
       "3                 817     7.315000                 1         0.124050   \n",
       "4                1197    12.695633                 0         0.344383   \n",
       "...               ...          ...               ...              ...   \n",
       "5676              233    10.500000                 0         0.116174   \n",
       "5677              308     7.600000                 0         0.378141   \n",
       "5678             1426    10.000000                 1         0.271162   \n",
       "5679              521    15.300000                 0         0.000000   \n",
       "5680              997     9.500000                 0         0.323605   \n",
       "\n",
       "      Item_Type  Item_MRP  Outlet_Identifier  Outlet_Establishment_Year  \\\n",
       "0            13  107.8622                  9                         14   \n",
       "1             4   87.3198                  2                          6   \n",
       "2            11  241.7538                  0                         15   \n",
       "3            13  155.0340                  2                          6   \n",
       "4             4  234.2300                  5                         28   \n",
       "...         ...       ...                ...                        ...   \n",
       "5676         13  141.3154                  8                         16   \n",
       "5677         15  169.1448                  3                          4   \n",
       "5678          8  118.7440                  7                         11   \n",
       "5679          3  214.6218                  2                          6   \n",
       "5680          3   79.7960                  7                         11   \n",
       "\n",
       "      Outlet_Size  Outlet_Location_Type  Outlet_Type  \n",
       "0               1                     0            0  \n",
       "1               2                     1            0  \n",
       "2               1                     2            3  \n",
       "3               2                     1            0  \n",
       "4               1                     2            2  \n",
       "...           ...                   ...          ...  \n",
       "5676            2                     0            0  \n",
       "5677            1                     2            1  \n",
       "5678            2                     1            0  \n",
       "5679            2                     1            0  \n",
       "5680            2                     1            0  \n",
       "\n",
       "[5681 rows x 11 columns]"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T06:30:51.973532Z",
     "start_time": "2020-04-12T05:29:34.983572Z"
    },
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, description='Optimization Progress', max=300.0, style=ProgressStyle(de…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generation 1 - Current best internal CV score: -1156132.947837275\n",
      "Generation 2 - Current best internal CV score: -1156132.947837275\n",
      "Generation 3 - Current best internal CV score: -1156132.947837275\n",
      "Generation 4 - Current best internal CV score: -1156132.947837275\n",
      "Generation 5 - Current best internal CV score: -1155245.0180700682\n",
      "\n",
      "Best pipeline: RidgeCV(ExtraTreesRegressor(input_matrix, bootstrap=False, max_features=0.3, min_samples_leaf=18, min_samples_split=19, n_estimators=100))\n",
      "-1247086.9479048133\n"
     ]
    }
   ],
   "source": [
    "# finally building model using tpot library\n",
    "# for a sample train it on a sample as it takes a lot of time to train model\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(train, target, train_size=0.75, test_size=0.25)\n",
    "\n",
    "tpot = TPOTRegressor(generations=5, population_size=50, verbosity=2)\n",
    "tpot.fit(X_train, y_train)\n",
    "print(tpot.score(X_test, y_test))\n",
    "tpot.export('tpot_boston_pipeline.py')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T06:48:08.611998Z",
     "start_time": "2020-04-12T06:47:52.589975Z"
    }
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import learning_curve\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "train_sizes = [1, 100, 500, 2000, 5000]\n",
    "train_sizes, train_scores, validation_scores = learning_curve(estimator = LinearRegression(),X = X_train,\n",
    "y = y_train, train_sizes = train_sizes, cv = 5,  n_jobs=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T06:48:14.028432Z",
     "start_time": "2020-04-12T06:48:14.016219Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training scores:\n",
      "\n",
      " [[       nan        nan        nan        nan        nan]\n",
      " [0.56563631 0.54226549 0.54226549 0.54226549 0.54226549]\n",
      " [0.50417531 0.45905523 0.45905523 0.45905523 0.45905523]\n",
      " [0.49018606 0.49147781 0.47846766 0.47846766 0.47846766]\n",
      " [0.49232587 0.49284111 0.48238813 0.49365953 0.48463299]]\n",
      "\n",
      " ----------------------------------------------------------------------\n",
      "\n",
      "Validation scores:\n",
      "\n",
      " [[-0.20089984 -0.44102724 -0.46901162 -0.4309296  -0.41552003]\n",
      " [ 0.40576159  0.4286258   0.45668531  0.4243356   0.44840326]\n",
      " [ 0.45213552  0.4620297   0.49639098  0.4645569   0.48995973]\n",
      " [ 0.47224786  0.47157611  0.5134078   0.46916252  0.50745629]\n",
      " [ 0.47499987  0.47363263  0.51364503  0.46696283  0.50831928]]\n"
     ]
    }
   ],
   "source": [
    "print('Training scores:\\n\\n', train_scores)\n",
    "print('\\n', '-' * 70) # separator to make the output easy to read\n",
    "print('\\nValidation scores:\\n\\n', validation_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T06:49:28.182895Z",
     "start_time": "2020-04-12T06:49:28.166745Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean training scores\n",
      "\n",
      " 1            NaN\n",
      "100    -0.546940\n",
      "500    -0.468079\n",
      "2000   -0.483413\n",
      "5000   -0.489170\n",
      "dtype: float64\n",
      "\n",
      " --------------------\n",
      "\n",
      "Mean validation scores\n",
      "\n",
      " 1       0.391478\n",
      "100    -0.432762\n",
      "500    -0.473015\n",
      "2000   -0.486770\n",
      "5000   -0.487512\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "train_scores_mean = -train_scores.mean(axis = 1)\n",
    "validation_scores_mean = -validation_scores.mean(axis = 1)\n",
    "print('Mean training scores\\n\\n', pd.Series(train_scores_mean, index = train_sizes))\n",
    "print('\\n', '-' * 20) # separator\n",
    "print('\\nMean validation scores\\n\\n',pd.Series(validation_scores_mean, index = train_sizes))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-04-12T07:26:41.804363Z",
     "start_time": "2020-04-12T07:26:41.635813Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-100, 100)"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x396 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "plt.style.use('seaborn')\n",
    "plt.plot(train_sizes, train_scores_mean, label = 'Training error')\n",
    "plt.plot(train_sizes, validation_scores_mean, label = 'Validation error')\n",
    "plt.ylabel('MSE', fontsize = 14)\n",
    "plt.xlabel('Training set size', fontsize = 14)\n",
    "plt.title('Learning curves for a linear regression model', fontsize = 18, y = 1.03)\n",
    "plt.legend()\n",
    "plt.ylim(-100,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tpot_pred = tpot.predict(tpot_test)\n",
    "sub1 = pd.DataFrame(data=tpot_pred)\n",
    "#sub1.index = np.arange(0, len(test)+1)\n",
    "sub1 = sub1.rename(columns = {'0':'Item_Outlet_Sales'})\n",
    "sub1['Item_Identifier'] = test['Item_Identifier']\n",
    "sub1['Outlet_Identifier'] = test['Outlet_Identifier']\n",
    "sub1.columns = ['Item_Outlet_Sales','Item_Identifier','Outlet_Identifier']\n",
    "sub1 = sub1[['Item_Identifier','Outlet_Identifier','Item_Outlet_Sales']]\n",
    "sub1.to_csv('tpot.csv',index=False)"
   ]
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
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": true,
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "164.988px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
