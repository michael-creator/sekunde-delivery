class Config:

      SECRET_KEY='SECRET_KEY=c037919dd5689b'
    
    
class ProductionConfig(Config):
    pass
    
class DevelopmentConfig(Config):
    
    DEBUG = True
config_options = {

'production':ProductionConfig,
'development': DevelopmentConfig,
}