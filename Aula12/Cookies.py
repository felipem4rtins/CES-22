# Felipe Martins Gomes
# Comp 20
# Exercício: Usando Cookies
# Programa compilado com PyCharm 2018.1.2


from flask import Flask, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    count = int(request.cookies.get('visit-count', 0))
    count += 1
    if count == 1:
        message = 'Você visitou esta página ' + str(count) + ' vez.'
    else: message = 'Você visitou esta página ' + str(count) + ' vezes.'

    resp = make_response(message)
    resp.set_cookie('visit-count', str(count))
    return resp

app.run()