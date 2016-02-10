#!/usr/bin/env python

from sklearn.preprocessing import LabelEncoder
from xgboost.sklearn import XGBClassifier
import pandas as pd

from kairbnb.io import generate_submission, load_users

train_users = pd.read_csv('../cache/train_users.csv1')
test_users = pd.read_csv('../cache/test_users.csv1')

y_train = train_users['country_destination']
train_users.drop(['country_destination', 'id'], axis=1, inplace=True)
train_users = train_users.fillna(-1)
x_train = train_users.values
label_encoder = LabelEncoder()
encoded_y_train = label_encoder.fit_transform(y_train)

test_users_ids = test_users['id']
test_users.drop('id', axis=1, inplace=True)
test_users = test_users.fillna(-1)
x_test = test_users.values

clf = XGBClassifier(
    max_depth=7,
    learning_rate=0.15,
    n_estimators=80,
    objective="rank:pairwise",
    gamma=0,
    min_child_weight=1,
    max_delta_step=0,
    subsample=1,
    colsample_bytree=0.8,
    colsample_bylevel=1,
    reg_alpha=0,
    reg_lambda=1,
    scale_pos_weight=1,
    base_score=0.5,
    missing=None,
    silent=True,
    nthread=-1,
    seed=42
)

clf.fit(x_train, encoded_y_train)
y_pred = clf.predict_proba(x_test)

train_users = pd.read_csv('../cache/train_users_with_age.csv')
test_users = pd.read_csv('../cache/test_users_with_age.csv')

y_train = train_users['country_destination']
train_users.drop(['country_destination', 'id'], axis=1, inplace=True)
train_users = train_users.fillna(-1)
x_train = train_users.values
label_encoder = LabelEncoder()
encoded_y_train = label_encoder.fit_transform(y_train)

test_users_ids = test_users['id']
test_users.drop('id', axis=1, inplace=True)
test_users = test_users.fillna(-1)
x_test = test_users.values

clf = XGBClassifier(
    max_depth=7,
    learning_rate=0.18,
    n_estimators=80,
    objective="rank:pairwise",
    gamma=0,
    min_child_weight=1,
    max_delta_step=0,
    subsample=1,
    colsample_bytree=1,
    colsample_bylevel=1,
    reg_alpha=0,
    reg_lambda=1,
    scale_pos_weight=1,
    base_score=0.5,
    missing=None,
    silent=True,
    nthread=-1,
    seed=42
)

clf.fit(x_train, encoded_y_train)
y_2_pred = clf.predict_proba(x_test)



train_users = pd.read_csv('../cache/train_users_with_age_et.csv')
test_users = pd.read_csv('../cache/test_users_with_age_et.csv')

y_train = train_users['country_destination']
train_users.drop(['country_destination', 'id'], axis=1, inplace=True)
train_users = train_users.fillna(-1)
x_train = train_users.values
label_encoder = LabelEncoder()
encoded_y_train = label_encoder.fit_transform(y_train)

test_users_ids = test_users['id']
test_users.drop('id', axis=1, inplace=True)
test_users = test_users.fillna(-1)
x_test = test_users.values

clf = XGBClassifier(
    max_depth=7,
    learning_rate=0.18,
    n_estimators=80,
    objective="rank:pairwise",
    gamma=0,
    min_child_weight=1,
    max_delta_step=0,
    subsample=1,
    colsample_bytree=1,
    colsample_bylevel=1,
    reg_alpha=0,
    reg_lambda=1,
    scale_pos_weight=1,
    base_score=0.5,
    missing=None,
    silent=True,
    nthread=-1,
    seed=42
)

clf.fit(x_train, encoded_y_train)
y_3_pred = clf.predict_proba(x_test)


y_pred = (y_pred * 0.6) + (y_2_pred * 0.2) + (y_3_pred * 0.2)

generate_submission(y_pred, test_users_ids, label_encoder, name='ensemble')
