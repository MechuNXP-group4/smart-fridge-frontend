from PIL import Image

item_name = [
    '蘋果',
    '高麗菜',
    '小黃瓜',
    '馬鈴薯'
]

item_images = [
    Image.open('assets/foods/apple.jpg'),
    Image.open('assets/foods/cabbage.jpg'),
    Image.open('assets/foods/cucumber.jpg'),
    Image.open('assets/foods/potato.jpg')
]

item_durability = [
    5,
    5,
    5,
    5,
]

item_cuisines = [
    '蘋果蛋沙拉、蘋果派、蘋果汁',
    '炒高麗菜',
    '小黃瓜炒甜椒、涼拌小黃瓜',
    '焗烤馬鈴薯、紅燒馬鈴薯',
]

item_handle = [
    '切塊泡水作為催熟劑、洗碗拿來去油汙',
    '切碎後作為有機肥料',
    '切塊後作為有機肥料',
    '拿去移除鐵鏽、清潔窗戶、去除衣物污漬',
]