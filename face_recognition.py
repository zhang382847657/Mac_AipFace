# 引入人脸识别SDK
from aip import AipFace
# 设置常量
APP_ID = '10133104'
API_KEY = 'ydyMeUKxiPvSvtolMKAmmmj8'
SECRET_KEY = 'GmTbtjLXHwtQlPwx4enzSf7wsyUYWMQh'

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义用户人脸检测参数变量
# options = {
#     'max_face_num': 1,
#     'face_fields': "age,beauty,expression,faceshape",
# }

# 定义用户人脸识别参数
options = {
    'user_top_num': 1,
    'face_top_num': 1,
}



# 注册一个新用户到人脸识别库中
# result = aipFace.addUser(
#     'uid_1',
#     'anglebaby',
#     'group_user',
#     get_file_content('image/anglebaby_1.jpg')
# )

# 用户人脸识别
result = aipFace.identifyUser(
    'group_user',
    get_file_content('image/anglebaby_2.jpg'),
    options
)

print(result)

