
## ▶ 접근제어자

인스턴스 변수 앞에 private 이라는 접근 제어자를 써주면 
age 변수는 해당 클래스 안에서만 접근이 가능해진다.


## ✍ 변수 age는 숨기고 싶어서 private으로 설정하고,
setAge와 getAge는 다른 클래스에서도 사용하고 싶기 때문에 어디서든 접근 가능하게 해주는 **public**을 써준다.
아래의 메소드를 'setter' 메소드와 'getter' 메소드라고 부른다.
```java

Person.java
public class Person {
    private int age;

    public void setAge(int newAge) {
        if (newAge > 0) {
            age = newAge;
        }
    }

    public int getAge() {
        return age;
    }
}




Driver.java
public class Driver {
    public static void main(String[] args) {
        Person p1 = new Person();
        p1.setAge(28);
        p1.setAge(-10);
        System.out.println(p1.getAge());
    }
}

>>28
```

---

## ▶ 메소드 오버로딩

클래스 내에 같은 이름의 메소드를 2개 이상 정의할 수 있게 해주는 기능

```java
public class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }

    double add(double a, double b) {
        return a + b;
    }

    public static void main(String[] args) {
        Calculator c = new Calculator();

        System.out.println(c.add(2, 4));        // test 1
        System.out.println(c.add(2, 4, 8));     // test 2
        System.out.println(c.add(3.14, 2.54));  // test 3
    }
}
>>6
>>14
>>5.68
```

## ✍ 은행 계좌 예제



```java
public boolean deposit(int amount) {
    if (amount < 0 || amount > owner.getCashAmount()) {
        System.out.println("입금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
        return false;
    }

    balance += amount;
    owner.setCashAmount(owner.getCashAmount() - amount);

    System.out.println(amount + "원 입금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
    return true;
}

public boolean depositUSD(double amount, double exchangeRate) {
    return deposit((int) (amount * exchangeRate));
}

public boolean depositJPN(double amount, double exchangeRate) {
    return deposit((int) (amount * exchangeRate));
}
```
위의 depositUSD, depositJPN 메소드는 내용은 같은데,
메소드 이름만 다르게 여러개를 만드는 비효율적인 상황이 발생될 수 있다.


```java
public boolean deposit(double amount, double exchangeRate) {
    return deposit((int) (amount * exchangeRate));
}
```

---

