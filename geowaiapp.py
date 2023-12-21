from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample pre-filled data
prefilled_data = [
    {'term': '1', 'week': '1', 'lesson': '1', 'topic': 'Gas Laws', 'subtopic': 'Boyles’ Law', 'lesson_content': 'Stating Boyles’ law', 'remarks': 'Pre-filled data'},
    {'term': '1', 'week': '1', 'lesson': '2', 'topic': 'Gas Laws', 'subtopic': 'Charles Law', 'lesson_content': 'Stating Charles’ law', 'remarks': 'Pre-filled data'},
    # Add more pre-filled data as needed
]

# Sample data (you can replace this with a database)
filled_contents = []

@app.route('/')
def index():
    return render_template('index.html', filled_contents=filled_contents)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        term = request.form['term']
        week = request.form['week']
        lesson = request.form['lesson']
        topic = request.form['topic']
        subtopic = request.form['subtopic']
        lesson_content = request.form['lesson_content']
        remarks = request.form['remarks']

        filled_contents.append({
            'term': term,
            'week': week,
            'lesson': lesson,
            'topic': topic,
            'subtopic': subtopic,
            'lesson_content': lesson_content,
            'remarks': remarks
        })

        return redirect(url_for('index'))

    return render_template('form.html', prefilled_data=prefilled_data)

if __name__ == '__main__':
    app.run(debug=True)
