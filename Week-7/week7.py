import mysql.connector
import json
from mysql.connector import pooling
from flask import Flask, redirect, url_for, render_template, request, session, jsonify, make_response
from flask_restful import Resource, Api, reqparse


week7 = Flask(__name__)
api = Api(week7)
week7.secret_key = "reqtsgsdfgertersdfgs"

members_pool = pooling.MySQLConnectionPool(
    pool_name="extension",
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    user="root",
    password="1234",
    database="Membership7"
)
# members = members_pool.get_connection()
# cursor = members.cursor()

# ensure ascii = False
week7.config['JSON_AS_ASCII'] = False


@week7.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")


# MemberPage
@week7.route("/member")
def member():
    if "loggedin" in session:
        userId = session["loggedin"]
        ismember = session["memberPk"]
        # get connection form connection pool instead of create one

        members = members_pool.get_connection()
        cursor = members.cursor(buffered=True)

        # Show memberName on memberPage
        cursor.execute(
            "select user_name from member where user_id = %s ", (userId,))
        name = cursor.fetchone()
        name = name[0]

        # Close connection
        cursor.close()
        members.close()

        # turn Tuple into dictionary
        members = members_pool.get_connection()
        cursor = members.cursor(dictionary=True, buffered=True)

        # Select memberName which fits message
        cursor.execute(
            " select member.user_name, message.content from member inner join message on member.id = message.member_id")
        boardComments = cursor.fetchall()
        session["boardComments"] = boardComments

        # Close connection
        cursor.close()
        members.close()

        # Return session into JSON
        return render_template("member.html", memberName=name, allComments=json.dumps(session["boardComments"]))
    else:
        return redirect("/")


# ErrorPage
@week7.route("/error")
def error():
    errorInput = request.args.get("message", "請輸入帳號密碼")
    return render_template("error.html", text=errorInput)


# SignupPage
@week7.route("/signup", methods=["POST"])
def signup():
    userName = request.form["regName"]
    userId = request.form["regAccount"]
    userPassword = request.form["regPassword"]
    try:
        if userName == "" or userId == "" or userPassword == "":
            return redirect("/error?message=請註冊")

        # check if userId exists
        members = members_pool.get_connection()
        cursor = members.cursor(buffered=True)
        cursor.execute(
            "select user_name from member where user_name = %s", (userId,))
        exists = cursor.fetchone()
        if exists:

            session["userName"] = exists

            return redirect("/error?message=帳號已經被註冊")
        else:

            # Commit User-Info into allmembers TABLE
            create = "insert into member(user_name, user_id, user_password) values (%s, %s, %s)"
            cursor.execute(create, (userName, userId, userPassword))
            members.commit()

            return redirect("/")
    except:
        print("?????????????")

    finally:
        cursor.close()
        members.close()


# Check
@week7.route("/signin", methods=["POST"])
def signin():
    userId = request.form["loginAccount"]
    userPassword = request.form["loginPassword"]
    members = members_pool.get_connection()
    cursor = members.cursor(buffered=True)

    try:
        # Check if account exists
        cursor.execute(
            "select id from member where user_id = %s and user_password = %s", (userId, userPassword,))
        ismember = cursor.fetchone()
        if ismember:
            session["loggedin"] = userId
            session["memberPk"] = ismember
            return redirect("/member")
        elif userId == "" or userPassword == "":
            return redirect("/error?message=請輸入帳號密碼")
        else:
            return redirect("/error?message=帳號或密碼錯誤")
    except:
        print("??????????????")
    finally:
        cursor.close()
        members.close()


# Signout Page
@week7.route("/signout")
def signout():
    session.pop("loggedin", None)
    session.pop("memberPk", None)
    return redirect("/")


# Message Page
@week7.route("/message", methods=["POST"])
def message():
    try:
        msg = request.form["msg"]
        userId = session["loggedin"]
        ismember = session["memberPk"]

        # commit comment with session["loggedin"]
        members = members_pool.get_connection()
        cursor = members.cursor(buffered=True)
        comment = "insert into message(member_id, content) values (%s, %s)"
        cursor.execute(comment, (ismember[0], msg,))
        members.commit()
    except:
        print("?????????????")
    # Close connection
    finally:
        cursor.close()
        members.close()

    return redirect("/member")


# API
@week7.route("/api/member", methods=['GET', 'PATCH'])
def api():
    if request.method == "GET":
        userName = request.args.get("username")
        members = members_pool.get_connection()
        cursor = members.cursor(buffered=True)
        try:
            if "loggedin" in session:
                cursor.execute(
                    "select id, user_name, user_id from member where user_id = %s", (userName,))
                searchResult = cursor.fetchall()
                data = {"data": None}

                for result in searchResult:
                    data = {
                        "data": {
                            "id": result[0],
                            "username": result[1],
                            "userId": result[2]
                        }}
                return jsonify(data)

        except:
            print("?????????")

        finally:
            cursor.close()
            members.close()

        # return jsonify(data)

    # Change Name
    if request.method == "PATCH":
        changed = request.get_json()
        members = members_pool.get_connection()
        cursor = members.cursor(buffered=True)
        try:
            if "loggedin" in session and changed["name"] != "":
                userId = session["loggedin"]
                cursor.execute(
                    "update member set user_name = %s where user_id = %s",
                    (changed["name"], userId,)
                )
                members.commit()
                response = {"ok": True}
                return jsonify(response)
            else:
                error = {"error": True}
                return jsonify(error)
        except:
            print("????????")
        finally:
            cursor.close()
            members.close()


if __name__ == "__main__":
    week7.run(port=3000, debug=True)
