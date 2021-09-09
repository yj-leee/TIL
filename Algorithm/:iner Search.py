"""
'선형 탐색(Linear Search)'   
알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다.  
선형 탐색이란, 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.  

파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요. 
0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해 주면 됩니다.

element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.
"""


def linear_search(element, some_list):
    for idx in range(len(some_list)):
        if some_list[idx] == element:
            return idx


print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
