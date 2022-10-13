from flask import Flask, redirect, url_for, render_template, request, session
week4 = Flask(__name__)

week4.secret_key = "ererererer"


# Home DONE
@week4.route("/", methods=["POST", "GET"])
def home():
    # if "logedin" in session:
    # passwordCorrect = session["logedin"]
    # return redirect("/member", code=307)
    return render_template("home.html")


# Member Page   DONE
@week4.route("/member")
def member():
    if "logedin" in session:
        return render_template("member.html")
    else:
        return redirect("/")


# Empty and Wrong Input Page   DONE
@week4.route("/error")
def error():
    errorInput = request.args.get("message", "請輸入帳號密碼")
    return render_template("error.html", text=errorInput)


# Check Account and Password   DONE
@week4.route("/signin", methods=["POST"])
def signin():
    accountCorrect = request.form["account"]
    passwordCorrect = request.form["password"]
    if accountCorrect == "test" and passwordCorrect == "test":
        session["logedin"] = accountCorrect
        # redirect to /member with POST request using code = 307
        # /member page no need to be POST
        return redirect("/member")
    if accountCorrect == "" or passwordCorrect == "":
        # redirect to /error but get message of empty input
        return redirect("/error?message=請輸入帳號密碼")
    if accountCorrect != "test" or passwordCorrect != "test":
        # redirect to /error but get message of wrong input
        return redirect("/error?message=帳號或密碼錯誤")


# Signout Page   Done
@week4.route("/signout")
def signout():
    session.pop("logedin", None)
    return redirect("/")


@week4.route("/square")
def Square():
    num = request.args.get("nums", 0)
    num = int(num)
    # num = num**2
    # return render_template("result.html")
    return redirect(url_for("handleSquare", result=num))


@ week4.route("/square/<int:result>")
def handleSquare(result):
    # if methods == "POST":
    #     root = request.form("num", 0)
    #     root = int(root)
    # return render_template("result.html")
    return render_template("result.html", ans=result**2)


if __name__ == "__main__":
    week4.run(port=3000, debug=True)
