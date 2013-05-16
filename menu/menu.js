(function($){
	/**
	 * 菜单式下拉列表
	 * 参数:
	 * options = {
	 * 		element: 点击的元素(可以使按钮或者input表单等),
	 * 		url: 接口url,
	 * 		
	 * }
	 */
	var Menu = function(options) {
		var _this = this;
		this.element = options.element;
	    this.menuNode = $("<div class='menu' style='position: absolute; height: 440px;'></div>"),
	    this.ul = $("<ul style='margin-top: 0px;'></ul>");
	    this.arr = [0];
	    $.extend(this, options);
	    this.init();
	}
	Menu.prototype = {
	    //在这里初始化对象的变量
	    init: function() {
	        this.bindEvent();
	    },
	    bindEvent: function() {
	    	var _this = this;
	        //绑定document点击事件
	        $(document).click(function(event) {
	            var targetDom = event.target;
                if($.contains(_this.element.parent()[0], targetDom)){
                }else {
                    _this.hide();
                }
	        });
	        this.element.click(function(){
	        	_this.getRootData();
	        });
	    },
	    show: function(){
	    	$('.menu', this.element).show();
	    },
	    hide: function(){
	    	$('.menu', this.element).hide();
	    },
	    getRootData: function() {
	    	var _this = this;
	    	this.element.unbind('click');
	    	this.element.click(function(){
	        	_this.show();
	        });
	    	
	    	var url = _this.url + "0/";
	        $.getJSON(url, function(json) {
	            var data = $.parseJSON(json.data);
                _this.element.append(_this.menuNode);
	            _this.menuNode.append(_this.ul);
	            for(var i=0; i<data.length; i++){
	            	$(".menu > ul", _this.element).append(_this.createANode(data[i]));
	            }
	        });
	        
	    },
	    //创建node，并且添加时间监听
	    createANode: function(nodeInfo, rootNode){
	        var icon_name,
	            _this = this;
	        if(nodeInfo.have_children == false){
	            var parentNode = $('<li class=""></li>');
	            var html = '<a value = ' + nodeInfo.id + '>' + nodeInfo.name + '</a>';
	            parentNode.append(html);
	        }else{
	            var parentNode = $('<li class=""></li>'),
	                html = '<a value = ' + nodeInfo.id + ' class="fly">'+ nodeInfo.name + '</a><ul style="display: none;"></ul>';
	            parentNode.append(html);
	        }
	        $("a", parentNode).hover(function(e){
                e.stopPropagation();
                var nodeId = parseInt(e.target.getAttribute("value"));
                var url = _this.url + nodeId + "/";
                var hovernode = $(this);
                if($.inArray(nodeId, _this.arr)==-1 && nodeId){
                    $.getJSON(url, function(json){
                        _this.arr.push(nodeId);
                        var nodes = $.parseJSON(json.data);
                        console.info(nodes);
                        for(var j=0; j<nodes.length; j++){
                            _this.createANode(nodes[j], parentNode);
                        }
                    });
                }
                if($(this).parent().children('ul')){
                	$(this).parent().children('ul').show();
                }
                $(this).parent().siblings().find('ul').hide();
            }, function(){
                $(this).siblings().children().find('ul').hide();
                $(this).parent().siblings().find('ul').hide();
            });
	        $('a', parentNode).click(function(e){
	            e.stopPropagation();
	            var value = $(this).attr('value')
	            var name = $(this).html();
	            _this.hide();
	            _this.nodeClickCallback(name, value)
	        });
	        if(rootNode){
	            rootNode.children().last().append(parentNode);
	        } else{
        		return parentNode;
	        }
	    },
	    nodeClickCallback: null
	}
	
	
	window.Menu = Menu;
})(jQuery);

