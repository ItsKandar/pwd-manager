from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, PasswordEntry
from .utils.encryption import encrypt, decrypt
from .utils.password_generator import generate_password
from flask import current_app as app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid credentials")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    entries = PasswordEntry.query.filter_by(user_id=current_user.id).all()
    decrypted_entries = []
    for entry in entries:
        try:
            decrypted_password = decrypt(entry.encrypted_password, current_user.username)
        except:
            decrypted_password = "Erreur de déchiffrement"
        decrypted_entries.append({
            "id": entry.id,
            "label": entry.label,
            "login": entry.login,
            "password": decrypted_password,
            "category": entry.category,
            "created_at": entry.created_at
        })
    return render_template("dashboard.html", entries=decrypted_entries)

@app.route("/add", methods=["POST"])
@login_required
def add():
    label = request.form["label"]
    login_data = request.form["login"]
    raw_password = request.form["password"]
    category = request.form["category"]
    encrypted = encrypt(raw_password, current_user.username)
    entry = PasswordEntry(user_id=current_user.id, label=label, login=login_data, encrypted_password=encrypted, category=category)
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:id>")
@login_required
def delete(id):
    entry = PasswordEntry.query.get_or_404(id)
    if entry.user_id != current_user.id:
        flash("Not authorized")
        return redirect(url_for("dashboard"))
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("dashboard"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken")
            return redirect(url_for("register"))
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created. Please log in.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/generate-password")
@login_required
def generate():
    new_password = generate_password()
    return {"password": new_password}