# Medicine-Search
It helps you to quickly find alternatives of a medicine on basis of its chemical composition.

The files with name "medicine_data (.py/.ipynb)" are used for exploring and preparing the data using the JSON file "medicine_dataset.json". The results of this are stored in csv format with name "clean_medicine_data.csv" which contains only the relevant information out of the entire dataset. 
After extracting the zip file, keep it in the same folder as rest of the files for your ease, otherwise change the address in the python code file.

The files "medicine_searching (.py/.ipynb)" use the csv file, load it in a pandas dataframe and create a hash table in python using a dictionary as dictionary offer searching in a quick manner.
The user has an option to look for alternatives of a medicine using its brand name or just entering the salt name to look at all the options available and it does support auto-complete where-in it will provide suggestions, if it doesnt find your salt name in our data-base, by considering the value incomplete and looking for that substring in the dictionary.

I'd suggest opening the .ipynb files for better experience and interface but I've attached the .py files too for convenience.

Thank You!
Adit Goyal
