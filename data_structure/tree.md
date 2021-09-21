> 자료구조

# 트리
트리는 데이터의 상하관계  
즉 데이터 사이의 높고 낮음을 나타내는 자료구조이다.  
배열이나 링크드 리스트는 계층적인 자료구조가 아니라 선형적인 자료구조이다.  
계층적 관계가 있는 데이터를 저장하기에는 적합하지 않은것이다.  
해시테이블도 마찬가지로 계층적 관계를 나타내기에는 적합하지 않다.  
트리를 통해서 이런 계층적 관계를 저장하고 활용해보자.  

링크드 리스트는 여러개의 데이터를 순서대로 저장해주는 선형적인 자료구조이다. 링크드 리스트에서는 노드라는 기본 단위의 데이터를 담고,   
하나의 노드가 저정하려는 데이터와 다음순서의 노드를 가리키는 레퍼런스를 갖는다. 각 노드가 다음 노드에 대한 레퍼런스를 갖고 있기 때문에, 여러 노드들 사이 앞과 뒤 라는 순서가 정해진다.
트리도 마찬가지로 여러개의 노드로 이루어져있다.  
트리는 하위 관계가 있는 노드들을 가리키는 레퍼런스를 갖는다. 특정노드의 하위 노드를 “자식 노드”라고 한다.  
하나의 노드가 더 많은 노드로 뻗어나가는 모습이 마치 나무와 같기 때문에 트리 라고 부른다.  
트리에서 가장 위에 있는 노드를 뿌리 노드 영어로는 root 노드라고 부른다. 이 노드에서부터 레퍼런스들을 따라가면 트리 안에 있는 모든 노드를 찾을 수 있다. 나무의 뿌리처럼 트리에 가장 시작점이기 때문에 루트라고 부르는 것이다.  

# 이진트리

각 노드가 최대 두개의 자식노드만 가질 수 있으면 이진 트리라고 한다.  
이진트리를 구현하는 노드 클래스를 만들기  
저장하려는 데이터와 자식 노드들에 대한 레퍼런스를 가져야 하니까 그 내용을 써준다.  

인스턴스 변수 data는 노드에 데이터를 저장합니다.  
파라미터로 받은 data 를 넣어줍니다.  
인스턴스 변수 left_child와 right_child는 각각 왼쪽 자식과 오른쪽 자식을 저장해준다.    
처음 생성될 때는 저장하려는 데이터만 가지고 있고 일단 자식 노드에 대한 레퍼런스는 가지고 있지 않은 것이다.  