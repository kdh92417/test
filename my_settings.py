DATABASES = {
    'default' : {
        'ENGINE'   : 'sql_server.pyodbc',
        'NAME': 'softstonedevdatabase01',
        'HOST': 'softstonedevdatabase01.database.windows.net',    # DB IP ('localhost')
        'PORT': '1433',                 # DB PORT
        'USER': 'Devssdbadm',          # DB 접근 ID
        'PASSWORD': 'Softstonedbadm1!',   # DB 접근 password

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'unicode_results': True,
        }
    }
}

SECRET = {
    'secret' : '=9!qw&ke8=0x45k$fqywq^$dey&t3aeim-*v_cm%^luf&w%bc3'
}

ALGORITHM = ''