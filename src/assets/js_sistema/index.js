function deactivateAll(){
	var buttons = document.getElementsByTagName('button');
	for(button in buttons)
		button.classList.remove("on")
}

function activate(sender){
	if(sender == null)
		return;
	sender.classList.add("on");
}

function handle(sender, action, value){
	console.log(value)
	$('.modal').modal();
	if(value === 'left'){
		$('.modal').modal();
	}

	// deactivateAll();
	// activate(sender);
	submit(action, value);
}

function submit(action, value){
	var xhr = new XMLHttpRequest();
	xhr.open("POST", window.location.href, true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify({
		'action' : action,
		'value' :  value,
	}));
}


