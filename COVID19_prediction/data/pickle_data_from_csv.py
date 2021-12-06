# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:25:58 2021

@author: xiatong
"""

import os

import joblib
import librosa
import numpy as np
import pandas as pd

SR = 16000  # sample rate
SR_VGG = 16000  # VGG pretrained model sample rate
FRAME_LEN = int(SR / 10)  # 100 ms
HOP = int(FRAME_LEN / 2)  # 50%overlap, 5ms
MFCC_DIM = 13

path = "data_0426_en_all"  # Change to your data path
inputFile = "preprocess/data_0426_en_task.csv"
df = pd.read_csv(inputFile)
"""
#Change this inputFile to other csv in prepocess to pickle the data used for bias evaluation
"""

# read from metadata remain type only
labels = {}
with open("prepocess/results_all_raw_0426.csv") as f:
    for index, line in enumerate(f):
        if index > 0:
            temp = line.strip().split(";")
            labels[temp[0] + "/" + temp[7]] = temp

df_train_pos = df[(df["label"] == 1) & (df["fold"] == "train")]
df_train_neg = df[(df["label"] == 0) & (df["fold"] == "train")]
df_vad_pos = df[(df["label"] == 1) & (df["fold"] == "validation")]
df_vad_neg = df[(df["label"] == 0) & (df["fold"] == "validation")]
df_test_pos = df[(df["label"] == 1) & (df["fold"] == "test")]
df_test_neg = df[(df["label"] == 0) & (df["fold"] == "test")]

user_all = {}
user_all["train_covid_id"] = set([u for u in df_train_pos["uid"]])
user_all["train_noncovid_id"] = set([u for u in df_train_neg["uid"]])
user_all["vad_covid_id"] = set([u for u in df_vad_pos["uid"]])
user_all["vad_noncovid_id"] = set([u for u in df_vad_neg["uid"]])
user_all["test_covid_id"] = set([u for u in df_test_pos["uid"]])
user_all["test_noncovid_id"] = set([u for u in df_test_neg["uid"]])


def get_feature(file):
    y, sr = librosa.load(file, sr=SR, mono=True, offset=0.0, duration=None)
    yt, index = librosa.effects.trim(y, frame_length=FRAME_LEN, hop_length=HOP)
    yt_n = yt / np.max(np.abs(yt))  # normolized the sound
    return yt_n


TASK = 2


def get_covid(temp):
    cot, sym, med, smo = temp[9], temp[8], temp[3], temp[4]
    print(cot, sym, med, smo)
    sym_dict = {
        "drycough": 0.0,
        "smelltasteloss": 0.0,
        "headache": 0.0,
        "sorethroat": 0.0,
        "muscleache": 0.0,
        "wetcough": 0.0,
        "shortbreath": 0.0,
        "tightness": 0.0,
        "fever": 0.0,
        "dizziness": 0.0,
        "chills": 0.0,
        "runnyblockednose": 0.0,
        "None": 0.0,
    }
    syms = sym.split(",")
    for s in syms:
        if s == "tighness":
            s = "tightness"
        if s == "drycoough":
            s = "drycough"
        if s == "runny":
            s = "runnyblockednose"
        if s == "none" or s == "":
            s = "None"
        if s in sym_dict:
            sym_dict[s] = 1
    sym_feature = [sym_dict[s] for s in sorted(sym_dict)]
    # for new task1 ans 2, I forgot to remove over14
    if cot == "last14" or cot == "yes" or cot == "positiveLast14":  # or cot == 'positiveOver14' or cot == 'over14':

        if sym in ["None", "", "none"]:
            label = "covidnosym"
        else:
            label = "covidsym"
    elif cot == "negativeNever":

        if sym in ["None", "", "none"]:
            label = "healthnosym"
        else:
            label = "healthsym"
    else:
        label = "negativeLast14_over14"
    return label, sym_feature


def get_android(uid, COVID):
    folds = uid
    data = []
    fold_path = os.listdir(os.path.join(path, folds))
    for files in fold_path:  # date, no more than 5, check label
        fname = uid + "/" + files
        temp = labels[fname]
        covid, sym = get_covid(temp)

        if TASK == 1:
            ccc = "covid" in covid if COVID == "pos" else covid == "healthnosym"
        if TASK == 2:
            ccc = "covid" in covid if COVID == "pos" else "health" in covid

        if ccc:
            samples = os.listdir(os.path.join(path, folds, files))
            for sample in samples:
                if "breath" in sample:
                    file_b = os.path.join(path, folds, files, sample)
                if "cough" in sample:
                    file_c = os.path.join(path, folds, files, sample)
                if "voice" in sample or "read" in sample:
                    file_v = os.path.join(path, folds, files, sample)

            breath = get_feature(file_b)
            cough = get_feature(file_c)
            voice = get_feature(file_v)
            if len(data) >= 5:
                break  # limited label
            data.append({"breath": breath, "cough": cough, "voice": voice, "label": COVID})

    return data


def get_web(uid, COVID):  # date
    folds = "form-app-users"
    data = []
    fname = uid + "/" + uid
    temp = labels[fname]
    # print(get_covid(temp))
    covid, sym = get_covid(temp)
    if TASK == 1:
        ccc = "covid" in covid if COVID == "pos" else covid == "healthnosym"
    if TASK == 2:
        ccc = "covid" in covid if COVID == "pos" else "health" in covid
    if ccc:
        samples = os.listdir(os.path.join(path, folds, uid))
        for sample in samples:
            if "breath" in sample:
                file_b = os.path.join(path, folds, uid, sample)
            if "cough" in sample:
                file_c = os.path.join(path, folds, uid, sample)
            if "voice" in sample or "read" in sample:
                file_v = os.path.join(path, folds, uid, sample)

        breath = get_feature(file_b)
        cough = get_feature(file_c)
        voice = get_feature(file_v)
        data.append({"breath": breath, "cough": cough, "voice": voice, "label": COVID})
    return data


# create directory to store Pickled data if it doesn't exist
if not os.path.exists("./data"):
    os.mkdir("./data")

# pickle postive users
COVID = 1
data_all_covid = {}  #
for fold in ["train_covid_id", "vad_covid_id", "test_covid_id"]:
    data_all_covid[fold] = {}
    for uid in user_all[fold]:
        print("==", uid, "===")
        if "202" in uid:
            temp = get_web(uid, COVID)
            if len(temp) > 0:
                data_all_covid[fold][uid] = temp
        else:
            temp = get_android(uid, COVID)
            if len(temp) > 0:
                data_all_covid[fold][uid] = temp
f = open("./data/audio_0426En_covid.pk", "wb")
joblib.dump(data_all_covid, f)
f.close()
for fold in data_all_covid:
    print(fold, len(data_all_covid[fold]))
del data_all_covid


# pickle negative users
COVID = 0
data_all_noncovid = {}
for fold in ["train_noncovid_id", "vad_noncovid_id", "test_noncovid_id"]:
    data_all_noncovid[fold] = {}
    for uid in user_all[fold]:
        print("==", uid, "===")
        if "202" in uid:
            temp = get_web(uid, COVID)
            if len(temp) > 0:
                data_all_noncovid[fold][uid] = temp
        else:
            temp = get_android(uid, COVID)
            if len(temp) > 0:
                data_all_noncovid[fold][uid] = temp
f = open("./data/audio_0426En_noncovid.pk", "wb")
joblib.dump(data_all_noncovid, f)
f.close()