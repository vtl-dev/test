import web, json, hashlib

f = open("database.txt")
dbinfo = eval(f.read())
f.close()
render = web.template.render('app')
db = web.database(dbn=dbinfo["dbn"], user=dbinfo["user"], pw=dbinfo["pw"], db=dbinfo["dbname"])

urls = (
  '/', 'index',
  '/user', 'user',
  '/login', 'login',
  '/logout', 'logout',
  '/course/(.*)', 'course_by_id'
)

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
#session = web.session.Session(app, web.session.DBStore(db, 'app_sessions'))

class index:
    def GET(self):
        if session.get("logged_in", False):
            return render.index()
        return render.login(False)

class test:
    def GET(self):
        # example GET requests

        result = db.query("SELECT * from todo t")
        # result is a list of rows from the query
        output = {}

        for i in result:
            # saves title columnu to a id in a dictionary output
            output[i["id"]] = i["title"]
        json_output = json.dumps(output)
        return json_output

    def POST(self):
        # example POST request

        # takes in a titleInput from AJAX request
        title = web.input().titleInput
        n = db.insert('todo', title=title)
        json_output = json.dumps({"post" : 123, 45: 54})
        return json_output

class user:

    def GET(self):
        return render.createUser(False)

    def POST(self):
        web_input = web.input(email="", pw="")
        email = web_input.email
        pw = web_input.pw
        if email and pw:
            email = email.lower().strip()
            pw = pw.strip()
            if email.endswith("utoronto.ca"):
                hashedPw = hashlib.md5()
                hashedPw.update(pw)
                pw = hashedPw.hexdigest()
                db.insert('app_users', email=email, pw=pw)
                return "200 OK"
        return render.createUser(False)

    def OPTION(self):
        web_input = web.input(cur_pw="", new_pw="")
        cur_pw = web_input.cur_pw
        new_pw = web_input.new_pw
        if cur_pw and new_pw:
            cur_pw = hashlib.md5().update(cur_pw.strip()).hexdigest()
            new_pw = new_pw.strip()
            result = db.query("SELECT * FROM app_users WHERE pw='%s' and id=%d" % (cur_pw, id))
            if len(result) == 1:
                hashedPw = hashlib.md5()
                hashedPw.update(pw)
                pw = hashedPw.hexdigest()
                db.query("UPDATE app_users SET pw='%s' WHERE pw='%s'" % (new_pw, cur_pw))
                return "200 OK"
        return "400 Bad Request"

class login:

    def GET(self):
        web_input = web.input(email="", pw="", error=False)
        email = web_input.email
        pw = web_input.pw
        error = web_input.error
        if email and pw:
            email = email.lower().strip()
            pw = pw.strip()
            hashedPw = hashlib.md5()
            hashedPw.update(pw)
            pw = hashedPw.hexdigest()
            result = db.query("SELECT * FROM app_users WHERE pw='%s' and email='%s'" % (pw, email))
            if len(result) == 1:
                session.logged_in = True
                raise web.seeother("/")
            else: 
                web.redirect("/login?error=True")
        return render.login(error)

class logout:

    def GET(self):
        session.logged_in = False
        return render.login(False)

class course_by_id:

    def GET(self, course_id):
        result = db.query("SELECT * FROM courses WHERE courses.course_id='%s'" % (course_id))
        web.header('Content-Type', 'application/json')
        data_string = json.dumps(result[0])
        return data_string


if __name__ == "__main__":
    app.run()