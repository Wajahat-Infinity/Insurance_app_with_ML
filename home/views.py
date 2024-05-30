from django.shortcuts import render
import joblib
import os
import sklearn

# Construct the file path
model_path = os.path.join(os.path.dirname(__file__), '../static/random_forest_regressor')

# Load the model
model = joblib.load(model_path)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def prediction(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        gender = int(request.POST.get("gender"))
        bmi = float(request.POST.get("bmi"))  # BMI is typically a float
        children = int(request.POST.get("children"))
        smoker = int(request.POST.get("smoker"))
        region = int(request.POST.get("region"))
        print(age, gender, bmi, children, smoker, region)

        pred = model.predict([[age, gender, bmi, children, smoker, region]])

        output = {
            'output': pred[0]  # pred is an array, return the first element
        }
        return render(request, "prediction.html", output)
    else:
        import sklearn
        print(sklearn.__version__)
        return render(request, "prediction.html")

def contact(request):
    return render(request, "contact.html")
