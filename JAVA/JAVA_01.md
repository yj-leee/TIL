
## JAVA 설치하기


[JAVA](https://www.oracle.com/index.html) 계정 가입
[다운로드 페이지](https://www.oracle.com/kr/java/technologies/javase/javase-jdk8-downloads.html)


## IntelliJ 설치하기

[Intelli](https://www.jetbrains.com/ko-kr/idea/download/#section=mac) 



## HelloWorld 출력하기

---
### Java 
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```
---

### C
```C
#include <stdio.h>

int main()
{
    printf("Hello\n");
    return 0;
}
```
---

### python 
```python
print("Hello")
```

---

C 언어는 객체 지향이 적용되지 않은 언어고
JAVA 와 python 은 객체지향이 적용된 언어이지만 python은 많은 내용이 생략되어 있는 반면
**JAVA 는 객체 지향의 개념이 강하게 드러나는 특징**이 있다


## Hello World 해석해보기

![](https://images.velog.io/images/yj-leee/post/1a8f1304-bf17-49fa-934f-d0ec1f0f0cc3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.09.20.png)

>### HelloWorld
내가 지은 Class의 이름

>### class
객체 지향 프로그래밍의 기본 단위


>### public
접근제어자
HelloWorld라는 클래스는 누구나 사용할 수 있는 공적인 클래스라는 의미
public 외에도 private, protected 등이 있다.

![](https://images.velog.io/images/yj-leee/post/0fcbeaf5-2b68-43c2-8766-4b433d6215bd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.17.31.png)

이 부분은 클래스 안에 위치한 메소드이다.

>### main
메소드의 이름
자바 프로그램을 실행하면 가장 먼저 main을 찾아서 실행시킨다.
main 앞에 있는 3개의 단어는 main 메소드의 특징을 설명해주고 항상 main과 함께 나오게된다.

>### public
main 메소드는 누구에게나 공개되어 있다.

>### static
static을 써주면 그 부분을 바로 실행 가능하게 만들어준다.
main은 가장 첫 번째로 실행되어야 하기 때문에, main 앞에는 항상 static을 붙이게 된다.

>### void
메소드는 필요에 따라 실행이 끝나고 어떤 값을 되돌려주기도 하는데, 되돌려줄 값이 무엇인지 미리 써주는것
void는 되돌려주는 값이 없다는 의미이다.
만약 실행이 끝나고 숫자형을 돌려줄 예정이면, void 대신 숫자를 의미하는 int를 쓴다.
메인 메소드는 보통 아무 것도 되돌려주지 않기 때문에 void를 붙여준다.

>### String[] args
메소드에 전달되는 파라미터
String[]은 문자열을 의미하고, 뒤에 있는 args는 변수 이름. 
즉, args라는 이름의 문자열 변수가 메소드에 전달된다는 뜻이 되는 것이다.

![](https://images.velog.io/images/yj-leee/post/3db3219d-ade9-4738-9af4-a29820df5f3b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.15.23.png)

>### System
자바에서 미리 직접 만들어둔 클래스입니다.
System 클래스는 말 그대로 입력, 출력 등 시스템에 관련된 기능들을 모아둔 클래스입니다.

>### out
System 클래스 안에 System.in, System.out, System.err 등으로 분리되어 있는데
그 중 out을 사용한다는 것

>### println()
print는 '출력하다' 라는 뜻이고, ln은 line의 줄임말.
괄호 안에 원하는 텍스트를 넣으면 출력해주고,
마지막에는 엔터를 치듯이 다음 줄(line)로 넘겨주는 역할을 한다.
println 역시 기능을 구현한 부분이기 때문에 메소드이다.
