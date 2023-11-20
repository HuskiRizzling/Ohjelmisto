from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<number>')
def prime(number):
    isprime = True
    kl = int(number)
    for i in range(2, kl):
        if kl % i == 0 and (i != 1 or i != kl):
            isprime = False
            break
    return {"Number": number, "isPrime": isprime}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
