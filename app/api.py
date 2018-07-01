from . import app, db
from flask import jsonify, request
from .models import *
from sqlalchemy import asc

#handling updates to table view
#endpoint for btcusd
@app.route('/api/update/btcusd/<id>', methods=['GET'])
def check_new_entries_btcusd(id):
    result = Btctrades.query.filter_by(id=id).first_or_404()
    new_entries = Btctrades.query.filter(Btctrades.time_recorded > result.time_recorded).order_by(asc(Btctrades.time_recorded)).limit(50).all()

    if len(new_entries) == 0:
        return jsonify({'updates':'No updates'}),200
    else:
        rows = []
        for item in new_entries:
            rows.append(item.as_dict())
            return jsonify({'updates':rows, 'size':len(rows)}),200

#endpoint for ethusd
@app.route('/api/update/ethusd/<id>', methods=['GET'])
def check_new_entries_ethusd(id):
    result = Ethtrades.query.filter_by(id=id).first_or_404()
    new_entries = Ethtrades.query.filter(Ethtrades.time_recorded > result.time_recorded).order_by(asc(Ethtrades.time_recorded)).limit(50).all()

    if len(new_entries) == 0:
        return jsonify({'updates':'No updates'}),200
    else:
        rows = []
        for item in new_entries:
            rows.append(item.as_dict())
            return jsonify({'updates':rows, 'size':len(rows)}),200


#endpoint for xrpusd
@app.route('/api/update/xrpusd/<id>', methods=['GET'])
def check_new_entries_xrpusd(id):
    result = Xrptrades.query.filter_by(id=id).first_or_404()
    new_entries = Xrptrades.query.filter(Xrptrades.time_recorded > result.time_recorded).order_by(asc(Xrptrades.time_recorded)).limit(50).all()

    if len(new_entries) == 0:
        return jsonify({'updates':'No updates'}),200
    else:
        rows = []
        for item in new_entries:
            rows.append(item.as_dict())
            return jsonify({'updates':rows, 'size':len(rows)}),200
