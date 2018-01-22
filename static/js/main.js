window.onload = function(){
	var floatElement = document.getElementById("floatElement");
	block_width = floatElement.parentElement.offsetWidth;
	coord = floatElement.getBoundingClientRect();
	top_coord = document.getElementById("head").getBoundingClientRect().bottom + 10 + pageYOffset;
	
	window.onscroll = function(){scroll_func(block_width)}

	function scroll_func(parent_width){

		var floatElement = document.getElementById("floatElement");
		
		 if (document.body.scrollTop > top_coord || document.documentElement.scrollTop > top_coord) {
       			floatElement.style.position = "fixed";
       			floatElement.style.top = "0";
       			floatElement.style.left = coord.left;
       			floatElement.style.width = parent_width + 'px';

       		}
       	else{
       		floatElement.style.position = "static";
       			floatElement.style.top = "";
       	}
	}
}