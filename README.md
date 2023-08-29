# <h1 align="center">Udacity - Data Scientist Nanodegree Program</h1>
<h2 align="center">Project 2: Disaster Response Pipeline</h2>

## Table of Contents
- Udacity - Data Scientist Nanodegree Program
  - [Table of Contents](#table-of-contents)
  - [Project Summary ](#Summary-)
  - [Project File Description ](#description-)
  - [Technical stack ](#technical-)
  - [Installation ](#installation-)
  
## Project Summary <a name="Summary"></a>
In this project, we will leverage our knowledge of ETL, Machine Learning, and related databases to analyze disaster data and then build a machine learning model for an API to classify disaster messages.

## Project File Description <a name="description"></a>
- disaster_messages.csv - Contains those fields: `id` and `categories` (related, offer, aid_related, medical_help..) which from the message.
- disaster_categories.csv - Contains those fields: `id`, `message`, `original`, `genre`.
- DisasterResponse.db - Database contain cleaned data after process and  merge disaster_messages.csv with disaster_categories.csv.
- process_data.py - for doing data cleaning and pre-processing into DisasterResponse.db
- train_classifier.py - for taking data from DisasterResponse.db to train the model
- classifier.pkl - Trained model which saved after done train_classifier.py
- run.py - for runing Web App and checking

## Requirement Technical <a name="technical"></a>
You need to have enough of these knowledge before going into project implementation:
- SQLite Database
- ETL (Python and libraries: pandas, numpy,...)
- Machine Learning (Random Forest, Decision Tree)
- Natural Language Processing (NLP)

## Installation <a name="Installation"></a>
1. Open project workspace IDE. Then we need to enter some of the following commands in bash to complete the project
2. To run ETL pipeline that cleans data and stores in database
```python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db```

3. To run ML pipeline that trains classifier and saves
```python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl```

4. Go to `app` directory: 
```cd app```

5. Run your web app: 
```python run.py```

6. Click the `PREVIEW` button to open the homepage
