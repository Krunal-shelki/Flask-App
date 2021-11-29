from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import json
from .models import Entry, EntrySchema, Water, WaterSchema, User
from . import db
from sqlalchemy.sql import func
from marshmallow import schema

views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        type = request.form.get("type")
        if type == "Food" or type == "Exercise":
            entryName = request.form.get("entryName")
            cal = request.form.get("caloriesData")
            count = request.form.get("entryCount")
            new_entry = Entry(
                type=type, item=entryName, cal=cal, count=count, user_id=current_user.id
            )
            db.session.add(new_entry)
            db.session.commit()
        elif type == "Water":
            waterCount = request.form.get("waterCount")
            new_water = Water(water_count=waterCount, user_id=current_user.id)
            db.session.add(new_water)
            db.session.commit()
    return render_template("/views/home.html", user=current_user)


@views.route("/delete-entry", methods=["POST"])
def delete_note():
    entry = json.loads(request.data)
    entryId = entry["entryId"]
    entry = Entry.query.get(entryId)
    if entry:
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
    return jsonify({})


@views.route("/cals-data")
@login_required
def cals_data():
    entry = current_user.entries
    entry_schema = EntrySchema(many=True)
    output = entry_schema.dump(entry)
    return jsonify({"Entry": output})


@views.route("/water-data")
@login_required
def water_data():
    water_entry = current_user.Water_entries
    entry_schema = WaterSchema(many=True)
    output = entry_schema.dump(water_entry)
    return jsonify({"water": output})
