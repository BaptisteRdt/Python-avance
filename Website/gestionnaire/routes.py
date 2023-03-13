from flask import Flask, render_template

def configure_routes(app: Flask()):
    """
    Fonction qui configure les routes d'une application Flask rentrée

    Args: 
        app: Flask, application Flask

    Returns:
        Pas de paramètres de retour 
    """

    # Les URLs 
    URLs: dict = {
        'index': 'http://localhost:5000/',
        'dix_annees': 'http://localhost:5000/les-dix-annees-les-plus-chaudes-depuis-1996',
        'changement_temp': 'http://localhost:5000/changement-de-temperature-dans-le-temps',
        'jour_de_vent': 'http://localhost:5000/jour-ou-les-eoliennes-n-ont-pas-tounees',
        'fort_changement_temp_semaine': 'http://localhost:5000/fort-changement-de-temperature-dans-une-semaine'
    }

    # route decorator
    # http://localhost:5000/
    @app.route('/')
    def index():
        return render_template("index.html", urls=URLs, name1="Quentin", name2="Simon", name3="Baptiste", url_img_AI_model="./picture/img1.png")

    @app.route('/les-dix-annees-les-plus-chaudes-depuis-1996')
    def dix_annee():
        return render_template("dix_annees.html", urls=URLs)

    @app.route('/changement-de-temperature-dans-le-temps')
    def changement_temp():
        return render_template("changement_temp.html", urls=URLs)

    @app.route('/jour-ou-les-eoliennes-n-ont-pas-tounees')
    def jour_de_vent():
        return render_template("jour_de_vent.html", urls=URLs)

    @app.route('/fort-changement-de-temperature-dans-une-semaine')
    def fort_changement_dans_semaine():
        return render_template("fort_changement_temp_semaine.html", urls=URLs)