import pandas as pd
import numpy as np
df = pd.read_csv("clean_medicine_data.csv")
df.head()
df.rename( columns = {'Unnamed: 0': 'index', 'active_ingredients_0_strength': 'ingredient_strength', 'active_ingredients_0_name': 'ingredient_name'}, inplace = True)
df.head()
dict_val = {}
columns = list(df)
for column_name in columns:
    if column_name == 'ingredient_name':
        for i in range(0,df.shape[0]):
            if df[column_name][i] not in dict_val.keys():
                index_list = []
                index_list.append(i)
                dict_val[df[column_name][i]] = index_list
            else:
                dict_val[df[column_name][i]].append(i)
    else:
        continue
def print_salt_search(user_search):
    if user_search in dict_val.keys():
        j = 0
        for i in range(0,len(dict_val[user_search])):
            index = dict_val[user_search][i]
            print(df.loc[index])
            print("")
            j = j + 1
            if j > 5:
                ans = input("do you want to see more results? (Yes/No) : ")
                ans.lower()
                if ans == 'no':
                    break
                else:
                    j = 0
                    continue
    else:
        print("Please enter the complete name to search")
        for salt,index in dict_val.items():
            if user_search in salt:
                j = 0
                for i in range(0,len(dict_val[salt])):
                    index = dict_val[salt][i]
                    print(df.loc[index])
                    print("")
                    j = j + 1
                    if j > 5:
                        break

def print_med_search(user_search):
    flag = 0
    for i in range(0,df.shape[0]):
        if user_search == df['brand_name'][i]:
            salt_present = df['ingredient_name'][i]
            flag = 1
            break
    if flag == 0:
        print("not found in the database, please try again!")
    else:
        print_salt_search(salt_present)

user_choice = input("1. Enter the salt whose alternatives you want to check : \n 2. Enter the medicine brand name whose alternatives you want to check :\n")
if user_choice == '1':
    user_search = input("Enter the salt name : ")
    print_salt_search(user_search.upper())
elif user_choice == '2':
    user_search = input("Enter the medicine name : ")
    print_med_search(user_search)
else:
    print("Enter a valid choice")
