from flask import Flask, redirect, url_for, render_template, request, make_response
week4 = Flask(__name__)


# Home DONE
@week4.route("/", methods=["POST", "GET"])
def home():
    # logedin = request.cookies.get("account")
    return render_template("home.html")


# Member Page WITH COOKIE  DONE
@week4.route("/member")
def member():
    if "logedin" in request.cookies:
        return render_template("member.html")
    else:
        return redirect("/")


# Empty and Wrong Input Page   DONE
@week4.route("/error")
def error():
    errorInput = request.args.get("message", "請輸入帳號密碼")
    return render_template("error.html", text=errorInput)


# Check Account and Password WITH COOKIE  DONE
@week4.route("/signin", methods=["POST"])
def signin():
    logedin = request.cookies.get("account")
    accountCorrect = request.form["account"]
    passwordCorrect = request.form["password"]
    if accountCorrect == "test" and passwordCorrect == "test":

        # cookieSetting
        resp = make_response(redirect("/member"))
        resp.set_cookie(key="logedin", value="setCookie")
        return resp

    if accountCorrect == "" or passwordCorrect == "":
        # redirect to /error but get message of empty input
        return redirect("/error?message=請輸入帳號密碼")
    if accountCorrect != "test" or passwordCorrect != "test":
        # redirect to /error but get message of wrong input
        return redirect("/error?message=帳號或密碼錯誤")


# Signout Page WITH COOKIE  Done
@week4.route("/signout")
def signout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('logedin')
    return resp


# @week4.route("/square")
# def Square():
#     num = request.args.get("nums", 0)
#     num = int(num)
#     return redirect(url_for("handleSquare", result=num))

# from JS directly send parameters in
@ week4.route("/square/<int:num>")
def handleSquare(num):

    return render_template("result.html", ans=num**2)


if __name__ == "__main__":
    week4.run(port=3000, debug=True)
