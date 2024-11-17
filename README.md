link to Dataset: https://www.kaggle.com/gdabhishek/fertilizer-prediction


The project focuses on developing a machine learning-based web application that predicts optimal fertilizers for farmers, utilizing parameters such as soil conditions, crop type, and environmental factors. The primary aim is to enhance agricultural productivity while minimizing resource wastage. By integrating predictive analytics with a user-friendly web interface, the application serves as a valuable tool for farmers seeking efficient fertilizer recommendations.
Agriculture relies heavily on informed decision-making regarding fertilizer use. Misapplication of fertilizers can adversely affect crop yield and the environment. This project proposes a recommendation system that leverages machine learning to suggest appropriate fertilizers, thereby supporting sustainable farming practices. The system effectively bridges the gap between advanced technology and the practical needs of rural farmers.
The methodology employed in this project includes several key steps: data collection from agricultural datasets, feature engineering to prepare relevant inputs like nitrogen, phosphorus, and potassium levels, model training using labeled fertilizer data, and the development of a web application using Flask for accessible deployment.
The software utilized in this project comprises Python as the core programming language, Flask for web application development, Scikit-learn for implementing machine learning models, Pickle for saving and loading trained models, and HTML/CSS for the front-end design.
Experimental results indicate that the application achieved high accuracy in fertilizer classification and demonstrated effective predictions based on test inputs. Usability tests further highlighted the app's potential to improve farming decisions.
In conclusion, the project successfully recommends fertilizers based on user-inputted parameters, offering a scalable solution to enhance farming efficiency and productivity. The integration of predictive analytics simplifies decision-making processes for farmers.
Looking ahead, future enhancements could include integrating additional parameters such as real-time weather updates, providing regional language support for broader accessibility, extending the solution to mobile platforms (Android/iOS), and implementing continuous learning mechanisms to improve model accuracy with ongoing data updates.
Dataset consists of 8 variables where 7 variables are considered for predicting output variable. The details of Variable is given Below

N (Nitrogen) : Nitrogen content in the soil. Nitrogen is really important for plant growth (structure), plant food processing (metabolism), and the creation of chlorophyll. Without enough nitrogen in the plant, the plant cannot grow taller, or produce enough food (usually yellow).
P (Phosphorus) : Phosphorus content in the soil. Phosphorus primary role in a plant is to store and transfer energy produced by photosynthesis for use in growth and reproductive processes. Soil P cycles in a variety forms in the soil
K (Potassium) : Potassium content in the soil. Potassium is an essential nutrient for plant growth.
Temperature : Temperature in degree censius. High temperatures affect plant growth in numerous ways. The most obvious are the effects of heat on photosynthesis, in which plants use carbon dioxide to produce oxygen, and respiration, an opposite process in which plants use oxygen to produce carbon dioxide.
Humidity : Relative humidity in %. When conditions are too humid, it may promote the growth of mold and bacteria that cause plants to die and crops to fail, as well as conditions like root or crown rot. Humid conditions also invite the presence of pests, such as fungus gnats, whose larva feed on plant roots and thrive in moist soil.
Soil Type :
Crop Type :
Finally,
Label : This is the output variable which contains 22 unique values i.e., 22 different crops and they are
'10-26-26'
'14-35-14'
'17-17-17'
'20-20'
'28-28'
'DAP'
'Urea'
Exploratory data analysis carried out to fetch insights from the data.

Algorithm :
Only three algorithms are used to predict the output. They are Logistic Regression and Random Forest.\

Accuracy of the model using Logistic Regression is 90%.
Accuracy of the model using Random Forest Classifier is 98%. Random Forest Classifier is used for development of model.



