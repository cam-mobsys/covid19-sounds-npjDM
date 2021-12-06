#!/bin/bash

'''
This doc records the commends we used to get data statistics.
cd /covid19-sounds-npjDM/COVID19_prediction/data/preprocess
'''

cat results_all_raw_0426.csv | awk -F ';' '{print $1}' | uniq | wc -l
36364
cat results_all_raw_0426.csv | awk -F ';' '{print $1}' | wc -l
75201

cat results_all_raw_0426.csv | grep neverThink | awk -F ';' '{print $1}' | uniq | wc -l
20896
cat results_all_raw_0426.csv | grep neverThink | awk -F ';' '{print $1}' | wc -l
41006

cat results_all_raw_0426.csv | grep -v neverThink | awk -F ';' '{print $1}' | uniq | wc -l
16990
cat results_all_raw_0426.csv | grep -v neverThink | awk -F ';' '{print $1}' | wc -l
34195

# python
# lans = json.load(open('0426_language_labels_raw.json'))
# En_users = lans['en']
# len(En_users)
# Out[13]: 16234

cat result_data_0426_en.csv | awk -F ';' '{print $1}' | uniq | wc -l
2562
cat result_data_0426_en.csv | awk -F ';' '{print $1}' | wc -l
5682

cat result_data_0426_en_all.csv | awk -F ';' '{print $1}' | uniq | wc -l
2482 positive = 514
cat result_data_0426_en_all.csv | awk -F ';' '{print $1}' | wc -l
5366

cat result_data_0426_en_all.csv | grep positiveOver14 | wc -l
116
cat result_data_0426_en_all.csv | grep -v positiveOver14 | awk -F ';' '{print $1}' | uniq | wc -l
2479
cat result_data_0426_en_all.csv | grep -v positiveOver14 | awk -F ';' '{print $1}' | wc -l
5250

quality check delete 116 + 316

$ cat result_data_0426_en_all.csv | awk -F ';' '{print $10}' | sort | uniq
Covid-Tested
last14
negativeNever
over14
positiveLast14
positiveOver14
yes

cat results_all_raw_0426.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes\|positiveLast14\|over14' | wc -l
13586
delete 75201-13586

cat results_all_raw_0426.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | wc -l
13476

cat results_all_raw_0426.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | awk -F ';' '{print $1}' | uniq | wc -l
5663
cat results_all_raw_0426.csv | grep -e 'last14\|positiveLast14\|yes' | wc -l
2080

cat result_data_0426_en.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | wc -l
5374

cat result_data_0426_en.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | awk -F ';' '{print $1}' | uniq | wc -l
2560

cat result_data_0426_en_all.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | awk -F ';' '{print $1}' | uniq | wc -l
2478
cat result_data_0426_en_all.csv | grep -e 'negativeNever\|last14\|positiveLast14\|yes' | wc -l
5240

cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1}' | uniq | wc -l
2015 # (exclude some positive users and will be 1,964)
cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1}' | uniq | wc -l
514

Uid
Age
Sex
Medhistory
Smoking
Language
Date
Folder Name
Symptoms
Covid-Tested
Hospitalized
Location
Voice filename
Cough filename
Breath filename
$ cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$9,$10}' | uniq | awk '{print $2}' | grep -e 'none\|None' | sort | uniq -c
81 None
1 none
16.0, 84.0

xiato@LAPTOP-SB5VB84O MINGW64 /i/propocess
$ cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$9,$10}' | uniq | awk '{print $2}' | grep -e 'none\|None' | sort | uniq -c
1023 None
1 None,shortbreath
4 none
51,49

cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$2,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
77 16-19
409 20-29
594 30-39
497 40-49
243 50-59
113 60-69
47 70-
35 pnts
3.8,20.3,29.5,24.7,12.1,5.6,2.3

cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$2,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
28 16-19
121 20-29
145 30-39
125 40-49
58 50-59
22 60-69
10 70-
6 pnts
5.4,23.5, 28.2, 24.3, 11.3. 4.3, 1.9

cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$3,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
1140 Male
858 Female
17 ptns
6 Other
56,7, 42.5

cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$3,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
287 Male
223 Female
5 pnts
55.3, 43.4

cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$5,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
1120 never
386 ex
175 1to10
127 11to20
119 ltOnce
33 ecig
26 21+
29 ptns
55.6, 19.2, 23.8

cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$5,$10}' | uniq | awk '{print $2}' | sort | uniq -c | sort -nr
333 never
90 ex
34 1to10
24 ltOnce
19 11to20
3 21+
6 ecig
6 ptns
64.8, 17.5, 16.7

$ cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$12}' | uniq | awk '{print $2}' | awk -F ',' '{print $4}' | sort | uniq -c
222 Germany
606 UnitedKingdom
881 UnitedStates
71 Italy
43.7, 30.1, 11.1

cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$5,$10}' | uniq | awk '{print $2}' | awk -F ',' '{print $4}' | sort | uniq -c | sort -nr
114 UnitedStates
57 UnitedKingdom
22 Germany
16 Slovakia
15 Iran
22.1, 11.1, 4.2

cat result_data_0426_en_all.csv | grep -e 'negativeNever' | awk -F ';' '{print $1,$10,$11}' | uniq | awk '{print $3}' | sort | uniq -c | sort -nr
2010 no
10 yes
2 ptns
cat result_data_0426_en_all.csv | grep -e 'last14\|positiveLast14\|yes' | awk -F ';' '{print $1,$11}' | uniq | awk '{print $3}' | sort | uniq -c | sort -nr
491 no
29 yes
