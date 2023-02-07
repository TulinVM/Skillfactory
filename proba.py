# with open('info.json') as user_file:
#     file_contents = user_file.read()
#
# print(file_contents)

def load_info():
    with open("info.json") as info_file:
        info = json.load(info_file)
    # with open("info.json") as user_file:
    #     info = user_file.read()

    return info
info = load_info()
print(info)