from app import app
from flask import Flask, jsonify, request, render_template
import pymongo

# client = pymongo.MongoClient("mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/DprogDb?retryWrites=true&w=majority")
#
# myDb = client["DprogDb"]
#
#
# @app.route('/google-charts')
# def google_pie_chart():
#     data = {"Provinces": "Total Cases"}
#     for coll in myDb.list_collection_names():
#         inner_dict = myDb[coll].find_one({}, {"_id": 0, "Date": 0})
#         data[coll] = int((inner_dict["Total Cases"].replace(',', '')))  # Returns Total Number of Cases Only
#     print(data)
#     return render_template('pie-chart.html', data=data)
#
#
# @app.route('/line-chart')
# def google_line_chart():
#     data = []
#     val = myDb["Ontario"].find({}, {"_id": 0})
#     for txt in val:
#         pair = [v for k, v in txt.items()]
#         data.append([pair[0], int(pair[1].replace(',', ''))])
#
#     return render_template('line-chart.html', data=data)
#
#
# @app.route('/api/all', methods=['GET'])
# def api_all():
#     data = []
#     for coll in myDb.list_collection_names():
#         tb_data = myDb[coll].find({}, {"_id": 0})
#         for txt in tb_data:
#             data.append(txt)
#     return jsonify(data)


if __name__ == "__main__":
    app.static_folder = 'Static'
    app.run()
