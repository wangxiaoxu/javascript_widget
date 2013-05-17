#==================================
# ���ı��༭���ϴ�ͼƬ��������
#==================================
# ��������ʽ���������������ģʽ
TOOLBARS_SETTINGS = {
    "mini":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','insertimage','attachment']],
    "normal":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','removeformat', 'formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','insertimage', 'emotion','attachment', '|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']],
}
# �����ϴ���ͼƬ����
UPLOAD_IMAGES_SETTINGS = {
    "allow_type":"jpg,bmp,png,gif,jpeg",         #�ļ������ʽ
    "path":"",
    "max_size":0                                #�ļ���С���ƣ���λKB,0������
}
# �����ϴ��ĸ�������
UPLOAD_FILES_SETTINGS = {
    "allow_type":"zip,rar,doc,docx,xls,xlsx,ppt,pptx,swf,dat,avi,rmvb,txt,pdf",         #�ļ������ʽ
    "path":"",
    "max_size":0                               #�ļ���С���ƣ���λKB,0������
}
# ͼƬ��������ַ
IMAGE_MANGER_SETTINGS = {
    "path":""                  #ͼƬ��������λ��,���û��ָ����Ĭ�ϸ�ͼƬ·���ϴ�һ��
}
UEditorSettings = {
    "toolbars":TOOLBARS_SETTINGS,
    "images_upload":UPLOAD_IMAGES_SETTINGS,
    "files_upload":UPLOAD_FILES_SETTINGS,
    "image_manager":IMAGE_MANGER_SETTINGS,
}


#========================================
# ֱ�����̨ʹ�õ�����
#========================================

# ��̨�ϴ�ͼƬ������
IMAGE_ZOOM_URL = "http://img.m.sohuno.com/dy/1/0/"
UPLOAD_FILE_URL = 'http://s1.rr.itc.cn/'
UPLOAD_FILE_ROOT = '/data/leofs/bms/'