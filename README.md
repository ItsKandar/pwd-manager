# 🔐 Gestionnaire de Mots de Passe - Python + Flask

Une application web simple et sécurisée de gestion de mots de passe, développée avec **Flask**.  
Les mots de passe sont **chiffrés avec AES-256** et stockés en base de données.

---

## ✨ Fonctionnalités

- Création de compte / Connexion utilisateur
- Ajout, affichage et suppression de mots de passe
- Chiffrement des mots de passe avec **AES-256**
- Génération de mots de passe robustes
- Interface web intuitive (HTML/CSS)

---

## ⚙️ Technologies utilisées

- **Python 3.8+**
- **Flask**
- **Flask-Login**
- **Flask-SQLAlchemy**
- **pycryptodome** (pour AES)
- **SQLite** (par défaut, extensible à PostgreSQL)

---

## 🚀 Installation & Lancement

### 1. Cloner le projet
```bash
git clone url
cd pwd-manager
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

```bash
python run.py
```

Accéder à l’application sur http://127.0.0.1:5000

Les mots de passe sont chiffrés avec AES-256 (mode EAX)
Chaque utilisateur ne peut accéder qu'à ses propres données