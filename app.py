from flask import Flask,render_template,request,jsonify
from flask.helpers import send_file
import io,base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from flask import url_for

from database import engine
from sqlalchemy import text
app = Flask(__name__)
#data=[{"age":34,"usage":3.5},{"age":25,"usage":4},{"age":19,"usage":4.5},{"age":45,"usage":3}]
fig,ax=plt.subplots(figsize=(6,6))
ax=sns.set_style(style="darkgrid")

def load_info_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from info"))
  return result.all()
def add_data_to_db(age_stats,usage_stats):
    with engine.connect() as conn:
        query=conn.execute(text(f"INSERT INTO info(age,time_spent_per_day) VALUES({age_stats},{usage_stats})"))
        

    
    
@app.route("/")
def hello_world():
    return render_template("home.html")
@app.route("/stats",methods=["GET","POST"])
def stats():
    if request.method=="POST":
     age_stats=request.form.get("age")   
     usage_stats=request.form.get("usage")
     add_data_to_db(age_stats, usage_stats)
     return render_template("chart.html")
    else:
      return render_template("chart.html") 
@app.route("/visualize")

def visualize():
     
    
     data=load_info_from_db()
   
     age1=[e[1] for e in data]
     usage=[e[2] for e in data]
     print(age1)
     print(usage)
     sns.scatterplot(x=age1,y=usage).set(title="Age vs Hours spent on social media per day")
     canvas=FigureCanvas(fig)
     img=io.BytesIO()
     fig.savefig(img)
     img.seek(0)
     return send_file(img,mimetype="img/png")
@app.route("/games")
def games():
  return render_template("games.html")

if __name__=="__main__":
    app.run(host="0.0.0.0")
