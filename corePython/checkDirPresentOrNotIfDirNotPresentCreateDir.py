import os.path

path = "C:/Worldline/TEST_JAVA_PYTHON"
isExist = os.path.exists(path)
print(isExist)
if not isExist:
    os.makedirs(path)
    isExist = os.path.exists(path)
    print("created dir")
    print(isExist)

path = "C:/Worldline/TEST_PYTHON"
if os.path.isdir(path):
    os.makedirs(path)