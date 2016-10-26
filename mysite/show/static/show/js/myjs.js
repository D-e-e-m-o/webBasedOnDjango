/**
 * Created by deemo on 16-10-19.
 */
//验证码ajax
$(document).ready(function () {
	$('#ca-refresh').click(function(){
	var $form = $(this).parents('.form-group');
	$.getJSON("/captcha/refresh", {}, function(json) {
		$form.find('input[name="ca_0"]').val(json.key);
		$form.find('img.captcha').attr('src', json.image_url);
	});
	return false;
	});
});
