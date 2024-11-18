@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    if request.method == 'POST':
        user_name = request.form['user_name']
        new_registration = Registration(event_id=event_id, user_name=user_name)
        db.session.add(new_registration)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', event_id=event_id)

