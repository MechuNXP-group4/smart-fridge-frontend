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
    30,
    25,
    40,
    50,
]

item_cuisines = [
    '蘋果蛋沙拉、蘋果派、蘋果汁',
    '炒高麗菜',
    '小黃瓜炒甜椒、涼拌小黃瓜',
    '焗烤馬鈴薯、紅燒馬鈴薯',
]