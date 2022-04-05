import pymysql
from flask import Flask, jsonify
from flask import request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'hys'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Hys@31197'
app.config['MYSQL_DATABASE_DB'] = 'hys'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)


# User Personal and School details
@app.route('/add_new_user', methods=['PUT'])
def add_user():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        # validate the received values
        if _id and request.method == 'PUT':
            # save edits
            sql = "INSERT INTO hys.users(user_id) VALUES(%s)"
            data = _id
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_personal_data', methods=['POST'])
def add_user_personal_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _f_name = _json['first_name']
        _l_name = _json['last_name']
        _profile_pic = _json['profilepic']
        _email_id = _json['email_id']
        _mobile_no = _json['mobile_no']
        _gender = _json['gender']
        _dob = _json['user_dob']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO hys.user_personal_details(user_id,first_name,last_name,profilepic,gender,user_dob," \
                  "address,street,city,state,email_id,mobile_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
            data = (
                _id, _f_name, _l_name, _profile_pic, _gender, _dob, _address, _street, _city, _state, _email_id,
                _mobile_no)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User personal data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_data/<string:id>', methods=['GET'])
def get_user_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.gender gender, pd.user_dob user_dob, pd.address address, pd.street street, pd.city city, pd.state state, pd.email_id email_id, pd.mobile_no mobile_no, sd.school_name school_name, sd.grade grade, sd.stream stream, sd.board board,sd.address school_address, sd.street school_street, sd.city school_city, sd.state school_state from hys.user_personal_details pd inner join hys.user_school_details sd on pd.user_id=sd.user_id where pd.user_id=%s;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_users_data_for_tagging', methods=['GET'])
def get_all_users_data_for_tagging():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.user_id user_id, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, sd.school_name school_name, sd.grade grade from hys.user_personal_details pd inner join hys.user_school_details sd on pd.user_id=sd.user_id;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_preferred_language_data', methods=['POST'])
def add_user_preferred_languages_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _preferred_lang = _json['preferred_lang']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO hys.user_preferred_languages(user_id,preferred_lang) VALUES(%s,%s); "
            data = (_id, _preferred_lang)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User preferred languages added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_preferred_languages_data/<string:id>', methods=['GET'])
def get_user_preferred_languages_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select preferred_lang from hys.user_preferred_languages where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_school_data', methods=['POST'])
def add_user_school_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _school_name = _json['school_name']
        _grade = _json['grade']
        _stream = _json['stream']
        _board = _json['board']
        _address = _json['address']
        _street = _json['street']
        _city = _json['city']
        _state = _json['state']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO hys.user_school_details(user_id,school_name,grade,stream,board,address,street,city,state) VALUES(%s,%s,%s,%s," \
                  "%s,%s,%s,%s,%s); "
            data = (_id, _school_name, _grade, _stream, _board, _address, _street, _city, _state)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User school data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_strength_data', methods=['POST'])
def add_user_strength_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject = _json['subject']
        _topic = _json['topic']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO hys.user_strength(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            data = (_id, _grade, _subject, _topic)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User strength added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_strength_data/<string:id>', methods=['GET'])
def get_user_strength_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from hys.user_strength where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_weakness_data', methods=['POST'])
def add_user_weakness_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _id = _json['user_id']
        _grade = _json['grade']
        _subject = _json['subject']
        _topic = _json['topic']
        # validate the received values
        if _id and request.method == 'POST':
            # save edits
            sql = "INSERT INTO hys.user_weakness(user_id,grade,subject,topic) VALUES(%s,%s,%s,%s);"
            data = (_id, _grade, _subject, _topic)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User weakness data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_weakness_data/<string:id>', methods=['GET'])
def get_user_weakness_data(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from hys.user_weakness where user_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Questions and answer details
@app.route('/add_user_question_details', methods=['POST'])
def add_user_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json['answer_count']
        _answer_preference = _json['answer_preference']
        _audio_reference = _json['audio_reference']
        _call_date = _json['call_date']
        _call_end_time = _json['call_end_time']
        _call_now = _json['call_now']
        _call_preferred_lang = _json['call_preferred_lang']
        _call_start_time = _json['call_start_time']
        _answer_credit = _json['answer_credit']
        _question_credit = _json['question_credit']
        _view_count = _json['view_count']
        _examlikelyhood_count = _json['examlikelyhood_count']
        _grade = _json['grade']
        _like_count = _json['like_count']
        _note_reference = _json['note_reference']
        _ocr_image = _json['ocr_image']
        _compare_date = _json['compare_date']
        _question = _json['question']
        _question_type = _json['question_type']
        _is_identity_visible = _json['is_identity_visible']
        _subject = _json['subject']
        _topic = _json['topic']
        _text_reference = _json['text_reference']
        _toughness_count = _json['toughness_count']
        _video_reference = _json['video_reference']
        _impression_count = _json['impression_count']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _question_id, _user_id, _answer_count, _answer_preference, _audio_reference, _call_date, _call_end_time,
                _call_now, _call_preferred_lang, _call_start_time, _answer_credit, _question_credit, _view_count,
                _examlikelyhood_count, _grade, _like_count, _note_reference, _ocr_image, _compare_date, _question,
                _question_type, _is_identity_visible, _subject, _topic, _text_reference, _toughness_count,
                _video_reference,
                _impression_count)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_question_details(question_id, user_id, answer_count, answer_preference, audio_reference, call_date, call_end_time, call_now, call_preferred_lang, call_start_time, answer_credit, question_credit, view_count, examlikelyhood_count, grade, like_count,note_reference, ocr_image, compare_date, question, question_type, is_identity_visible, subject, topic, text_reference, toughness_count, video_reference, impression_count) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('User posted question successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_tagged_in_question', methods=['POST'])
def add_users_tagged_in_question():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into hys.users_tagged_with_question(question_id, user_id) values (%s, %s);", data)
            conn.commit()
            resp = jsonify('Users tagged with question added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_questions_posted/<string:id>', methods=['GET'])
def get_user_questions_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference,floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name from hys.user_question_details as qd inner join hys.user_personal_details pd on qd.user_id=pd.user_id inner join hys.user_school_details sd on qd.user_id=sd.user_id where qd.user_id=%s order by qd.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_questions_posted', methods=['GET'])
def get_all_question_posted():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select qd.question_id question_id,qd.user_id user_id,floor(qd.answer_count) answer_count,qd.answer_preference answer_preference,qd.audio_reference audio_reference,qd.call_date call_date,qd.call_end_time call_end_time,qd.call_now call_now,qd.call_preferred_lang call_preferred_lang,qd.call_start_time call_start_time,floor(qd.answer_credit) answer_credit,floor(qd.question_credit) question_credit,floor(qd.view_count) view_count,floor(qd.examlikelyhood_count) examlikelyhood_count,qd.grade grade,floor(qd.like_count) like_count,qd.note_reference note_reference,qd.ocr_image ocr_image,qd.compare_date compare_date,qd.question question,qd.question_type question_type,qd.is_identity_visible is_identity_visible,qd.subject subject,qd.topic topic,qd.text_reference text_reference,floor(qd.toughness_count) toughness_count,qd.video_reference video_reference,floor(qd.impression_count) impression_count,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.profilepic profilepic, pd.city city, sd.school_name school_name from hys.user_question_details as qd inner join hys.user_personal_details pd on qd.user_id=pd.user_id inner join hys.user_school_details sd on qd.user_id=sd.user_id order by qd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_like_details', methods=['POST'])
def add_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _like_type = _json['like_type']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _like_type)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.questions_like_details(question_id, user_id, like_type) values (%s, %s, %s);", data)
            conn.commit()
            resp = jsonify('Users like details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_like_details', methods=['DELETE'])
def delete_questions_like_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from hys.questions_like_details where question_id=%s and user_id=%s;", data)
            conn.commit()
            resp = jsonify('Users like details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_toughness_details', methods=['POST'])
def add_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _toughness_level = _json['toughness_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _toughness_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.questions_toughness_details(question_id, user_id, toughness_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users toughness details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_toughness_details', methods=['DELETE'])
def delete_questions_toughness_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from hys.questions_toughness_details where question_id=%s and user_id=%s;", data)
            conn.commit()
            resp = jsonify('Users toughness details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_questions_examlikelyhood_details', methods=['POST'])
def add_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _examlikelyhood_level = _json['examlikelyhood_level']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id, _examlikelyhood_level)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.questions_examlikelyhood_details(question_id, user_id, examlikelyhood_level) values (%s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_questions_examlikelyhood_details', methods=['DELETE'])
def delete_questions_examlikelyhood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'DELETE':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from hys.questions_examlikelyhood_details where question_id=%s and user_id=%s;",
                           data)
            conn.commit()
            resp = jsonify('Users examlikelyhood details deleted successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_counts_in_question_details', methods=['PUT'])
def update_counts_in_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _answer_count = _json["answer_count"]
        _like_count = _json["like_count"]
        _view_count = _json["view_count"]
        _examlikelyhood_count = _json["examlikelyhood_count"]
        _toughness_count = _json["toughness_count"]
        _impression_count = _json["impression_count"]
        # validate the received values
        if _user_id and request.method == 'PUT':
            data = (_answer_count, _view_count, _examlikelyhood_count, _like_count, _toughness_count, _impression_count,
                    _user_id, _question_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "update hys.user_question_details set answer_count=%s, view_count=%s, examlikelyhood_count=%s, like_count=%s, toughness_count=%s, impression_count=%s where user_id=%s and question_id=%s;",
                data)
            conn.commit()
            resp = jsonify('Count updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Answers
@app.route('/post_answer_on_question_details', methods=['POST'])
def post_answer_on_question_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json["user_id"]
        _comment_count = _json["comment_count"]
        _audio_reference = _json["audio_reference"]
        _like_count = _json["like_count"]
        _upvote_count = _json["upvote_count"]
        _downvote_count = _json["downvote_count"]
        _note_reference = _json["note_reference"]
        _image = _json["image"]
        _compare_date = _json["compare_date"]
        _answer = _json["answer"]
        _answer_type = _json["answer_type"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_answer_id, _question_id, _user_id, _comment_count, _audio_reference, _like_count, _upvote_count,
                    _downvote_count, _note_reference, _image, _compare_date, _answer, _answer_type, _text_reference,
                    _video_reference)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_answer_details(answer_id, question_id, user_id, comment_count, audio_reference, like_count, upvote_count, downvote_count, note_reference, image, compare_date, answer, answer_type, text_reference,video_reference) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Users posted answer successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_tagged_in_answer', methods=['POST'])
def add_users_tagged_in_answer():
    conn = None
    cursor = None
    try:
        _json = request.json
        _question_id = _json["answer_id"]
        _user_id = _json['user_id']
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_question_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into hys.users_tagged_with_answer(answer_id, user_id) values (%s, %s);", data)
            conn.commit()
            resp = jsonify('Users tagged with answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_answer_posted', methods=['GET'])
def get_all_answer_posted():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id answer_id, ad.question_id question_id, ad.user_id user_id, ad.comment_count comment_count, ad.audio_reference audio_reference, ad.like_count like_count, ad.upvote_count upvote_count, ad.downvote_count downvote_count, ad.note_reference note_reference, ad.image image, ad.compare_date compare_date, ad.answer answer, ad.answer_type answer_type, ad.text_reference text_reference, ad.video_reference video_reference, pd.first_name first_name, pd.last_name last_name,pd.profilepic profilepic,pd.city city,sd.school_name school_name, sd.grade grade from hys.user_answer_details ad inner join hys.user_personal_details pd on ad.user_id=pd.user_id inner join hys.user_school_details sd on ad.user_id=sd.user_id order by ad.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_answers_posted/<string:id>', methods=['GET'])
def get_user_answers_posted(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select ad.answer_id, ad.question_id, ad.user_id, ad.comment_count, ad.audio_reference, ad.like_count, ad.upvote_count, ad.downvote_count, ad.note_reference, ad.image, ad.compare_date, ad.answer, ad.answer_type, ad.text_reference, ad.video_reference, qd.subject,qd.topic from hys.user_answer_details ad inner join hys.user_question_details qd on ad.question_id=qd.question_id where ad.user_id=%s order by ad.createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_answer_comment', methods=['POST'])
def add_users_answer_comment():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _comment = _json["comment"]
        _comment_type = _json["comment_type"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _note_reference = _json["note_reference"]
        _text_reference = _json["text_reference"]
        _video_reference = _json["video_reference"]
        _audio_reference = _json["audio_reference"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_comment_id, _answer_id, _question_id, _user_id, _comment, _comment_type, _like_count, _reply_count,
                    _audio_reference, _note_reference, _text_reference, _video_reference, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_answer_comment_details(comment_id,answer_id,question_id,user_id,comment,comment_type,like_count,reply_count,audio_reference,note_reference,text_reference,video_reference,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('Comment on answer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_answer_comments', methods=['GET'])
def get_all_answer_comments():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select acd.comment_id comment_id, acd.answer_id answer_id, acd.question_id question_id, acd.user_id user_id, acd.comment comment, acd.comment_type comment_type, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, acd.like_count like_count, acd.reply_count reply_count, acd.audio_reference audio_reference, acd.note_reference note_reference, acd.text_reference text_reference, acd.video_reference video_reference, acd.compare_date compare_date from hys.user_answer_comment_details acd inner join hys.user_personal_details pd on acd.user_id = pd.user_id inner join hys.user_school_details sd on acd.user_id = sd.user_id order by acd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_users_answer_reply', methods=['POST'])
def add_users_answer_reply():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _answer_id = _json["answer_id"]
        _question_id = _json["question_id"]
        _user_id = _json['user_id']
        _reply = _json["reply"]
        _reply_type = _json["reply_type"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (
                _reply_id, _comment_id, _answer_id, _question_id, _user_id, _reply, _reply_type, _like_count,
                _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_answer_reply_details(reply_id, comment_id, answer_id, question_id, user_id, reply, reply_type, like_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('reply on comment added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_answer_reply', methods=['GET'])
def get_all_answer_reply():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select rd.reply_id reply_id, rd.comment_id comment_id, rd.answer_id answer_id, rd.question_id question_id, rd.user_id user_id, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, sd.school_name school_name, sd.grade grade, rd.reply reply, rd.reply_type, rd.like_count like_count, rd.compare_date compare_date from hys.user_answer_reply_details rd inner join hys.user_personal_details pd on rd.user_id=pd.user_id inner join hys.user_school_details sd on rd.user_id=sd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_details', methods=['POST'])
def add_sm_post_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _post_type = _json["post_type"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _post_type, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_post_details(post_id, user_id, post_type, compare_date) values(%s ,%s ,%s ,%s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_mood_details', methods=['POST'])
def add_sm_mood_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json['user_id']
        _message = _json["message"]
        _user_mood = _json["user_mood"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if _user_id and request.method == 'POST':
            data = (_post_id, _user_id, _message, _user_mood, _imagelist_id, _videolist_id, _usertaglist_id, _privacy,
                    _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_mood_details(post_id, user_id, message, user_mood, imagelist_id, videolist_id, usertaglist_id, privacy, like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_images', methods=['POST'])
def add_sm_post_images():
    conn = None
    cursor = None
    try:
        _json = request.json
        _imagelist_id = _json["imagelist_id"]
        _image = _json['image']
        # validate the received values
        if request.method == 'POST':
            data = (_imagelist_id, _image)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into hys.sm_post_images(imagelist_id, image) values(%s ,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_videos', methods=['POST'])
def add_sm_post_videos():
    conn = None
    cursor = None
    try:
        _json = request.json
        _videolist_id = _json["videolist_id"]
        _video = _json['video']
        _thumbnail = _json['thumbnail']
        # validate the received values
        if request.method == 'POST':
            data = (_videolist_id, _video, _thumbnail)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into hys.sm_post_videos(videolist_id, video, thumbnail) values(%s ,%s,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_post_users_tagged', methods=['POST'])
def add_sm_post_users_tagged():
    conn = None
    cursor = None
    try:
        _json = request.json
        _usertaglist_id = _json["usertaglist_id"]
        _user_id = _json['user_id']
        # validate the received values
        if request.method == 'POST':
            data = (_usertaglist_id, _user_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("insert into hys.sm_post_users_tagged(usertaglist_id, user_id) values(%s ,%s);", data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_posts', methods=['GET'])
def get_all_sm_post():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select post_id, user_id, post_type, compare_date from hys.user_sm_post_details order by createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_images', methods=['GET'])
def get_all_sm_images():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select imagelist_id, image from hys.sm_post_images;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_videos', methods=['GET'])
def get_all_sm_videos():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select videolist_id, video, thumbnail from hys.sm_post_videos;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_usertagged', methods=['GET'])
def get_all_sm_usertagged():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select usertaglist_id, user_id from hys.sm_post_users_tagged;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_mood_posts', methods=['GET'])
def get_all_sm_mood_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.gender gender, md.post_id post_id, md.user_id user_id, md.message message, md.user_mood user_mood, md.imagelist_id imagelist_id, md.usertaglist_id usertaglist_id, md.privacy privacy, md.like_count like_count, md.comment_count comment_count, md.view_count view_count, md.impression_count impression_count, md.compare_date compare_date, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, pd.gender gender, sd.school_name school_name, sd.grade grade from hys.user_sm_mood_details md inner join hys.user_personal_details pd on md.user_id=pd.user_id inner join hys.user_school_details sd on md.user_id=sd.user_id order by md.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_comment_details', methods=['POST'])
def add_user_sm_comment_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _comment = _json["comment"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _reply_count = _json["reply_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _comment_id, _post_id, _user_id, _comment, _imagelist_id, _videolist_id, _usertaglist_id, _like_count,
                _reply_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_comment_details(comment_id, post_id, user_id, comment, imagelist_id, videolist_id, usertaglist_id, like_count, reply_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_comment_posts', methods=['GET'])
def get_all_sm_comment_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic, cd.comment_id comment_id, cd.post_id post_id, cd.user_id user_id, cd.comment comment, cd.imagelist_id imagelist_id, cd.videolist_id videolist_id, cd.usertaglist_id usertaglist_id, cd.like_count like_count, cd.reply_count reply_count, cd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from hys.user_sm_comment_details cd inner join hys.user_personal_details pd on pd.user_id = cd.user_id inner join hys.user_school_details sd on sd.user_id = cd.user_id order by cd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_reply_details', methods=['POST'])
def add_user_sm_reply_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _reply_id = _json["reply_id"]
        _comment_id = _json["comment_id"]
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _reply = _json["reply"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _like_count = _json["like_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (_reply_id, _comment_id, _post_id, _user_id, _reply, _imagelist_id, _videolist_id, _usertaglist_id,
                    _like_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_reply_details(reply_id, comment_id, post_id, user_id, reply, imagelist_id, videolist_id, usertaglist_id, like_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_reply_posts', methods=['GET'])
def get_all_sm_reply_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select pd.profilepic profilepic,rd.reply_id reply_id, rd.comment_id comment_id, rd.post_id post_id, rd.user_id user_id, rd.reply reply, rd.imagelist_id imagelist_id, rd.videolist_id videolist_id, rd.usertaglist_id usertaglist_id, rd.like_count like_count, rd.compare_date compare_date, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city, sd.school_name school_name, sd.grade grade from hys.user_sm_reply_details rd inner join hys.user_personal_details pd on pd.user_id = rd.user_id inner join hys.user_school_details sd on sd.user_id = rd.user_id order by rd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_cause_details', methods=['POST'])
def add_user_sm_cause_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _message = _json["message"]
        _datetime = _json["datetime"]
        _address = _json["address"]
        _date = _json["date"]
        _eventcategory = _json["eventcategory"]
        _eventname = _json["eventname"]
        _eventsubcategory = _json["eventsubcategory"]
        _eventtype = _json["eventtype"]
        _feedtype = _json["feedtype"]
        _frequency = _json["frequency"]
        _from_ = _json["from_"]
        _from24hrs = _json["from24hrs"]
        _fromtime = _json["fromtime"]
        _grade = _json["grade"]
        _latitude = _json["latitude"]
        _longitude = _json["longitude"]
        _meetingid = _json["meetingid"]
        _subject = _json["subject"]
        _theme = _json["theme"]
        _themeindex = _json["themeindex"]
        _to_ = _json["to_"]
        _to24hrs = _json["to24hrs"]
        _totime = _json["totime"]
        _imagelist_id = _json["imagelist_id"]
        _videolist_id = _json["videolist_id"]
        _usertaglist_id = _json["usertaglist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _message, _datetime, _address, _date, _eventcategory, _eventname, _eventsubcategory,
                _eventtype, _feedtype, _frequency, _from_, _from24hrs, _fromtime, _grade, _latitude, _longitude,
                _meetingid,
                _subject, _theme, _themeindex, _to_, _to24hrs, _totime, _imagelist_id, _videolist_id, _usertaglist_id,
                _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_cause_details(post_id,user_id,message,datetime,address,date,eventcategory,eventname,eventsubcategory,eventtype,feedtype,frequency,from_,from24hrs,fromtime,grade,latitude,longitude,meetingid,subject,theme,themeindex ,to_ ,to24hrs,totime,imagelist_id ,videolist_id ,usertaglist_id ,privacy ,like_count ,comment_count ,view_count ,impression_count ,compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_cause_posts', methods=['GET'])
def get_all_sm_cause_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select cd.post_id post_id,cd.user_id user_id,cd.message message,cd.datetime datetime,cd.address address,cd.date date,cd.eventcategory eventcategory,cd.eventname eventname,cd.eventsubcategory eventsubcategory,cd.eventtype eventtype,cd.feedtype feedtype,cd.frequency frequency,cd.from_ from_,cd.from24hrs from24hrs,cd.fromtime fromtime,cd.grade grade,cd.latitude latitude,cd.longitude longitude,cd.meetingid meetingid,cd.subject subject,cd.theme theme,cd.themeindex themeindex,cd.to_ to_,cd.to24hrs to24hrs,cd.totime totime,cd.imagelist_id imagelist_id,cd.videolist_id videolist_id,cd.usertaglist_id usertaglist_id,cd.privacy privacy,cd.like_count like_count,cd.comment_count comment_count,cd.view_count view_count,cd.impression_count impression_count,cd.compare_date compare_date,pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.city city, pd.gender gender, sd.school_name school_name,sd.grade grade from hys.user_sm_cause_details cd inner join hys.user_personal_details pd on pd.user_id=cd.user_id inner join hys.user_school_details sd on sd.user_id=cd.user_id order by cd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_bideas_details', methods=['POST'])
def add_user_sm_bideas_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _identification = _json["identification"]
        _solution = _json["solution"]
        _target = _json["target"]
        _competitors = _json["competitors"]
        _swot = _json["swot"]
        _strategy = _json["strategy"]
        _funds = _json["funds"]
        _documentlist_id = _json["documentlist_id"]
        _videolist_id = _json["videolist_id"]
        _memberlist_id = _json["memberlist_id"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _identification, _solution, _target, _competitors, _swot,
                _strategy, _funds, _documentlist_id, _videolist_id, _memberlist_id, _privacy, _like_count,
                _comment_count,
                _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_b_ideas_details(post_id, user_id, content, theme, title, identification, solution, target, competitors, swot, strategy, funds, documentlist_id, videolist_id, memberlist_id, privacy,like_count, comment_count, view_count, impression_count, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_bideas_posts', methods=['GET'])
def get_all_sm_bideas_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select bd.post_id post_id, bd.user_id user_id, bd.content content, bd.theme theme, bd.title title, bd.identification identification, bd.solution solution,bd.target target, bd.competitors competitors, bd.swot swot, bd.strategy strategy, bd.funds funds, bd.documentlist_id documentlist_id, bd.videolist_id videolist_id,bd.memberlist_id memberlist_id, bd.privacy privacy, bd.like_count like_count, bd.comment_count comment_count, bd.view_count view_count, bd.impression_count impression_count, bd.compare_date compare_date, pd.profilepic profilepic, pd.first_name first_name, pd.last_name last_name, pd.gender gender, pd.city city, sd.school_name school_name,sd.grade grade from hys.user_sm_b_ideas_details bd inner join hys.user_personal_details pd on bd.user_id=pd.user_id inner join hys.user_school_details sd on bd.user_id = sd.user_id order by bd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_project_details', methods=['POST'])
def add_user_sm_project_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _post_id = _json["post_id"]
        _user_id = _json["user_id"]
        _content = _json["content"]
        _theme = _json["theme"]
        _title = _json["title"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _topic = _json["topic"]
        _requirements = _json["requirements"]
        _purchasedfrom = _json["purchasedfrom"]
        _procedure = _json["procedure_"]
        _theory = _json["theory"]
        _findings = _json["findings"]
        _similartheory = _json["similartheory"]
        _memberlist_id = _json["memberlist_id"]
        _projectvideourl = _json["projectvideourl"]
        _reqvideourl = _json["reqvideourl"]
        _summarydoc = _json["summarydoc"]
        _otherdoc = _json["otherdoc"]
        _privacy = _json["privacy"]
        _like_count = _json["like_count"]
        _comment_count = _json["comment_count"]
        _view_count = _json["view_count"]
        _impression_count = _json["impression_count"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _post_id, _user_id, _content, _theme, _title, _grade, _subject, _topic, _requirements, _purchasedfrom,
                _procedure, _theory, _findings, _similartheory, _memberlist_id, _projectvideourl, _reqvideourl,
                _summarydoc,
                _otherdoc, _privacy, _like_count, _comment_count, _view_count, _impression_count, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_project_details (post_id,user_id,content,theme,title,grade,subject,topic,requirements,purchasedfrom,procedure_,theory,findings,similartheory,memberlist_id,projectvideourl,reqvideourl,summarydoc,otherdoc,privacy,like_count,comment_count,view_count,impression_count,compare_date)  values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('post details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_sm_project_posts', methods=['GET'])
def get_all_sm_project_posts():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from hys.user_sm_project_details prd inner join hys.user_personal_details pd on pd.user_id=prd.user_id inner join hys.user_school_details sd on sd.user_id=prd.user_id order by prd.createdate desc;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_sm_uploads_details', methods=['POST'])
def add_user_sm_uploads_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _upload_type = _json["upload_type"]
        _user_id = _json["user_id"]
        _school_name = _json["school_name"]
        _exam_name = _json["exam_name"]
        _grade = _json["grade"]
        _subject = _json["subject"]
        _chapter = _json["chapter"]
        _topic = _json["topic"]
        _term = _json["term"]
        _year = _json["year"]
        _tags = _json["tags"]
        _description = _json["description"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _upload_id, _upload_type, _user_id, _school_name, _exam_name, _grade, _subject, _chapter, _topic, _term,
                _year, _tags, _description, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_sm_uploads_details(upload_id, upload_type, user_id, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_sm_upload_file_details', methods=['POST'])
def add_sm_upload_file_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _upload_id = _json["upload_id"]
        _file_url = _json["file_url"]
        _file_ext = _json["file_ext"]
        _file_name = _json["file_name"]
        # validate the received values
        if request.method == 'POST':
            data = (_upload_id, _file_url, _file_ext, _file_name)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.sm_upload_files_details(upload_id, file_url, file_ext, file_name) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_uploads/<string:id>', methods=['GET'])
def get_user_uploads(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, user_id, upload_type, school_name, exam_name, grade, subject, chapter, topic, term, year, tags, description, compare_date from hys.user_sm_uploads_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_upload_files', methods=['GET'])
def get_user_upload_files():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select upload_id, file_url, file_name, file_ext,createdate from hys.sm_upload_files_details order by createdate;")
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_achievement_details', methods=['POST'])
def add_user_achievement_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _scorecard_school_name = _json["scorecard_school_name"]
        _scorecard_board_name = _json["scorecard_board_name"]
        _ach_description = _json["ach_description"]
        _ach_image_url = _json["ach_image_url"]
        _ach_title = _json["ach_title"]
        _scorecard_grade = _json["scorecard_grade"]
        _scorecard_total_score = _json["scorecard_total_score"]
        _ach_type = _json["ach_type"]
        _compare_date = _json["compare_date"]
        # validate the received values
        if request.method == 'POST':
            data = (
                _achievement_id, _user_id, _scorecard_school_name, _scorecard_board_name, _ach_description,
                _ach_image_url,
                _ach_title, _scorecard_grade, _scorecard_total_score, _ach_type, _compare_date)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_achievement_details(achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_user_scorecard_details', methods=['POST'])
def add_user_scorecard_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _achievement_id = _json["achievement_id"]
        _user_id = _json["user_id"]
        _subject = _json["subject"]
        _marks = _json["marks"]
        # validate the received values
        if request.method == 'POST':
            data = (_achievement_id, _user_id, _subject, _marks)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "insert into hys.user_scorecard_details(achievement_id, user_id, subject, marks) values(%s, %s, %s, %s);",
                data)
            conn.commit()
            resp = jsonify('data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_achievement_details/<string:id>', methods=['GET'])
def get_user_achievement_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, scorecard_school_name, scorecard_board_name, ach_description, ach_image_url, ach_title, scorecard_grade, scorecard_total_score, ach_type, compare_date from hys.user_achievement_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_user_scorecard_details/<string:id>', methods=['GET'])
def get_user_scorecard_details(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select achievement_id, user_id, subject,marks from hys.user_scorecard_details where user_id=%s order by createdate desc;",
            id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True)
