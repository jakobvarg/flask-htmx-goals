from flask import Flask, render_template, url_for, request, redirect

HTMX_KNOWLEDGE = [
  'HTMX is a great alternative to React etc.',
  'It offers a different way of loading data into your frontend web UI.',
  'It might be especially interesting for server-side developers who are not so familiar with frontend development.',
  "But - as you will see - it's actually also a very promising alternative to React, Angular etc.",
  'You just have to be open for a diffent mental model.',
  'When using HTMX you typically write way less frontend JavaScript code.',
  "You also don't need to manage any frontend state.",
  'Though you can always add extra JS code if needed.',
  'And you can also combine HTMX with other libraries like AlpineJS or integrate it into React apps etc.']


app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html', list_notes=HTMX_KNOWLEDGE)


@app.route('/info', methods=['GET'])
def info():
  ol_list = "<ol>"+"".join(f"<li>{quote}</li>" for quote in HTMX_KNOWLEDGE)+"</ol>"
  return ol_list

 
@app.route('/add_note', methods=['POST'])
def add_note():
  if request.method == 'POST':
    note = request.form['note']
    HTMX_KNOWLEDGE.insert(0, note)
  return render_template('_partials/show-notes.html', list_notes=HTMX_KNOWLEDGE)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
