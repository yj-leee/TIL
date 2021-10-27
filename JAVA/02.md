## ✍ 변수 선언

>✓ 자료형 + 변수이름
 ```java
int a;
String s;
```
>✓ 변수 선언하고 값 넣어주기
```java
int age;
age = 27;
```

## ▶ 규칙

1. 대소문자 구분

2. 숫자로 시작할 수 없다

3. 밑줄(_)과 달러 표시($)를 사용할 수는 있지만, 사용하지 않는 것이 좋다

4. '카멜 케이스(camelCase)'

---

## ✍ 자료형


![](https://images.velog.io/images/yj-leee/post/02e98f0b-a88e-4762-911e-4a2e03ae2165/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.42.54.png)

![](https://images.velog.io/images/yj-leee/post/89c7fb1c-ca6c-420a-b88f-eb24f8af834e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.43.01.png)

**✓ 숫자형
**`byte`, `short`, `int`, `long`


**✓ 정수형
**정수를 입력하면 기본적으로 `int`로 간주

**✓ 소수형
**`float`, `double`

>❓차이 
float과 double은 둘다 소수형을 담지만 정밀도(Precision) 혹은 정확도에 차이가 있다. double이 더 정밀하게 값을 보관하므로 자바에서는 double을 소수형의 기본으로 한다. 정수를 입력하면 기본적으로 int로 인식되듯이, 소수를 입력하면 기본적으로 double로 인식된다.

만약 float를 쓰고 싶으면 소수를 쓰고, 뒤에 f를 붙인다.

```java
float f = 3.14f;

```
**✓  글자
**`char`, `String`

>❓  char : 글자(Character) 하나를 담는 자료형

**✓  불린
**`true`, `false`

**✓ 문자열
**String은 기본 자료형이 아니라 Class이다. 
"" 큰따움표를 사용


---

## ✍ 연산



```java
String myString = "Hello " + "World!";
System.out.println(myString);
Hello World!
```
>❓문자열과 숫자를 더하면 숫자가 저절로 문자열로 바뀌고, 
문자열과 불린을 더하면 불린이 저절로 문자열로 바뀐다.

```java
System.out.println("데카르트는 \"나는 생각한다. 고로 존재한다.\"라고 말했다.");
```

>❓ 이스케이프 문자에는 "\n", "\"", "\'" 정도만 자주 쓸 것.
Escape Sequence	Description
\t	탭
\b	백스페이스
\n	줄 바꿈 (new line)
\r	줄 바꿈 (carriage return)
\f	폼 피드(form feed)
'	작은 따옴표
"	큰 따옴표
\	역슬래쉬
줄 바꿈을 위해서 맥에서는 "\n", 윈도우즈에서는 "\r\n"을 사용



```java
System.out.println(9 / 5);
> 1
```
>❓서로 다른 자료형의 연산은 랭크가 더 높은 자료형의 결과값을 갖는다.
소수형은 정수형보다 랭크가 높기 때문에 소수형과 정수형 간의 연산의 결과값으로는 소수형이 나온다.


>❓ 단항 연산자
System.out.println(-a);  // 양, 음 부호가 바뀜
System.out.println(++a); // a에 1을 추가
System.out.println(--a); // a에 1을 감소


---
## ✍ 형 변환

![](https://images.velog.io/images/yj-leee/post/ba895efb-a29e-4e61-8c28-5aceeb8843da/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.56.56.png)

바꾸고자 하는 형(to)이 기존의 형(from)보다 넓은 데이터를 담을 수 있는 자료형일 경우 
특별한 처리 없이 형을 변환할 수 있다.
```java
int a = 36;
double b = a;     // int to double

short c = 17;
long d = c;       // short to long

float e = 3.14f;
double f = e;     // float to double

타입 캐스팅 (Type Casting)
값(혹은 변수) 앞에 (자료형)(예: (int) x)
int a = 3;
double b = (double) a;
long c = (long) a;

System.out.println(b);
System.out.println(c);
3.0
3

더 큰 랭크의 값을 더 작을 랭크의 변수에 담는 것도 가능하지만 
데이터의 손실이 있을 수 있다!
double pi = 3.14;
int myInt = (int) pi; // 데이터 손실 (소수 부분)
System.out.println(myInt);
3
```

---

## ✍ 조건문

if문

```java
int x = 10;
int y = 1;

if (x != 10 || x % 2 != 0) {
    System.out.println(x);
} else if (y == 1) {
    System.out.println(y);
} else {
    System.out.println(x + y);
}
```


switch문
```java
switch (score / 10) {
    case 10:
        grade = "A+";
        break;
    case 9:
        grade = "A";
        break;
    case 8:
        grade = "B";
        break;
    case 7:
        grade = "C";
        break;
    case 6:
        grade = "D";
        break;
    default:
        grade = "F";
        break;
}


switch (grade) {
    case "A+":
    case "A":
    case "B":
        System.out.println("참 잘했어요!");
        break;
    case "C":
    case "D":
        System.out.println("조금만 더 노력해 볼까요?");
        break;
    case "F":
        System.out.println("Fail입니다.");
    default:
        System.out.println("다시 수강해주세요.");
        break;
}

```

while문

```java
int sum = 0, i = 1;

while (sum < 10000) {
    sum += i;
    i++;
}

System.out.println(sum);
System.out.println(i - 1);


int sum = 0, i = 1;

while (true) {
    if (sum >= 10000) {
        break;
    }

    sum += i;
    i++;
}

System.out.println(sum);
System.out.println(i - 1);
```

for문
```java
for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}
```


---


## ✍ 배열

(1) 선언과 동시에 빈 배열 생성

int[] intArray = new int[5]; // 크기 5의 빈 배열


(2) 선언 후, 배열 생성

int[] intArray;
intArray = new int[5]; // 크기 5의 빈 배열

(3) 리터럴로 생성

int[] intArray = {1, 2, 3, 4, 5};
이렇게 하면 5개의 원소가 있으니까 intArray는 자동으로 크기 5의 배열이 생성.
이 방식은 변수를 정의할 때만 사용이 가능


>❓ 런타임?
런타임이란, 코드 작성 시점이 아니라 실제 실행될 때를 뜻한다. intArray[5] = 6;을 적었을 때는 문법적으로 오류가 없다. 그런데 실제 실행을 해서 접근하려고 할 때 에러가 생긴다.


값을 대입할 때, 일반적인 변수와 사용법 동일하다.
intArray[0] = 1;
intArray[1] = 2;


## 앨리어싱 (Aliasing)

int[] arr1 = {1, 2, 3, 4, 5};
int[] arr2 = arr1;

arr1[0] = 100;
System.out.println(arr2[0]);
100


arr1을 arr2에 새롭게 복사하고 싶으면?
clone 메소드 사용
int[] arr1 = {1, 2, 3, 4, 5};
int[] arr2 = arr1.clone();

arr1[0] = 100;
System.out.println(arr1[0]);
System.out.println(arr2[0]);
100
1


## for-each문
```
for (int i : intArray) {
    System.out.println(i);
}
```
이렇게 쓰면, 처음에 수행 부분으로 들어갈 때 i는 intArray의 0번 인덱스의 값(원소)을 갖게 되고, 그 다음 들어갈 때는 1번 인덱스의 값(원소)을 갖게 되고... 이런 식으로 배열의 마지막 값(원소)까지 갖는다.

```
for (double i : intArray) {
    System.out.println(i);
}
```


```java

String[] fruitsArray = new String[5];

fruitsArray[0] = "딸기";
fruitsArray[1] = "당근";
fruitsArray[2] = "수박";
fruitsArray[3] = "참외";
fruitsArray[4] = "메론";

for (String fruit : fruitsArray) {
    System.out.println(fruit);
}
딸기
당근
수박
참외
메론
```
