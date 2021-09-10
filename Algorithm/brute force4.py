"""
실습과제

강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 
정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.
그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.
함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.
예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 3의 건물이, 
3번 인덱스에 높이 2의 건물이, 5번 인덱스에 높이 4의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.
그러면 아래의 사진에 따라 총 1010 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠.
이번에는 파라미터 buildings로 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]가 들어왔다고 합시다. 
그러면 아래의 사진에 따라 총 66 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 6을 리턴하는 거죠.
이 정보를 기반으로, trapping_rain 함수를 작성해 보세요!
"""


def trapping_rain(buildings):
    # 가장 높은 값 구하기
    sort_buildings = sorted(buildings, reverse=True)
    height, weight = sort_buildings[0], sort_buildings[1]
    # 가장 높은 값의 인덱스 구하기
    height_index = buildings.index(height)
    weight_index = buildings.index(weight)
    temp = 0
    if weight_index < height_index:
        for i in range(weight_index + 1, height_index):
            temp = temp + buildings[i]
        return height * weight - temp
    elif weight_index > height_index:
        for i in range(height_index + 1, weight_index):
            temp = temp + buildings[i]
        return height * weight - temp


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
