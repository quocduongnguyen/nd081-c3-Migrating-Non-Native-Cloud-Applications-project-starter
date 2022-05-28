import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="duongnq9-project3-server.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="postgres" #TODO: Update value
    POSTGRES_PW="Fsoft@12345"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://duongnq9-project3-service-bus.servicebus.windows.net/;SharedAccessKeyName=FullAccessKey;SharedAccessKey=X3K8mpPwBhz8zd76TpRe6Ryn98zAHrb+Ju7NjcSWHBI=;EntityPath=notificationqueue' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'quocduong.th10b.mta@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    POSTGRES_URL="duongnq9-project3-server.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="postgres@duongnq9-project3-server" #TODO: Update value
    POSTGRES_PW="Fsoft@12345"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://duongnq9-project3-service-bus.servicebus.windows.net/;SharedAccessKeyName=FullAccessKey;SharedAccessKey=X3K8mpPwBhz8zd76TpRe6Ryn98zAHrb+Ju7NjcSWHBI=;EntityPath=notificationqueue' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'quocduong.th10b.mta@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class ProductionConfig(BaseConfig):
    DEBUG = False