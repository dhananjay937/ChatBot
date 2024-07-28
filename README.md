In this Python web-based project, we will build a chatbot using deep learning and Flask. The chatbot will be trained on a dataset containing predefined categories (intents), patterns, and responses. We will use a special artificial neural network (ANN) to classify which category the user's message belongs to and then provide a suitable response from the predefined list.

Technologies Used:
1. Flask
2. NLTK (Natural Language Toolkit)
3. Keras
4. Python

For the project you need to  install:- The project requires you to have good knowledge of Python, Keras, and Natural language processing (NLTK). you can install using below commands.
pip install tensorflow 
pip install keras 
pip install pickle
pip install nltk
pip install flask

Project Structure:
1.data.json – Contains predefined patterns and responses categorized by intents.
2.training.py – Script to build and train the ANN model for the chatbot.
3.texts.pkl – A pickle file storing a list of vocabulary words processed using NLTK.
4.labels.pkl – A pickle file containing a list of categories (intents).
5.model.h5 – The trained model file that contains the architecture and weights of the ANN.
6.app.py – Flask application script implementing the web-based GUI for user interaction with the chatbot.

If you are using these files and codes you need to give the path same as the following structure:-

project_root/
1.1 app.py
1.2 training.py
1.3 data.json
1.4 static/
   1.4.1 images/
	   1.4.1.1 neobot.png
		 1.4.1.2 person.png
	 1.4.2 styles/
	   1.4.2.1 style.css
	 1.4.3 scripts/
	   1.4.3.1 app.js
1.5 templates/
     1.5.1 index.html
