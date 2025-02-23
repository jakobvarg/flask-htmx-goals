from flask import Flask, url_for, render_template, render_template_string, request, redirect

course = Flask('__name__')

COURSE_CURR= []
# COURSE_CURR = [
#   {'id': 1, 'goal': "HTML and CSS for 2 Weeks"},
#   {'id': 2, 'goal': "Python for 4 Weeks"},
# ]

@course.route('/', methods=['GET'])
def home():
  return render_template('home.html', course_curr=COURSE_CURR)
 

@course.route('/add_goal', methods=['POST'])
def add_goal():
  if request.method == 'POST':
    goal = request.form['goal']
    id = max(COURSE_CURR, key = lambda x : x['id'])['id'] + 1 if COURSE_CURR else 1
    new_goal = {'id': id, 'goal': goal}
    COURSE_CURR.append(new_goal)
    print(COURSE_CURR)
  return render_template('_partials/show_goals.html', goal=new_goal)


@course.route('/delete_goal/<int:id>', methods=['DELETE'])
def delete_goal(id):
  global COURSE_CURR
  COURSE_CURR = [goal for goal in COURSE_CURR if goal['id'] != id]
  print(COURSE_CURR)
  return "", 200


if __name__ == '__main__':
  course.run(host='0.0.0.0', debug=True)
