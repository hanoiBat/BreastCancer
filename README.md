# BreastCancerPrediction

💡 Inspiration 💡
Before we started brainstorming, we tried to formulate a guiding question to help us brainstorm our ideas. We asked ourselves what is a problem or difficulty in our community that could be made easier with a computer program. Immediately, we were struck with the thought of doctors. The breast cancer identification process is long and tedious. As a result, we decided to create a program that could help doctors know which cases will require more attention based on the features of the tumour.

⚙️ What it does ⚙️
The main feature of our app is to predict whether or not the user has breast cancer. We do this by making the user input values for smoothness mean, concave points_mean, radius_se, compactness_se, concavity_se, concave points_se, texture worst, smoothness worst, compactness_worst, symmetry_worst, fractal dimension_worst. Then we plug the values into an equation which is val = (-8.25427891 + 0.25934413sm +  1.86810728concm +  0.29750163symean + 4.68625661rs - 0.0716165compse - 0.031984concse
+ 0.08120882cps + 0.15562404texw + 0.57776422smow + 4.03547874compw + 1.75361088symw + 0.11486053fdw). In the equation, sm = smoothness mean, concm = concave points_mean, rs = radius_se, compse = compactness_se, concse = concavity_se, cps = concave points_se, texw = texture worst, smow = smoothness worst, compw = compactness_worst, symw = symmetry_worst, and fdw = fractal dimension_worst. Finally, we plug in that equation into m.exp(val)/(1+m.exp(val)) this then results in the probability that the patient has breast cancer.

🛠️ How we built it 🛠️
The frontend was completely built in the Python framework called Streamlit. We used numpy, pandas, and Sci-kit learn in order to create a model. The model was then used to create the equation which we used.

😣 Challenges 😣
When beginning this hackathon, we both came from different backgrounds. Both of us were more used to backend work so we decided to use Streamlit in order to create the frontend. However, the problem was that before this hackathon we both had no experience with Streamlit. But, we persevered through this barrier and finished our front-end.

📚 What we learned 📚
During this Hackathon, we learned how to build a decent looking front-end within Python. We also learned how to collaborate well through repl.it and Discord.
