# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2021/11/21
Last Modified: 2021/11/21
Description: 
"""
import os

from flask import Flask


def create_app(test_config=None):
    """应用工厂函数"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),)

    if test_config is None:
        # 加载正式环境
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 加载测试环境
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, world'

    return app


if __name__ == '__main__':
    create_app()
