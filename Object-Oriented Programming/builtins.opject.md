


# 상속

파이썬에서 모든 클래스는 builtins.opject 클래스를 자동으로 상속받는다.  
상속이란 두 클래스 사이에 부모 자식 관계를 설정하는 것이다.  
자식 클래스는 부모 클래스의 모든 변수와 메소드를 물려 받을 수 있다.  

장점 코드의 중복을 없애줄 수 있다.

```
# isinstance

isinstance(검사할 인스턴스의 이름, 기준 클래스의 이름)  
# 함수의 첫번째 파라미터로 들어온 이름이 기준 클래스의 인스턴스인지를 알려준다.  

```

```
# issubclass

issubclass(검사할 클래스의 이름, 기준 클래스의 이름)
# 첫번째 파라미터로 들어온 검사할 클래스의 이름이 기준 클래스의 자식 클래스인지를 알려주는 함수

```

# 오버라이딩

자식 클래스가 부모 클래스로부터 물려받은 내용을 자신에 맞게 변경하는것  

```
# super
# 부모 클래스의 메소드를 호출할 수 있다.

class Cashier(Employee):
  def __init(selt, name, wage, number_sold):
    super().__init__(name, wage)
    self.number_sold = number_sold

```






