import os
from glob import glob
from config import ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY

current_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_path, '.gitignore'), 'r', encoding='utf8') as file:
    exclude = set(file for file in file.read().split('\n'))

if os.name == 'nt':
    print("Удали windows")
    exit(-1)
folders = list(
    set([folder.replace('\\', '/').replace("app/", "").strip('/') for folder in glob('app/*/')]) - exclude
)


apps = [
    folder.replace("/", ".") for folder in folders
]

tortoise_apps = {
    folder: {
        'models': [f'app.{folder.replace("/", ".")}.models']
    }
    for folder in folders
}
print(tortoise_apps, folders)

PROD_TORTOISE_ORM = {
    'connections': {'default': f'sqlite://{current_path}/db/prod/db.sqlite3'},
    'apps': tortoise_apps,
    # 'apps': {'models': model_paths},
}

TEST_TORTOISE_ORM = {
    'connections': {'default': f'sqlite://{current_path}/db/test/db.sqlite3'},
    'apps': tortoise_apps,
    # 'apps': {'models': model_paths},
}

# with open(os.path.join(current_path, 'secrets.json')) as file:
#     secrets = json.load(file)

SECRET_KEY = SECRET_KEY

ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES
ALGORITHM = ALGORITHM
CORS_ORIGINS = ['*']
IS_PROD = False #os.getenv('IS_PROD', False)
DOMAIN = 'localhost.local'# os.getenv('DOMAIN', 'set.prod.domain.com')

