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


###################### REGISTRATION ############################
@app.route('/add_store_details', methods=['POST'])
@cross_origin()
def add_store_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        _store_name = _json['store_name']
        _store_image_url = _json['store_image_url']
        _store_mobile_number = _json['store_mobile_number']
        _store_email_id = _json['store_email_id']
        _gst_cert_image_url = _json['gst_cert_image_url']
        _store_pan_number = _json['store_pan_number']
        _address = _json['address']
        _city = _json['city']
        _zip_code = _json['zip_code']
        _state = _json['state']
        _profile_verify_status = _json['profile_verify_status']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_store_id, _store_name, _store_image_url, _store_mobile_number, _store_email_id, _gst_cert_image_url, _store_pan_number, _address, _city, _zip_code, _state, _profile_verify_status, _compare_date)
            cursor.execute(" insert into u155614453_restro.tbl_d_store(store_id, store_name, store_image_url, store_mobile_number, store_email_id, "
                           " gst_cert_image_url, store_pan_number, address, city, zip_code, state, profile_verify_status, compare_date) "
                           " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
            conn.commit()
            resp = jsonify('Store details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_owner_details', methods=['POST'])
@cross_origin()
def add_owner_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _owner_id = _json['owner_id']
        _store_id = _json['store_id']
        _owner_name = _json['owner_name']
        _email_id = _json['email_id']
        _mobile_number = _json['mobile_number']
        _aadhar_number = _json['aadhar_number']
        _pan_number = _json['pan_number']
        _zip_code = _json['zip_code']
        _owner_image_url = _json['owner_image_url']
        _aadhar_image_url = _json['aadhar_image_url']
        _pan_image_url = _json['pan_image_url']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_owner_id, _store_id, _owner_name, _email_id, _mobile_number, _aadhar_number, _pan_number, _zip_code, _owner_image_url, _aadhar_image_url, _pan_image_url, _compare_date)
            cursor.execute(" insert into u155614453_restro.tbl_d_owner(owner_id, store_id, owner_name, email_id, mobile_number, aadhar_number, pan_number, "
                           " zip_code, owner_image_url, aadhar_image_url, pan_image_url, compare_date) "
                           " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
            conn.commit()
            resp = jsonify('Store owner details added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/store_verified', methods=['POST'])
@cross_origin()
def store_verified():
    conn = None
    cursor = None
    try:
        _json = request.json
        _store_id = _json['store_id']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(" select * from u155614453_restro.tbl_d_store where store_id=%s; ", _store_id)
            row = cursor.fetchall()
            value = "false"
            if len(row) >0 :
                if row[0]["profile_verify_status"]=="PENDING":
                    value="false"
                else:
                    value="true"
            else:
                value = "no_entry"
            resp = value
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


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
        _tax_percent = _json['tax_percent']
        _subproduct_list = _json['subproduct_list']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_store_id, _product_id, _product_name, _product_image_url, _product_desc, _discount_percent, _avg_rating, _veg_nonveg, _tax_percent, _compare_date)
            cursor.execute("insert into u155614453_restro.tbl_d_product(store_id, product_id, product_name, product_image_url, product_desc, discount_percent, " 
              "avg_rating, veg_nonveg, tax_percent, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
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
        _tax_percent = _json['tax_percent']
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
            _store_id, _product_id, _product_name, _product_image_url, _product_desc, _discount_percent, _avg_rating, _tax_percent,
            _veg_nonveg, _compare_date)
            cursor.execute(
                "insert into u155614453_restro.tbl_d_product(store_id, product_id, product_name, product_image_url, product_desc, discount_percent, "
                "avg_rating, tax_percent, veg_nonveg, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ", data)
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
                " pro.compare_date compare_date, pro.discount_percent discount_percent, pro.tax_percent tax_percent, 0 as overall_qnty   "
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


@app.route('/add_order', methods=['POST'])
@cross_origin()
def add_order():
    conn = None
    cursor = None
    try:
        _json = request.json
        _order_id = _json['order_id']
        _store_id = _json['store_id']
        _table_num = _json['table_num']
        _customer_id = _json['customer_id']
        _category_id = _json['category_id']
        _product_id = _json['product_id']
        _subproduct_id = _json['subproduct_id']
        _quantity = _json['quantity']
        _total_quantity = _json['total_quantity']
        _price = _json['price']
        _line_amount = _json['line_amount']
        _total_amount = _json['total_amount']
        _tax_amount = _json['tax_amount']
        _discount_amount = _json['discount_amount']
        _tax_percent = _json['tax_percent']
        _discount_percent = _json['discount_percent']
        _coupon_id = _json['coupon_id']
        _compare_date = _json['compare_date']
        _order_datetime = _json['order_datetime']
        _order_complete_datetime = _json['order_complete_datetime']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(" delete from u155614453_restro.tbl_d_order where order_id=%s;", _order_id)
            conn.commit()
            data = (
            _order_id, _store_id, _table_num, _customer_id, _category_id, _product_id, _subproduct_id, _quantity, _total_quantity,
            _price, _line_amount, _total_amount, _tax_amount, _discount_amount, _tax_percent, _discount_percent,
            _coupon_id, _compare_date, _order_datetime, _order_complete_datetime)
            cursor.execute(
                " insert into u155614453_restro.tbl_d_order (order_id, store_id, table_num, customer_id, category_id, product_id, subproduct_id, quantity, total_quantity, price, line_amount, total_amount, tax_amount, "
                " discount_amount, tax_percent, discount_percent, coupon_id, compare_date, order_datetime, order_complete_datetime, order_status) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0); ",
                data)
            conn.commit()
            resp = jsonify('order added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_order_from_store', methods=['POST'])
@cross_origin()
def add_order_from_store():
    conn = None
    cursor = None
    try:
        _json = request.json
        _order_id = _json['order_id']
        _store_id = _json['store_id']
        _table_num = _json['table_num']
        _customer_id = _json['customer_id']
        _category_id = _json['category_id']
        _product_id = _json['product_id']
        _subproduct_id = _json['subproduct_id']
        _quantity = _json['quantity']
        _total_quantity = _json['total_quantity']
        _price = _json['price']
        _line_amount = _json['line_amount']
        _total_amount = _json['total_amount']
        _tax_amount = _json['tax_amount']
        _discount_amount = _json['discount_amount']
        _tax_percent = _json['tax_percent']
        _discount_percent = _json['discount_percent']
        _coupon_id = _json['coupon_id']
        _compare_date = _json['compare_date']
        _order_datetime = _json['order_datetime']
        _order_complete_datetime = _json['order_complete_datetime']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            data = (_order_id, _subproduct_id)
            cursor.execute(
                " select * from u155614453_restro.tbl_d_order where order_id=%s and subproduct_id=%s;",
                data)
            previousOrder = cursor.fetchall()
            if len(previousOrder) > 0:
                qnt = _quantity+previousOrder[0]["quantity"]
                taxAmt = (qnt * _price)*(_tax_percent/100)
                data = (qnt, _price*qnt, taxAmt, _order_id, _subproduct_id)
                cursor.execute(
                    " update u155614453_restro.tbl_d_order set quantity=%s, line_amount=%s, tax_amount=%s where order_id=%s and subproduct_id=%s;",
                    data)
                conn.commit()
            else:
                data = (
                    _order_id, _store_id, _table_num, _customer_id, _category_id, _product_id, _subproduct_id,
                    _quantity, _total_quantity,
                    _price, _line_amount, _total_amount, _tax_amount, _discount_amount, _tax_percent, _discount_percent,
                    _coupon_id, _compare_date, _order_datetime, _order_complete_datetime)
                cursor.execute(
                    " insert into u155614453_restro.tbl_d_order (order_id, store_id, table_num, customer_id, category_id, product_id, subproduct_id, quantity, total_quantity, price, line_amount, total_amount, tax_amount, "
                    " discount_amount, tax_percent, discount_percent, coupon_id, compare_date, order_datetime, order_complete_datetime, order_status) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0); ",
                    data)
                conn.commit()
            data = (_total_quantity, _total_amount, _order_id)
            cursor.execute(
                " update u155614453_restro.tbl_d_order set total_quantity=%s, total_amount=%s where order_id=%s;",
                data)
            conn.commit()
            resp = jsonify('order updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/add_customer_details', methods=['POST'])
@cross_origin()
def add_customer_details():
    conn = None
    cursor = None
    try:
        _json = request.json
        _customer_id = _json['customer_id']
        _first_name = _json['first_name']
        _last_name = _json['last_name']
        _email_id = _json['email_id']
        _mobile_no = _json['mobile_no']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        _compare_date = _json['compare_date']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (
            _customer_id, _first_name, _last_name, _email_id, _mobile_no, _latitude, _longitude, _compare_date)
            cursor.execute(
                " insert into u155614453_restro.tbl_d_customer (customer_id, first_name, last_name, email_id, mobile_no, latitude, longitude, compare_date) values(%s, %s, %s, %s, %s, %s, %s, %s); ",
                data)
            conn.commit()
            resp = jsonify('customer added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/get_order_details/<string:storeid>', methods=['GET'])
def get_order_details(storeid):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            " WITH total_rder_detials AS (   "
            "     select distinct ord.order_id order_id, ord.table_num table_num, cust.customer_id customer_id, cust.first_name first_name, cust.last_name last_name, cust.mobile_no mobile_no, cust.email_id email_id, "
            "  prod.product_id product_id, prod.product_name product_name, prod.product_image_url product_image_url, prod.product_desc product_desc, prod.veg_nonveg veg_nonveg,  "
            " subprod.subproduct_id subproduct_id, subprod.subproduct_name subproduct_name, subprod.price price, "
            " cat.category_id category_id, cat.category_name category_name, cat.category_desc category_desc, cat.category_image_url category_image_url,  "
            " ord.quantity quantity, ord.line_amount line_amount, ord.total_quantity total_quantity, ord.total_amount total_amount, ord.tax_amount tax_amount, ord.tax_percent tax_percent,  "
            " ord.discount_amount discount_amount, ord.discount_percent discount_percent, ord.coupon_id coupon_id, ord.order_status order_status, ord.order_datetime order_datetime,  "
            " ord.order_complete_datetime order_complete_datetime, ord.compare_date compare_date, ord.createdate createdate "
            " from u155614453_restro.tbl_d_order ord  "
            " inner join u155614453_restro.tbl_d_customer cust on cust.customer_id=ord.customer_id  "
            " inner join u155614453_restro.tbl_d_category cat on cat.category_id=ord.category_id  "
            " inner join u155614453_restro.tbl_d_product prod on prod.product_id = ord.product_id  "
            " inner join u155614453_restro.tbl_d_subproduct subprod on subprod.subproduct_id = ord.subproduct_id  "
            " order by ord.createdate desc, ord.order_id)  "
            " select distinct mord.order_id order_id, "
            " (select distinct concat('[',group_concat(json_object('order_id',order_id,'table_num',table_num,'customer_id',customer_id,'first_name',first_name,'last_name',last_name, "
            " 'mobile_no',mobile_no,'email_id',email_id,'product_id',product_id,'product_name',product_name,'product_image_url',product_image_url, "
            " 'product_desc',product_desc,'veg_nonveg',veg_nonveg,'subproduct_id',subproduct_id,'subproduct_name',subproduct_name,'price',price, "
            " 'category_id',category_id,'category_name',category_name,'category_desc',category_desc,'category_image_url',category_image_url, "
            " 'quantity',quantity,'line_amount',line_amount,'total_quantity',total_quantity,'total_amount',total_amount,'tax_amount',tax_amount,'tax_percent',tax_percent, "
            " 'discount_amount',discount_amount,'discount_percent',discount_percent,'coupon_id',coupon_id,'order_status',order_status,'order_datetime',order_datetime, "
            " 'order_complete_datetime', order_complete_datetime,'compare_date',compare_date,'createdate',createdate)),']') order_details  "
            " from total_rder_detials where mord.order_id=order_id) order_details  "
            " from u155614453_restro.tbl_d_order mord where mord.store_id=%s order by mord.createdate desc; ", storeid)
        order = cursor.fetchall()
        resp = jsonify(order)
        resp.status_code = 200
        resp.headers.add("Access-Control-Allow-Origin", "*")
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_order_status', methods=['POST'])
@cross_origin()
def update_order_status():
    conn = None
    cursor = None
    try:
        _json = request.json
        _order_id = _json['order_id']
        _order_status = _json['order_status']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor()
            data = (_order_status, _order_id)
            cursor.execute(
                " update u155614453_restro.tbl_d_order set order_status=%s where order_id=%s; ",
                data)
            conn.commit()
            resp = jsonify('order status updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found("error")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_order', methods=['POST'])
@cross_origin()
def delete_order():
    conn = None
    cursor = None
    try:
        _json = request.json
        _order_id = _json['order_id']
        _subproduct_id = _json['subproduct_id']
        _quantity = _json['quantity']
        _type = _json['type']
        # validate the received values
        if  request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            if _type == "true":
                data = (_order_id, _subproduct_id)
                cursor.execute(
                    " select * from u155614453_restro.tbl_d_order where order_id=%s and subproduct_id=%s; ",
                    data)
                order = cursor.fetchall()
                data = (order[0]["total_quantity"] - order[0]["quantity"], order[0]["total_amount"]-order[0]["line_amount"], _order_id)
                cursor.execute(
                    " update u155614453_restro.tbl_d_order set total_quantity=%s, total_amount=%s where order_id=%s; ",
                    data)
                conn.commit()
                data = (_order_id, _subproduct_id)
                cursor.execute(
                    " delete from u155614453_restro.tbl_d_order where order_id=%s and subproduct_id=%s; ",
                    data)
                conn.commit()
            else:
                if _quantity > 0:
                    data = (_order_id, _subproduct_id)
                    cursor.execute(
                        " select * from u155614453_restro.tbl_d_order where order_id=%s and subproduct_id=%s; ",
                        data)
                    order = cursor.fetchall()
                    print(order[0]["total_quantity"])
                    print(order[0]["quantity"])
                    totalQnty = (order[0]["total_quantity"] - order[0]["quantity"]) + _quantity
                    totalAmnt = (order[0]["total_amount"] - order[0]["line_amount"]) + _quantity * order[0]["price"]
                    print(_quantity)
                    print(totalQnty)
                    data = (totalQnty, totalAmnt, _order_id)
                    cursor.execute(
                        " update u155614453_restro.tbl_d_order set total_quantity=%s, total_amount=%s where order_id=%s; ",
                        data)
                    conn.commit()
                    data = (_quantity, _quantity * order[0]["price"], _order_id, _subproduct_id)
                    cursor.execute(
                        " update u155614453_restro.tbl_d_order set quantity=%s, line_amount=%s where order_id=%s and subproduct_id=%s; ",
                        data)
                    conn.commit()
            resp = jsonify('order updated successfully!')
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
    app.run(debug=True)
