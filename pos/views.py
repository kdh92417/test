import pyodbc
import json

from django.shortcuts import render
from django.http      import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=softstonedevdatabase01.database.windows.net;'
                      'DATABASE=softstonedevdatabase01;'
                      'UID=Devssdbadm;'
                      'PWD=Softstonedbadm1!;')
cursor = conn.cursor()

def index(request):
    return render(request, 'pos/index.html')

def getData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)
        cursor.execute(f"SELECT * FROM TEST_TJS_EMPLOYEE WHERE EMP_NM='{data['name']}';")
        row = cursor.fetchone()

        return JsonResponse(list(row), safe=False)

def update_nick_name(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cursor.execute(f"UPDATE TEST_TJS_EMPLOYEE SET NICK_NM = '{data['name']}' WHERE EMP_NM='{data['nick_name']}';")

        return JsonResponse({'message' : 'success'}, status=200)

def insert_person(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cursor.execute(
            f"DECLARE @name NVARCHAR(40); "
            f"SET @name = CONVERT(NUMERIC, (SELECT TOP (1) EMP_NO FROM TEST_TJS_EMPLOYEE ORDER BY CONVERT(NUMERIC, EMP_NO) DESC)) + 1; "
            f"INSERT INTO TEST_TJS_EMPLOYEE (EMP_NO, EMP_NM) VALUES(CONVERT(CHAR(40), @name), '{data['name']}');")

        cursor.commit()
        return JsonResponse({'data' : 'success'}, status=201)
    else:
        JsonResponse({'message' : 'Wrong Http Method'}, status=405)

def delete_person(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        cursor.execute(f"DELETE FROM TEST_TJS_EMPLOYEE WHERE EMP_NM='{data['name']}'")
        cursor.commit()
        return JsonResponse({'data': 'success'}, status=201)
    else:
        JsonResponse({'message': 'Wrong Http Method'}, status=405)