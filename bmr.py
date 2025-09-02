from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmr(weight_kg, height_cm, age_years,gender):
    #male BMR formula
    
    if gender == 0 :
        if height_cm <= 0:
         raise ValueError("Height must be greater than zero.")
        bmr  = (10*weight_kg) +(6.25*height_cm )-(5*age_years)+5
        return bmr
   
   
   #female bmr formula
    elif gender == 1 :
       if height_cm <=0 :
           raise ValueError("height must be greater than zero.")
       bmr = (10*weight_kg) +(6.25*height_cm )-(5*age_years)-161
       return bmr
         
         
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            name = request.form['name']
            weight = float(request.form['weight_kg'])
            height = float(request.form['height_cm'])
            age = int(request.form['age_years'])
            gender = int(request.form['gender'])
            
            bmr = calculate_bmr(weight, height, age, gender)
            return render_template("index.html", result=f"{name}, your BMR is {bmr:.2f} calories/day")
        except ValueError as e:
            return render_template("index.html", result=str(e))

    return render_template("index.html")
#  render_template("index.html")
                
if __name__=="__main__":
    app.run(debug=True)