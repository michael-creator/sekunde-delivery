class Config:
    
      

      
      SECRET_KEY='SECRET_KEY=c037919dd5689b'
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dominic@localhost/sekunde'
    
    
class ProductionConfig(Config):
    pass
    
class DevelopmentConfig(Config):
    
    DEBUG = True
config_options = {

'production':ProductionConfig,
'development': DevelopmentConfig,
}