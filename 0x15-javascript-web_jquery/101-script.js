#!/usr/bin/node
document.onreadystatechange = function () {
	if (document.readyState === 'interactive') {
		$('#add_item').click(function () {
			$('.my_list').append('<li>Item</li>');
		});
		$('#remove_item').click(function () {
			$('.my_list li').last().remove();
		});
		$('#clear_list').click(function () {
			$('.my_list li').detach();
		});
	}
}