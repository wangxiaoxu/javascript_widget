(function($){
	/**
	 * 上传组件
	 * 参数:
	 * options = {
	 * 		id: 被绑定元素id(按钮元素)
	 * 		url: 上传路径
	 * 		directory: 上传目录
	 * 		allow_types: 允许上传的类型(['jpg', 'png', 'gif', 'bmp', 'jpeg'])
	 * 		preuploadCallback: 上传前的回调函数
	 * 		uploadSuccessCallback: 上传成功的回调函数
	 * 		uploadErrorCallback: 上传失败的回调函数
	 * }
	 */
	var Uploader = function(options){
		for(key in options){
			this[key] = options[key];
		}
		this.init();
	}
	
	Uploader.FILE_INPUT_ID_PREFIX = 'file_input_id_';
	
	Uploader.prototype = {
		init: function(){
			var _this = this;
			var file_input_id_count = $('[id^="' + Uploader.FILE_INPUT_ID_PREFIX + '"]').length;
			this.file_input_id = Uploader.FILE_INPUT_ID_PREFIX + (file_input_id_count + 1);
			
			var uploaderHTML = '<input id="' + this.file_input_id + '" type="file" style="position:relative; z-index:-999; width: 0px; display:none;" />';
		    $(uploaderHTML).insertAfter("#" + this.id);
		    //点击按钮元素，模拟触发点击file input元素
		    $("#" + this.id).click(function(){
		    	console.info($("#" + _this.file_input_id).length);
		        $("#" + _this.file_input_id).trigger("click");
		    });
			setTimeout(function(){
				_this.init_upload();
			}, 50);
		    
		},
		init_upload: function(){
			var _this = this;
			//querySelector一个选择器，IE浏览器还不支持。
	        document.querySelector('#' + this.file_input_id).onchange = function(e) {
	        	var _this2 = this;
	            //获取input type=file上上传的文件
	            var files = this.files;
	
	            for(var i=0, len = files.length; i < len; i++) {
	                var file = files[i];
                    if(!_this.checkFileType(file)){
                        return;
                    }

                    if(!_this.checkFileSize(file)){
                        return;
                    }
					
                    if(_this.preuploadCallback){
                    	var reader = new FileReader(),
                    		name = file.name;
	                    reader.onload = function() {
	                        image_base64 = this.result; // 只取一个图片
	                        _this.preuploadCallback(image_base64);
	                    };
	                    reader.readAsDataURL(file);	
                    }

                    var formData = new FormData();
                    for (var i = 0, file; file = files[i]; ++i) {
                        formData.append("Filedata", file);
                        formData.append('directory', _this.directory);
                    }
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', _this.url, true);
                    (function(file){
                        xhr.onload = function(e) {
                            _this2.value = ''; // 将原有图片记录清空
                            console.info($.trim(this.responseText));
                            var data = eval("("+$.trim(this.responseText)+")");
                            if(data.status==0){
                                _this.uploadSuccessCallback(data.data.urls);
                            }else{
                            	_this.uploadErrorCallback();
//                                alert("图片上传失败!");
                            }
                        };
                    })(files[0]);
                    xhr.send(formData);  // multipart/form-data
	            }
	        }
		},
		checkFileType: function(file){
			var file_type = file.type.toLowerCase();
            if($.inArray(file_type, this.allow_types)){
                return true;
            }else{
            	alert('图片类型必须为' + allow_types.join('、') + '格式!');
				_this.value = ''; // 将原有图片记录清空
                return false;
            }
		},
		checkFileSize: function(file){
			if(file.size <= 8388608){   // 1024*1024*8
	        	return true;
			}else{
				alert("图片大小必须小于8M！");
	        	_this.value = ''; // 将原有图片记录清空
				return false;				
			}
		},
		preuploadCallback: null,
		uploadSuccessCallback: null,
		uploadErrorCallback: null
	}
	
	
	window.Uploader = Uploader;
})(jQuery);
