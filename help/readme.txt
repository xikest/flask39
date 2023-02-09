1. 플라스크 서버 실행
2. 환경 변수에 플라스크 앱 설정: 실행할 파일이 있는 폴더로 이동 후 등록
3. 개발 서버를 디버깅 가능하도록 실행


> set FLASK_APP=pybo
> set FLASK_DEBUG=true
> flask run


ORM 라이브러리 설치 및 실행
>pip install flask-migrate
flask db init
flask db migrate
flask db upgrade

flask shell