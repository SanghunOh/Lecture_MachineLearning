## 모델 재사용 확인 및  테스트를 위한 전처리
import os
os.getcwd()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

path = os.getcwd() + '/drive/My Drive/Colab Notebooks/bigdataAcademy_Project/'

train_df = pd.read_csv('/root/Documents/datas/readAndwrtieCSV.csv')
train_df.head()

train_df.columns = ['arh', 'execution', 'op', 'label']
train_df.info()


import re
train_df = train_df.fillna(' ')
train_df['op'] = train_df['op'].apply(lambda x : re.sub(r'\d+',' ',x))
train_df.info()

# OPCODE 분리하고 벡터값으로 변경
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

tfidfVectorizer = TfidfVectorizer()
tfidVec_matrix_train = tfidfVectorizer.fit_transform(train_df['op'])

print(tfidVec_matrix_train.shape)

from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold

import numpy
import pandas as pd
import tensorflow as tf

seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

X = tfidVec_matrix_train[:,0:377]
Y_obj = train_df['label']

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

tfidVec_matrix_predict = tfidfVectorizer.transform(['STMFD LDR LDRB CMP LDMNEFD LDR LDR LDR CMP BEQ ADD STR MOV MOV LDR LDR CMP BNE LDR CMP LDRNE MOVNE MOVNE MOV STRB LDMFD LDR CMP STR LDR LDR MOVNE MOVNE LDR LDR CMP LDR LDREQ CMP LDREQ MOV MOV LDR MOV MOV LDR MOV STR STR LDR STR LDR LDR B MOV STMFD SUB SUB STR MOV STR MOV STR SUB MOV MOV MOV BL B MOV STR B LDR MOV LDR ADD LDRB LDR LDR LDRB CMP BNE LDR LDR LDR LDRB MOV MOV SUB ADD ADD MOV STRB LDR ADD STR LDR ADD STR LDR CMP BLS LDR ADD STR LDR LDR BL MOV CMP BCC LDR MOV MOV SUB ADD ADD MOV STRB SUB MOV BL MOV STR LDR MOV SUB LDMFD MOV STMFD SUB SUB STR MOV STR MOV STR SUB MOV MOV MOV BL SUB MOV MOV MOV BL B MOV STR B LDR MOV LDR ADD LDRB LDR LDR LDRB CMP BNE LDR LDR LDR LDRB MOV SUB ADD ADD MOV STRB LDR ADD STR LDR ADD STR LDR CMP BLS LDR ADD STR LDR LDR BL MOV CMP BCC SUB MOV SUB LDMFD MOV STMFD SUB SUB STR LDR LDR STR LDR ADD SUB SUB SUB LDR STR LDR ADD SUB SUB SUB LDR STR MOV STR B LDR LDR SUB LDR LDR LDR SUB LDR LDR EOR LDR EOR LDR EOR LDR STR LDR ADD STR LDR MOV CMP BLE SUB LDMFD MOV STMFD SUB SUB MOV MOV STR STR MOV STR LDR LDR ADD MOV MOV LDR STR LDR LDR LDR LDR MOV MOV MOV SUB LDMIA BL MOV MOV MOV MOV LDR LDR MOV ADDS ADC STR STR LDR MOV MOV MOV LDR STR LDR LDR LDR ADD STR LDR LDR LDR CMP BCS LDR ADD STR LDR LDR ADD LDR STR LDR LDR LDR LDR RSB LDR STR LDR LDR MOV SUB LDMFD MOV STMFD SUB SUB STR LDR LDR MOV BL MOV LDR AND STR BL MOV LDR MVN AND LDR EOR MOV SUB LDMFD MOV STMFD SUB SUB STR MOV STR LDR BL MOV SUB STR B LDR ADD STR LDR MOV LDR ADD LDRB MOV BL MOV CMP BNE B LDR SUB STR LDR LDR CMP BLT LDR MOV LDR ADD LDRB MOV BL MOV CMP BNE LDR STR B LDR LDR RSB MOV LDR ADD LDR MOV LDR ADD LDRB STRB LDR ADD STR LDR LDR CMP BLE LDR LDR RSB MOV LDR ADD MOV STRB SUB LDMFD MOV STMFD SUB SUB STR STR LDR CMP BEQ LDR LDR LDR AND STRB LDR LDR ADD LDR STR B SUB MOV MOV MOV BL SUB LDMFD MOV STMFD SUB SUB STR STR STR STR MOV STR MOV STR LDR CMP BLE MOV STR LDR STR B LDR ADD STR LDR ADD STR LDR LDRB '])
result = e.predict(tfidVec_matrix_predict)

print(result)

