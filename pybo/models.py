from pybo import db


class Question(db.Model):
    """_summary_
    Question 모델은 고유 번호(id), 제목(subject), 내용(content), 작성일시(create_date) 속성으로 구성
    
    db.Column() 괄호 안의 첫 번째 인수는 데이터 타입을 의미한다. 
    데이터 타입은 속성에 저장할 데이터의 종류를 결정한다. 
    db.Integer는 고유 번호와 같은 숫자값에 사용하고, db.String은 제목처럼 글자 수가 제한된 텍스트에 사용한다. 
    글 내용처럼 글자 수를 제한할 수 없는 텍스트는 db.Text를 사용한다. 
    작성일시는 날짜와 시각에 해당하는 db.DateTime을 사용했다.
    db.Column에는 데이터 타입 외에 다음과 같은 속성을 추가로 설정할수 있다.
    primary_key:  
        id 속성을 기본 키(Primary Key)로 만든다. 
        기본 키는 데이터베이스에서 중복된 값을 가질 수 없게 만드는 설정이다.
    nullable:
        nullable은 속성에 값을 저장할 때 빈값을 허용할지의 여부이다. 
    
    Args:
        db (_type_): _description_
    """
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    
    
    
class Answer(db.Model):
    """_summary_
    question_id:
    uestion_id 속성은 답변을 질문과 연결하기 위해 추가한 속성이다. 
    답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id 속성이 필요하다. 
    그리고 모델을 서로 연결할 때에는 위와 같이 db.ForeignKey를 사용해야 한다.
    db.ForeignKey의 첫 번째 파라미터 'question.id'는 question 테이블의 id 컬럼을 의미한다. (question 객체의 속성 id로 착각하지 말자.) 
    즉, Answer 모델의 question_id 속성은 question 테이블의 id 컬럼과 연결된다는 뜻이다.
    
    db.ForeignKey의 두 번째 파라미터 ondelete는 삭제 연동 설정이다. 
    즉, ondelete='CASCADE'는 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다는 의미이다.
    
    question:
    question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가했다. 
    위와 같이 db.relationship으로 question 속성을 생성하면 답변 모델에서 연결된 질문 모델의 제목을 answer.question.subject처럼 참조할 수 있다.
    db.relationship의 첫 번째 파라미터는 참조할 모델명이고 두 번째 backref 파라미터는 역참조 설정이다. 
    역참조란 쉽게 말해 질문에서 답변을 거꾸로 참조하는 것을 의미한다. 
    한 질문에는 여러 개의 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다. 
    예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다.
    
    Args:
        db (_type_): _description_
    """
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    
    