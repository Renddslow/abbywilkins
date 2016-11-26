global_page_number = 1;

$(function(){
	var bottomOfPage = false;
	getPosts();
	if (bottomOfPage) {
		getPosts();
	}
});

function getPosts() {
	$.ajax({
		type: "GET",
		url: "/posts?limit=12&page=" + global_page_number,
		success: function(e) {
			displayPosts(e);
		}
	});
	global_page_number++;
}

function displayPosts(data) {
	for (var i = 0; i < data.length; i++) {
		var title = data['title'];
		var text = data['text'];
		var image = date['image'];
		var date_created = date['date_created'];
		$(".post-column").append($("#post-template").html());

	}
}
