# npj Digital Medicine paper Supplementary Material

![lint](https://github.com/cam-mobsys/covid19-sounds-npjDM/workflows/lint/badge.svg)

This repository contains codes accompanying the npj digital medicine paper named:
*Sounds of COVID-19: exploring realistic performance of audio-based digital testing*.

## Introduction

To identify Coronavirus disease (COVID-19) cases efficiently, affordably, and at scale, recent work has shown how
audio (including cough, breathing, and voice) based approaches can be used for testing. However, there is a lack
of exploration of how biases and methodological decisions impact these tools' performance in practice.
Due to these issues, many researchers raised concerns about the feasibility and effectiveness of such models
if deployed in real settings. In this work, we investigate the limits of audio-based COVID-19 testing to
create the foundation of realistically applicable audio tools. The aim of this study is two-fold: first, to
investigate the performance of an audio-based COVID-19 testing method while addressing the issues noted in
the previous studies, by using a large crowd-sourced dataset, to the best of our knowledge, unbiased data,
with a methodological design based on realistic assumptions (e.g. independent user split). Second, to explore
the impact of biases and design pipeline on the performance.

## Dataset

For the above purpose, we developed an app to crowd-source audio data. More details about this project can be found
at [https://www.covid-19-sounds.org/](https://www.covid-19-sounds.org/en/). Naturally, data of such origin are
sensitive in nature. Thus, to gain access to the full dataset, a Data Transfer Agreement (DTA) needs to be signed.
To obtain this or to contact the team, please email us:
[covid-19-sounds@cl.cam.ac.uk](mailto:covid-19-sounds@cl.cam.ac.uk).

## Code

Our models are implemented in Python 3 (tested using `3.6`) using Tensorflow `1.15`.
Please note that due to the requirement of Tensorflow `1.15` versions of python above `3.7` are **not** supported.
Before you start, please ensure that you have requested and downloaded the task files as they are not included when
cloning the repository. After receiving the files and in order to reproduce the results, you need to create an
appropriate virtual environment and activate it. You can create such an environment, as is shown below:

```bash
# create a virtual environment for this project (assuming you are in covid19-sounds-neurips)
python3 -m venv ./venv
# now activate it
source ./venv/bin/activate
# and finally, install the dependencies
pip install -r ./requirements.txt
```

As described in the paper, we develop a VGGish based model. We will now describe how to reproduce the results
presented in the paper using the data provided. To reproduce, please follow the steps below:

1. Navigate to the cloned repository (normally, `covid19-sounds-npjDM`)

1. Ensure you have downloaded the *npjDM21_data* files from Google Drive
   - Move the drive file `data_0426_en_all` and `preprocess` to path `COVID19_prediction/data`
   - Prepare input

      ```shell
       cd ./COVID19_prediction/data
       python pickle_data_from_csv.py
      ```

   - Go to model's path `cd ./COVID19_prediction/COVID_model`
      - Train the model `sh run_train.sh`
         -  After training, models will be stored in path `./COVID19_prediction/data/train/` 
      - Test the model `sh run_test.sh`

1. Baselined on model output, we also provide the codes to generate table and figure in our paper in `covid19-sounds-npjDM/results`:

   - Move the drive file `output/*` to path `COVID19_prediction/results/output/`
   - Main experimental findings and figures: `Experiment_results_figures.ipynb`
   - Results in tables: `Experiment_results_tables.ipynb`
   - Results with bias in the data: `Experiment_with_bias_table.ipynb`

## Issues

The code was initially created by Tong Xia ([tx229@cl.cam.ac.uk](mailto:tx229@cl.cam.ac.uk)).
For any questions, please either contact the authors directly or create an issue.
