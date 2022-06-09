from flask import Flask, json, render_template
from flask.globals import request
from flask import Flask, jsonify
import pymysql
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin


# APPLICATION_ROOT = '/user'
app = Flask(__name__)
# app.config.from_object('config.Config')

CORS(app, resources={r"/": {"origins": ""}})
# app.config.from_object(__name__)

mysql = MySQL()
# app.config['CACHE_TYPE'] = 'simple'
app.config['MYSQL_DATABASE_USER'] = 'u155614453_restro'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Pratik@31197'
app.config['MYSQL_DATABASE_DB'] = 'u155614453_restro'
app.config['MYSQL_DATABASE_HOST'] = '217.21.95.205'
mysql.init_app(app)

###################### CATEGORY ############################
@app.route('/create_category', methods=['POST'])
@cross_origin()
def create_category():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _category_id = _json['category_id']
        _category_name = _json['category_name']
        _category_image_url = _json['category_image_url']
        _category_desc = _json['category_desc']
        _veg_nonveg = _json['veg_nonveg']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_store_id, _category_id, _category_name, _category_image_url, _category_desc,_veg_nonveg,_compare_date)
            cursor.execute("insert into u155614453_restro.tbl_d_category(store_id, category_id, category_name, category_image_url, category_desc, veg_nonveg, compare_date) "
                  " VALUES(%s,%s,%s,%s,%s,%s,%s); ", data)
            conn.commit()
            resp = jsonify('Category created successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_category', methods=['POST'])
@cross_origin()
def update_category():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _category_id = _json['category_id']
        _category_name = _json['category_name']
        _category_image_url = _json['category_image_url']
        _category_desc = _json['category_desc']
        _veg_nonveg = _json['veg_nonveg']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u155614453_restro.tbl_d_category where category_id=%s;", _category_id)
            conn.commit()
            data = (_store_id, _category_id, _category_name, _category_image_url, _category_desc,_veg_nonveg,_compare_date)
            cursor.execute("insert into u155614453_restro.tbl_d_category(store_id, category_id, category_name, category_image_url, category_desc, veg_nonveg, compare_date) "
                  " VALUES(%s,%s,%s,%s,%s,%s,%s); ", data)
            conn.commit()
            resp = jsonify('Category updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_category/<string:id>', methods=['GET'])
def delete_category(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "delete from u155614453_restro.tbl_d_category where category_id=%s;", id)
        conn.commit()
        resp = jsonify(['Category deleted successfully'])
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_categories/<string:id>', methods=['GET'])
def get_all_categories(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u155614453_restro.tbl_d_category where store_id=%s;", id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

######################### PRODUCT ##############################
@app.route('/create_product', methods=['POST'])
@cross_origin()
def create_product():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _product_id = _json['product_id']
        _product_name = _json['product_name']
        _product_image_url = _json['product_image_url']
        _product_desc = _json['product_desc']
        _discount_percent = _json['discount_percent']
        _avg_rating = _json['avg_rating']
        _veg_nonveg = _json['veg_nonveg']
        _subproduct_list = _json['subproduct_list']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_store_id, _product_id, _product_name, _product_image_url, _product_desc, _discount_percent, _avg_rating, _veg_nonveg, _compare_date)
            cursor.execute("insert into u155614453_restro.tbl_d_product(store_id, product_id, product_name, product_image_url, product_desc, discount_percent, " 
              "avg_rating, veg_nonveg, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
            conn.commit()
            for i in range(len(_subproduct_list)):
                subproduct_id = "sub"+_product_id+str(i)
                data = (subproduct_id, _product_id, _subproduct_list[i][0], _subproduct_list[i][1])
                cursor.execute(
                    "insert into u155614453_restro.tbl_d_subproduct(subproduct_id, product_id, subproduct_name, price) values(%s, %s, %s, %s);", data)
                conn.commit()
            resp = jsonify('Product created successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_all_products/<string:id>', methods=['GET'])
def get_all_products(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u155614453_restro.tbl_d_product where store_id=%s;", id)
        row = cursor.fetchall()
        for i in range(len(row)):
            cursor.execute(
                "select * from u155614453_restro.tbl_d_subproduct where product_id=%s;", row[i]["product_id"])
            row[i]["subproduct_list"] = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_product', methods=['POST'])
@cross_origin()
def update_product():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _product_id = _json['product_id']
        _product_name = _json['product_name']
        _product_image_url = _json['product_image_url']
        _product_desc = _json['product_desc']
        _discount_percent = _json['discount_percent']
        _avg_rating = _json['avg_rating']
        _veg_nonveg = _json['veg_nonveg']
        _subproduct_list = _json['subproduct_list']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u155614453_restro.tbl_d_product where product_id=%s", _product_id)
            conn.commit()
            cursor.execute(
                "delete from u155614453_restro.tbl_d_subproduct where product_id=%s;",
                _product_id)
            conn.commit()
            data = (
            _store_id, _product_id, _product_name, _product_image_url, _product_desc, _discount_percent, _avg_rating,
            _veg_nonveg, _compare_date)
            cursor.execute(
                "insert into u155614453_restro.tbl_d_product(store_id, product_id, product_name, product_image_url, product_desc, discount_percent, "
                "avg_rating, veg_nonveg, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
            conn.commit()
            for i in range(len(_subproduct_list)):
                subproduct_id = "sub" + _product_id + str(i)
                data = (subproduct_id, _product_id, _subproduct_list[i][0], _subproduct_list[i][1])
                cursor.execute(
                    "insert into u155614453_restro.tbl_d_subproduct(subproduct_id, product_id, subproduct_name, price) values(%s, %s, %s, %s);",
                    data)
                conn.commit()
            resp = jsonify('Product updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_product/<string:id>', methods=['GET'])
def delete_product(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "delete from u155614453_restro.tbl_d_product where product_id=%s;", id)
        conn.commit()
        resp = jsonify(['Product deleted successfully'])
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


######################### PRODUCT ##############################
@app.route('/create_menucard', methods=['POST'])
@cross_origin()
def create_menucard():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _category_id = _json['category_id']
        _product_id = _json['product_id']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_store_id, _category_id, _product_id, _compare_date)
            cursor.execute("insert into u155614453_restro.tbl_d_menucard(store_id, category_id, product_id, compare_date) values(%s, %s, %s, %s); ", data)
            conn.commit()
            resp = jsonify('Menucard updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_menucard/<string:id>', methods=['GET'])
def get_menucard(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "select * from u155614453_restro.tbl_d_product where store_id=%s;", id)
        product = cursor.fetchall()
        for i in range(len(product)):
            cursor.execute(
                "select * from u155614453_restro.tbl_d_subproduct where product_id=%s;", product[i]["product_id"])
            product[i]["subproduct_list"] = cursor.fetchall()

        cursor.execute(
            "select * from u155614453_restro.tbl_d_category where store_id=%s;", id)
        category = cursor.fetchall()
        for j in range(len(category)):
            data = (id, category[j]["category_id"])
            cursor.execute(
                " select menu.store_id store_id, menu.category_id category_id, menu.product_id product_id, pro.product_name product_name, "
                " pro.product_desc product_desc, pro.product_image_url product_image_url, pro.veg_nonveg veg_nonveg, pro.avg_rating avg_rating,  "
                " pro.compare_date compare_date, pro.discount_percent discount_percent   "
                " from u155614453_restro.tbl_d_menucard menu left join u155614453_restro.tbl_d_product pro "
                " on pro.product_id=menu.product_id where menu.store_id=%s and category_id=%s; ", data)
            category[j]["menu_card"] = cursor.fetchall()
            for i in range(len(category[j]["menu_card"])):
                cursor.execute(
                    "select * from u155614453_restro.tbl_d_subproduct where product_id=%s;", category[j]["menu_card"][i]["product_id"])
                category[j]["menu_card"][i]["subproduct_list"] = cursor.fetchall()
        resp = jsonify([{"menuCategories":category, "products": product}])
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_menucard', methods=['POST'])
@cross_origin()
def update_menucard():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _category_id = _json['category_id']
        _product_list = _json['product_list']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                "delete from u155614453_restro.tbl_d_menucard where category_id=%s", _category_id)
            conn.commit()
            for i in range(len(_product_list)):
                data = (_store_id, _category_id, _product_list[i], _compare_date)
                cursor.execute(
                    "insert into u155614453_restro.tbl_d_menucard(store_id, category_id, product_id, compare_date) values(%s, %s, %s, %s); ",
                    data)
                conn.commit()
            resp = jsonify('Menucard updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    # app.run(debug =True)
    #  serve(app, host="0.0.0.0", port=8080)
    # Relevant documents:
    # http://werkzeug.pocoo.org/docs/middlewares/
    # http://flask.pocoo.org/docs/patterns/appdispatch/
    # from werkzeug.serving import run_simple
    # from werkzeug.wsgi import DispatcherMiddleware
    # app.config['DEBUG'] = True

    # # Load a dummy app at the root URL to give 404 errors.
    # # Serve app at APPLICATION_ROOT for localhost development.
    # application = DispatcherMiddleware(Flask('dummy_app'), {
    #     app.config['APPLICATION_ROOT']: app,
    # })
    # run_simple('localhost', 8080, application, use_reloader=True)
    app.run(host='127.0.0.1', port=8080, debug=True)
