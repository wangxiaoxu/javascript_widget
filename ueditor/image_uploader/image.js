/**
 * Created by JetBrains PhpStorm.
 * User: taoqili
 * Date: 12-01-08
 * Time: 下午2:52
 * To change this template use File | Settings | File Templates.
 */
var imageUploader = {},
    flashObj = null,
    postConfig=[];
(function () {
    var g = $G,
        ajax = parent.baidu.editor.ajax,
        maskIframe = g("maskIframe"); //tab遮罩层,用来解决flash和其他dom元素的z-index层级不一致问题
       // flashObj;                   //flash上传对象

    var flagImg = null, flashContainer;
    imageUploader.init = function (opt, callbacks) {
        activeFlash();
        createFlash(opt, callbacks);
        addOKListener();
    };
    imageUploader.setPostParams = function(obj,index){
        if(index===undefined){
            utils.each(postConfig,function(config){
                config.data = obj;
            })
        }else{
            postConfig[index].data = obj;
        }
    };

    function insertImage(imgObjs) {
        editor.fireEvent('beforeInsertImage', imgObjs);
        editor.execCommand("insertImage", imgObjs);
    }

    /**
     * 绑定确认按钮
     */
    function addOKListener() {
        dialog.onok = function () {
        	insertBatch();
        };
        dialog.oncancel = function () {
            hideFlash();
        }
    }

    function hideFlash() {
        flashObj = null;
        flashContainer.innerHTML = "";
    }


    /**
     * 插入多张图片
     */
    function insertBatch() {
        if (imageUrls.length < 1) return;
        var imgObjs = [],
            align = findFocus("localFloat", "name");

        for (var i = 0, ci; ci = imageUrls[i++];) {
            var tmpObj = {};
            tmpObj.title = ci.title;
            tmpObj.floatStyle = align;
            //修正显示时候的地址数据,如果后台返回的是图片的绝对地址，那么此处无需修正
            tmpObj.data_ue_src = tmpObj.src = editor.options.imagePath + ci.url;
            imgObjs.push(tmpObj);
        }
        insertImage(imgObjs);
        hideFlash();
    }

    /**
     * 找到id下具有focus类的节点并返回该节点下的某个属性
     * @param id
     * @param returnProperty
     */
    function findFocus(id, returnProperty) {
        var tabs = g(id).children,
            property;
        for (var i = 0, ci; ci = tabs[i++];) {
            if (ci.className == "focus") {
                property = ci.getAttribute(returnProperty);
                break;
            }
        }
        return property;
    }

    /**
     * 创建flash实例
     * @param opt
     * @param callbacks
     */
    function createFlash(opt, callbacks) {
        var i18n = utils.extend({}, lang.flashI18n);
        //处理图片资源地址的编码，补全等问题
        for (var i in i18n) {
            if (!(i in {"lang":1, "uploadingTF":1, "imageTF":1, "textEncoding":1}) && i18n[i]) {
                i18n[i] = encodeURIComponent(editor.options.langPath + editor.options.lang + "/images/" + i18n[i]);
            }
        }
        opt = utils.extend(opt, i18n, false);
        var option = {
            createOptions:{
                id:'flash',
                url:opt.flashUrl,
                width:opt.width,
                height:opt.height,
                errorMessage:lang.flashError,
                wmode:browser.safari ? 'transparent' : 'window',
                ver:'10.0.0',
                vars:opt,
                container:opt.container
            }
        };
        flashContainer = $G(opt.container);
        option = utils.extend(option, callbacks, false);
        flashObj = new baidu.flash.imageUploader(option);
    }

    function toggleFlash(show) {
        if (flashContainer && browser.webkit) {
            flashContainer.style.left = show ? "0" : "-10000px";
        }
    }

    function activeFlash(){
    	var body = g('local')
        body.style.zIndex = 200;
        //当切换到本地图片上传时，隐藏遮罩用的iframe
        toggleFlash(true);
        maskIframe.style.display = "none";
        //处理确定按钮的状态
        if (selectedImageCount) {
            dialog.buttons[0].setDisabled(true);
        }
    }
})();
