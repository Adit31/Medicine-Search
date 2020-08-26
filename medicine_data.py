import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
file = open("medicine_dataset.json")
data = json.load(file)
df = pd.json_normalize(data['results'])
df.head(5)
def flatten_json(nested_json, exclude=['']):
    out = {}

    def flatten(x, name='', exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out
new_df = pd.DataFrame([flatten_json(x) for x in data['results']])
new_df1 = new_df[['product_type','product_id','marketing_category','generic_name','brand_name','brand_name_base','labeler_name','active_ingredients_0_strength','active_ingredients_0_name']].copy()
new_df1.head()
np.random.seed(42)
new_df1['price'] = np.random.randint(50,4500,new_df1.shape[0])
new_df1.head()
new_df1.shape
new_df1 = new_df1.dropna( how = 'any', axis = 0)
new_df1.shape
new_df1 = new_df1.sort_values("price")
new_df1.reset_index(inplace = True, drop = True)
new_df1.head()
new_df1.to_csv("clean_medicine_data.csv")