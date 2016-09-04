from flask import *

from model import *

app = Flask(__name__)


@app.route('/story', methods=['GET'])
def story():
    empty_list = UserStory(story_title="", user_story="", criteria="", business_value="100",
                             estimation_time="0.5", status="choose an option")
    return render_template('form.html', user_story=empty_list)


@app.route('/save', methods=['POST'])
def save_userstroy():
    user_story = UserStory.create(story_title=request.form['story_title'],
                                user_story=request.form['user_story'],
                                criteria=request.form['acceptance_criteria'],
                                business_value=request.form['business_value'],
                                estimation_time=request.form['estimation'],
                                status=request.form['status'])
    return "Saved!"


@app.route('/update/<story_id>', methods=['POST'])
def update_userstory(story_id):
    user_story = UserStory.get(UserStory.id == story_id)
    user_story.update(story_title=request.form['story_title'],
                user_story=request.form['user_story'],
                criteria=request.form['acceptance_criteria'],
                business_value=request.form['business_value'],
                estimation=request.form['estimation'],
                status=request.form['status'])
    return "Updated!"


@app.route('/show/<story_id>', methods=['GET'])
def show_data(story_id):
    user_story = UserStory.get(UserStory.id == story_id)
    return render_template("form.html", user_story=user_story)


@app.route('/list/')
def list_all_user_stories():
    user_story = UserStory.select()
    print(user_story)
    return render_template('list.html', user_story=user_story)


@app.route('/delete/<story_id>', methods=['GET'])
def delete_user_story(story_id):
    UserStory.delete().where(UserStory.id == story_id).execute()
    return redirect('/list/')




if __name__ == '__main__':
    app.run(debug=True)
