# Semantic Search Engine

## The Semantic Search Engine is Final Year Industry project. It aims to provide a search engine for Azeus Systems limited, to efficiently search through their internal company documents. 

### Important notes: 
 Note 1: Since the original dataset and database are both too large for the submission, they were not submitted with the source code. Rather, a database that contains a smaller subset (test dataset) has been included which might not have all the functionalities shown in the demo. 
 The full dataset can be found in the link: https://drive.google.com/file/d/12mxSfijkvrsTtHwR2wmkvf7Blh_s3MU1/view?usp=sharing

 The database and dataset might need to be placed in correct directories for the proper usage

### Dependencies: 
 Django framework is needed to run the server. The additional dependencies needed for the backend are included in the settings.py file in the backend directory. 

 Similarly, the frontend needs ReactJS framework to run. Additional dependencies can be installed using 
```
npm install
```
command in the frontend directory. 
#### Instructions on model creation 
Please note as the model size is too large, the final model has not been submitted. Nevertheless it can be generated by running Roberta Optimisation.ipynb.
Once the model is exported, please update the filepath for the location in backend/views.py and BERT.ipynb if needed

#### Instructions on database population 
The database can be populated using BERT.ipynb. 
However, if your files are not in .txt format, please extract the text using the following files: 
1. extraction/text_extract.py
1. extraction/image_extract.py

Open the jupyternotebook by running the following command: 

```
python manage.py shell_plus --notebook
```
Make sure to update the filepath where needed such that it points to the directory with the text files.
Run the notebook.


#### Instructions to run the application 
1. 	Install the dependencies
1.  Go to backend directory. Inside the directory, run the command “python manage.py runserver” to start the server
1.  Go to the frontend directory. Run the following command 
    ```
    npm start 
    ```
1.  Install http-server using 
    ```
    npm install http-server
    ```
1.  Go the directory with all the original reports and run the command:
 ```
http-server ./
 ```
The React application as well as server should start and the search engine should be functional given you have the database and directory with original documents.
