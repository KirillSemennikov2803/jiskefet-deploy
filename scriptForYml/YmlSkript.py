import yaml
from pprint import pprint
from enterTheValue import *
def startToCreate():
  host = enterTheHost()
  username = enterTheName()
  password = enterThePassword()
  db = enterTheDBName()
  clientId = enterTheClientId()
  clientSecret = enterTheSecret()
  redirect = enterTheRedirectUri()
  api_general_settings = {'TYPEORM_HOST': host, 'TYPEORM_USERNAME': username, 'TYPEORM_PASSWORD': password, 'TYPEORM_DATABASE': db}
  oauth_settings = {'CLIENT_ID': clientId, 'CLIENT_SECRET': clientSecret, 'AUTH_REDIRECT_URI': redirect}
  remote_repository_url = {'JISKEFET_API': 'https://github.com/SoftwareForScience/jiskefet-api.git', 'JISKEFET_UI': 'https://github.com/SoftwareForScience/jiskefet-ui.git'}
  with open('template.yml') as f:
      templates = yaml.safe_load(f)
  templates.update({'jiskefet_api_general_settings': api_general_settings})
  templates.update({'jiskefet_oauth_settings': oauth_settings})
  templates.update({'remote_repository_url': remote_repository_url})
  with open('ansible.config.yml', 'w') as f:
      yaml.dump(templates, f)
    