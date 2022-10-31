import mysql.connector
import json
from flask import Flask, redirect, url_for, render_template, request, session, jsonify
week6 = Flask(__name__)
week6.secret_key = "432452345tr452"

members = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Membership"
)

# set cursor
cursor = members.cursor()


# HomePage
@week6.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")


# MemberPage
@week6.route("/member")
def member():
    if "loggedin" in session:
        userId = session["loggedin"]
        cursor = members.cursor(buffered=True)

        # Show memberName on memberPage
        cursor.execute(
            "select member_name from allmembers where member_id = %s ", (userId,))
        name = cursor.fetchone()
        name = name[0]

        # turn Tuple into dictionary
        cursor = members.cursor(dictionary=True, buffered=True)

        # Select memberName which fits message
        cursor.execute(
            " select allmembers.member_name, message.content from allmembers inner join message on allmembers.member_id = message.allmembers_id")
        boardComments = cursor.fetchall()
        session["boardComments"] = boardComments

        # Return session into JSON
        return render_template("member.html", memberName=name, allComments=json.dumps(session["boardComments"], ensure_ascii=False))
    else:
        return redirect("/")


# ErrorPage
@week6.route("/error")
def error():
    errorInput = request.args.get("message", "請輸入帳號密碼")
    return render_template("error.html", text=errorInput)


# SignupPage
@week6.route("/signup", methods=["POST"])
def signup():
    userName = request.form["regName"]
    userId = request.form["regAccount"]
    userPassword = request.form["regPassword"]
    if userName == "" or userId == "" or userPassword == "":
        return redirect("/error?message=請註冊")

    # check if userId exists
    cursor = members.cursor(buffered=True)
    cursor.execute(
        "select member_id from allmembers where member_id = %s", (userId,))
    exists = cursor.fetchone()
    if exists:
        return redirect("/error?message=帳號已經被註冊")
    else:

        # Commit User-Info into allmembers TABLE
        create = "insert into allmembers(member_name, member_id, member_password) values (%s, %s, %s)"
        cursor.execute(create, (userName, userId, userPassword))
        members.commit()
        return redirect("/")


# Check
@week6.route("/signin", methods=["POST"])
def signin():
    userId = request.form["loginAccount"]
    userPassword = request.form["loginPassword"]
    cursor = members.cursor(buffered=True)

    # Check if account exists
    cursor.execute(
        "select id from allmembers where member_id = %s and member_password = %s", (userId, userPassword,))
    ismember = cursor.fetchone()
    if ismember:
        session["loggedin"] = userId
        return redirect("/member")
    elif userId == "" or userPassword == "":
        return redirect("/error?message=請輸入帳號密碼")
    else:
        return redirect("/error?message=帳號或密碼錯誤")


# Signout Page
@week6.route("/signout")
def signout():
    session.pop("loggedin", None)
    session.pop("userName", None)
    return redirect("/")


# Message Page
@week6.route("/message", methods=["POST"])
def message():
    msg = request.form["msg"]
    userId = session["loggedin"]

    # commit comment with session["loggedin"]
    cursor = members.cursor(buffered=True)
    comment = "insert into message(allmembers_id, content) values (%s, %s)"
    # USERID為數字是要多增加一欄還是要改
    cursor.execute(comment, (userId, msg,))
    members.commit()

    return redirect("/member")


if __name__ == "__main__":
    week6.run(port=3000, debug=True)
