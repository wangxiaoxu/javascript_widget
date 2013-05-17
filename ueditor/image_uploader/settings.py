#==================================
# 富文本编辑器上传图片功能配置
#==================================
# 工具栏样式，可以添加任意多的模式
TOOLBARS_SETTINGS = {
    "mini":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','insertimage','attachment']],
    "normal":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','removeformat', 'formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','insertimage', 'emotion','attachment', '|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']],
}
# 允许上传的图片类型
UPLOAD_IMAGES_SETTINGS = {
    "allow_type":"jpg,bmp,png,gif,jpeg",         #文件允许格式
    "path":"",
    "max_size":0                                #文件大小限制，单位KB,0不限制
}
# 允许上传的附件类型
UPLOAD_FILES_SETTINGS = {
    "allow_type":"zip,rar,doc,docx,xls,xlsx,ppt,pptx,swf,dat,avi,rmvb,txt,pdf",         #文件允许格式
    "path":"",
    "max_size":0                               #文件大小限制，单位KB,0不限制
}
# 图片管理器地址
IMAGE_MANGER_SETTINGS = {
    "path":""                  #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
}
UEditorSettings = {
    "toolbars":TOOLBARS_SETTINGS,
    "images_upload":UPLOAD_IMAGES_SETTINGS,
    "files_upload":UPLOAD_FILES_SETTINGS,
    "image_manager":IMAGE_MANGER_SETTINGS,
}


#========================================
# 直播间后台使用的配置
#========================================

# 后台上传图片的配置
IMAGE_ZOOM_URL = "http://img.m.sohuno.com/dy/1/0/"
UPLOAD_FILE_URL = 'http://s1.rr.itc.cn/'
UPLOAD_FILE_ROOT = '/data/leofs/bms/'