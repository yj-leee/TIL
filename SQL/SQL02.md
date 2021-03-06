
SQL문 쓰는 규칙에 대해서
세미콜론의 의미
하나의 SQL문을 종결하는 단위이다.

대소문자의 구분
MySQL에 기본으로 내장된 키워드들('예약어라고 부른다') 대문자로 써주고, 나머지 부분은 소문자로 써준다.
소문자로 바꾸고 실행해도 실행은 잘 되지만 가독성을 위해 꼭 대문자로 쓰는 습관을 들이자.
워크벤치에서 테이블 정보 보면 아래와 같은 문구가 있는데 이 부분에서 ci 는 대소문자를 구별하지 않는다는 뜻이다.


설정에 상관 없이 늘 대소문자를 구분하도록 하는 법? >>BINARY<< 써주기

SELECT * FROM member.test WHERE sentence LIKE BINARY '%g%';
BINARY 0과 1로 된이라는 이진의라는 뜻으로 해당 0과 1이 정확히 일치하는 것을 찾는다.
소문자와 대문자 G는 같은 알파벳이지만 컴퓨터에서 이진수로 저장될 때는 다른 값이기 때문에 구분이 가능하다.

데이터베이스의 이름과 테이블 이름
테이블 이름 뒤에 점을 붙이고 그 다음에 테이블 이름을 써준다.
그 이유는 실무에서 서로 다른 데이터베이스에 같은 이름의 테이블이 존재할 수도 있기 때문이다.
이거는 상황에 맞춰서 쓰면 된다
SELECT * FROM member.age 
워크벤치에서 글자 크기 조정하기
MySQLWorkbench Proferences
Fonts 탭에서 알맞게 조절한다.

뭐 귀찮지만 한번 나갔다 들어와준다.
SELECT WHERE BETWEEN A AND B
BETWEEN A and B
NOT BETWEEN A AND B

DATE 형식일 때
sign_up_day > '2019-01-01'
sign_up_day BETWEEN '2018-01-01' AND '2018-12-31'

문자열 패턴 매칭
LIKE '서울%'
서울로 시작하고 그 뒤로는 임의의 길이의 문자를 가진 row 검색

LIKE '%고양시%'
고양시를 포함한 모든 row 검색

같지 않음
(!= , <>)

이중에 있는
age IN (20, 30)
나이가 20이거나 30이라는 뜻

LIKE 'C___@%'
C라는 글자 뒤에 길이가 3개이고 골뱅이를 포함하며 그 뒤로는 임의의 길이의 문자를 가진 row 검색

함수 활용하기
DATE

YEAR(birthday) = '1992';
MONTH(sign_up_day) IN (6,7,8);
DAYOFMONTH(sign_up_day) BETWEEN 15 AND 31;

DATE 연산
SELECT email, sign_up_day, DATEDIFF sign_up_day, '2019-01-01') FROM member

CUREDATE() 오늘 날짜 함수
SELECT email, sign_up_day, DATEDIFF sign_up_day, CURDDATE()) FROM member

DATE_ADD, DATE_SUB

DATE_ADD(sign_up_day, INTERBAL 300DAY) FROM member
DATE_ADD(sign_up_day, INTERBAL 150DAY) FROM member

