from flask import Flask, render_template

# Flask instance
app = Flask(__name__)

# route decorator
# http://localhost:5000/
@app.route('/')
def index():
    return render_template("index.html", name1="Quentin", name2="Simon", name3="Baptiste", url_img_AI_model="./picture/img1.png")