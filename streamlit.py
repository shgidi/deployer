import streamlit as st
import json
from joblib import dump, load
import numpy as np
import glob

with open('params.json') as f:
	config = json.load(f)

features = config['feature_names']

models = glob.glob('artifacts/*.joblib')+glob.glob('artifacts/*.pkl')
if len(models)>0:
	model = load(models[0])

st.title('Welcome to')
st.title(config['model_name'])

# show feature fields
if "sklearn" in str(type(model)): # tabular model
	feature_vals = []
	for i,feature in enumerate(features):
		f_type = config["feature_types"][i]
		if f_type["type"] == "float":
			feature_vals.append(st.number_input(f'Which {feature}?', float(f_type["limit"][0]), float(f_type["limit"][1])))

	pred = model.predict(np.array(feature_vals).reshape(1, -1) )[0]

	st.title('prediction is')
	st.title(config['classes'][pred])

elif 'torch' in str(type(model)):
	# load image
	# do the fucking prediction
	pass


