from flask import Flask, request, send_file
import database
import geo_converter

app = Flask(__name__)

@app.route("/glebas")
def glebas():
	return database.glebas()


@app.route("/geojson", methods=['POST'])
def geojson():
    geojson_file = geo_converter.get_data(request.form.getlist("glebas"), request.form.get("view"))
    return send_file(geojson_file)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')