from flask import Flask,jsonify

from datetime import datetime


@app.route('/timedifferecne/<int:n>')


def timedifferecne(n):
    for i in range(int(input())):
        t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        print(abs(int((t1 - t2).total_seconds())))


    @app.route('/timedifferecne/<int:n>')
    def time1():

        return jsonify(print(abs(int((t1 - t2).total_seconds()))))

if __name__=='__main__':
app.run(debug=True)



