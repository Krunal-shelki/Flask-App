from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from .models import Entry, Water
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
@login_required
def home():
    if request.method == "POST":
        type = request.form.get("type")
        print(type)
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
            new_water = Water(waterCount=waterCount, user_id=current_user)
            db.session.add(new_water)
            db.session.commit()
    return render_template("/views/home.html", user=current_user)


@views.route("/progress")
@login_required
def progress():
    return render_template("/views/progress.html", user=current_user)


@views.route("/profile")
@login_required
def profile():
    return render_template("/views/profile.html", user=current_user)


@views.route("/delete-entry", methods=["POST"])
def delete_note():
    entry = json.loads(request.data)
    entryId = entry["entryId"]
    entry = Entry.query.get(entryId)
    print(entry)
    if entry:
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
    return jsonify({})
