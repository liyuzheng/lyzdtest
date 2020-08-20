'''
Created on 2016年12月13日

@author: liyuzheng
'''


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lyz:Lyz190019@81.70.19.176:3306/customsconsulation?charset=utf8'


class TestingConfig(Config):
    TESTINT = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://lyz:Lyz190019@81.70.19.176:3306/customsconsulation?charset=utf8'


config = {'development': DevelopmentConfig, 'testing': TestingConfig}
