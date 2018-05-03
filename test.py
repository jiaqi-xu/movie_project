#!/usr/bin/env python3
# coding=utf-8
import flask

app = flask.Flask(__name__)


@app.route('/', endpoint="home")
def amihome():
    '''
    请尝试以  `/` 和 `/shajiquan` 两个路径来访问；
    '''
    return "View function: {view}. Endpoint: {endpoint}".format(view="amihome", endpoint=flask.request.endpoint)


# 给 app 添加一条 url rule, 指定 rule, endpoint, 但不指定 view function.
app.add_url_rule(rule='/shajiquan', endpoint="shajiquan", methods=["GET", "DELETE"])
# 为 endpoint="shajiquan" 指定 view function
app.view_functions['shajiquan'] = amihome


@app.route('/')
def miao():
    return "wu at: {}".format(flask.request.endpoint)


# 尝试取消注释
#app.view_functions['home'] = miao


if __name__ == '__main__':
    app.run(debug=True, port=8964)