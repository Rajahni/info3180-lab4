import os

def get_uploaded_images():
    uploads_folder = './uploads'  # Change this to the path of your uploads folder
    filenames = []
    for filename in os.listdir(uploads_folder):
        if os.path.isfile(os.path.join(uploads_folder, filename)):
            filenames.append(filename)
    print(filenames)
    return filenames

#     # rootdir = os.getcwd()
#     # print(rootdir)
#     # for subdir, dirs, files in os.walk(rootdir + uploads_folder):
#     #     for file in files:
#     #         filenames.append(file)
#     # print(filenames)
# def get_uploaded_images():
#     filenames = []
#     rootdir = os.getcwd()
#     print(rootdir)
#     for subdir, dirs, files in os.walk(rootdir + app.config['UPLOAD_FOLDER']):
#         for file in files:
#             filenames_lst = os.path.join(subdir,file)
#             filenames.append(os.path.basename(filenames_lst))
#     return filenames    

if __name__ == "__main__":
   get_uploaded_images()