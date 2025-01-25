from flask import render_template, current_app, request, redirect, url_for, g, jsonify
from .decorators import login_required, require_unauthenticated
from .utils.authentication import get_user_identifiers
from .models import User
from .db import db

app = current_app


@app.route('/')
def home():
    if not getattr(g, 'corbado_user', None):
        return render_template(
            'home_guest.html',
        )
    corbado_user = getattr(g, 'corbado_user')
    user = User.query.filter_by(corbado_user_id=corbado_user.user_id).first()
    return render_template(
        'home_authenticated.html',
        city=(user and user.city) or 'unknown'
    )


@app.route('/userarea')
def user_area():
    if not getattr(g, 'corbado_user', None):
        return render_template(
            'userarea_guest.html',
        )
    return render_template(
        'userarea_authenticated.html',
    )


@app.route('/login')
@require_unauthenticated()
def login():
    return render_template(
        'login.html',
    )


@app.route('/signup')
@require_unauthenticated()
def signup():
    return render_template(
        'signup.html',
    )


@app.route('/signup/onboarding', methods=['GET', 'POST'], strict_slashes=False)
@login_required(redirect_to_login=True)
def onboarding():
    corbado_user = getattr(g, 'corbado_user')
    if request.method == 'POST':
        user = User.query.filter_by(corbado_user_id=corbado_user.user_id).one()
        user.city = request.form['city']
        db.session.commit()
        return redirect(url_for('home'))

    user = User.query.filter_by(corbado_user_id=corbado_user.user_id).first()
    if not user:
        user = User(corbado_user_id=corbado_user.user_id)
        db.session.add(user)
        db.session.commit()
    if user.city is not None:
        return redirect(url_for('profile'))
    return render_template(
        'onboarding.html'
    )


@app.route('/profile')
@login_required(redirect_to_login=True)
def profile():
    corbado_user = getattr(g, 'corbado_user')
    user = User.query.filter_by(corbado_user_id=corbado_user.user_id).one()
    identifiers = get_user_identifiers(corbado_user.user_id)
    return render_template(
        'profile.html',
        example_id=user.id, corbado_id=user.corbado_user_id, identifiers=identifiers.identifiers
    )


@app.route('/api/secret', strict_slashes=False)
@login_required(redirect_to_login=False)
def get_secret():
    return jsonify({'secret': 'Passkeys are cool!'})

@app.route('/favicon.ico', strict_slashes=False)
def favicon_redirect():
    return redirect(url_for('static', filename='favicon.ico'))

# Add other routes (e.g., signup, login, profile) as needed
