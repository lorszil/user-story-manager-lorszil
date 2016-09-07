from flask import *

from model import *

app = Flask(__name__)


@app.route('/story', methods=['GET'])
def get_user_stories():
    user_story = UserStory.select()
    return render_template("form.html", user_story=user_story)


@app.route('/story', methods=['POST'])
def save_userstory():
        columns = ['story_title', 'user_story', 'criteria', 'business_value', 'estimation_time', 'status']
        data = [request.form[element] for element in columns]
        new_user_story = UserStory(story_title=data[0], user_story=data[1], criteria=data[2], business_value=data[3],
                                   estimation_time=data[4], status=data[5])
        new_user_story.save()
        return "Saved!"


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def update_userstory(story_id):
    user_story = UserStory.get(UserStory.id == story_id)
    user_story.update(story_title=request.form['story_title'],
                      user_story=request.form['user_story'],
                      criteria=request.form['acceptance_criteria'],
                      business_value=request.form['business_value'],
                      estimation_time=request.form['estimation_time'],
                      status=request.form['status'])
    user_story.execute()
    return "Updated!"


@app.route('/list', methods=['GET'])
def show_data(story_id):
    return render_template('list.html', user_stories=user_story)


@app.route('/list/')
def list_all_user_stories():
    user_story = UserStory.select()
    return render_template("list.html", user_stories=user_story)


@app.route('/delete/<story_id>', methods=['GET'])
def delete_data(story_id):
    UserStory.delete_data()


if __name__ == '__main__':
    app.run(debug=True)
