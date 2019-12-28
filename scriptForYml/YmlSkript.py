import yaml
from pprint import pprint
from enterTheValue import *
import io 

def start_to_create(settingMode):
  
  with io.open('template.yml') as f:
      templates = yaml.safe_load(f)

  api_general_settings = {'TYPEORM_HOST': enter_the_host(),
                          'TYPEORM_USERNAME': set_some_value('username'),
                          'TYPEORM_PASSWORD': enter_the_password(),
                          'TYPEORM_DATABASE': set_some_value('database name')
                         }
  oauth_settings = {'CLIENT_ID': set_some_value('client ID'),
                    'CLIENT_SECRET': set_some_value('client secret'),
                    'AUTH_REDIRECT_URI': enter_the_redirect_uri()
                   }
  remote_repository_url = {'JISKEFET_API': 'https://github.com/SoftwareForScience/jiskefet-api.git',
                           'JISKEFET_UI': 'https://github.com/SoftwareForScience/jiskefet-ui.git'
                          }
  if settingMode=='y':
    local_Repo = {'use_local_repository': enter_yes_or_no('local repository', 0)}
    CERN_SSO = {'USE_CERN_SSO': enter_yes_or_no('CERN SSO', 1)}
    if CERN_SSO.get('USE_CERN_SSO')=='yes':
      CERN_registered_uri={'CERN_REGISTERED_URI': set_some_value('CERN registered uri')}
    api_optional_settings={'TEST_DB_HOST': enter_the_host(),
                           'TEST_DB_USERNAME': set_some_value('test DB name'),
                           'TEST_DB_PASSWORD': enter_the_password()
                          }
    templates.update({'jiskefet_api_optional_settings': api_optional_settings})
    templates.update(local_Repo)
    templates.update(CERN_SSO)
  templates.update({'jiskefet_api_general_settings': api_general_settings})
  templates.update({'jiskefet_oauth_settings': oauth_settings})
  templates.update({'remote_repository_url': remote_repository_url})
  with io.open('ansible.config.yml', 'w') as f:
    yaml.dump(templates, f)
