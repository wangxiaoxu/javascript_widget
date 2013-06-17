(function($){
	//ADDON_CHOICES = ((0x0, u'无扩展'), (0x1, u'篮球比赛'), (0x2, u'足球比赛'))
	
	var addonMap = {
		0x1: 'basketballgame_set-group', 
		0x2: 'footballgame_set-group'
	}
	
	//根据情况渲染扩展
	function renderAddon(){
		_hideAddon();
		var addon = $('#id_addon').val();
		for(var key in addonMap){
			if(key & addon){
				$('#'+addonMap[key]).show();
			}
		}
	}
	
	//隐藏所有扩展
	function _hideAddon(){
		for(var key in addonMap){
			$('#'+addonMap[key]).hide();
		}
	}
	
	//根据情况渲染嘉宾元素
	function renderGuests(){
		_hideGuests();
		var templateSelect = $('#id_template option:selected');
		templateSelect.each(function(){
			if($(this).text()=='访谈'){
				$('.field-guests').show();
			}
		});
	}
	
	//隐藏嘉宾元素
	function _hideGuests(){
		$('.field-guests').hide();
	}
	
	
	function renderAllElement(){
		renderAddon();
		renderGuests();
	}
	
	$(document).ready(function(){
		renderAllElement();
		$('#id_addon').change(function(){
			renderAddon();
		});
		$('#id_template').change(function(){
			renderGuests();
		});
	});
	
	
	
})(django.jQuery);