rsync --cvs-exclude -vr ../bicidade_backend barufi@bicidade.net:works/
rsync --cvs-exclude -vr ../frontend barufi@bicidade.net:works/
scp ../bicidade_backend/bemok/settings.production.py barufi@bicidade.net:works/bicidade_backend/bemok/settings.py
scp ../bicidade_backend/bicidade_uwsgi.production.ini barufi@bicidade.net:works/bicidade_backend/bicidade_uwsgi.ini

