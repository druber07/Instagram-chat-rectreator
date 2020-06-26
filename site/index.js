$.get('data.txt', function(data) {
    var lines = data.split("∫");

    $.each(lines, function(n, elem) {
    	var info = elem.split('+');

    	if(info != ''){
            var date = info[2].split('-');
            if(lines[n+1] != undefined && lines[n+1] != ''){
                var fdate = lines[n+1].split('+')[2].split('-');
                if(parseInt(date[0]) != parseInt(fdate[0])){
                    $('body').append('<div class="date"><p>'+dateShow(date)+'</p></div>');
                }else if(parseInt(date[1]) != parseInt(fdate[1])){
                    $('body').append('<div class="date"><p>'+dateShow(date)+'</p></div>');
                }else if(parseInt(date[2]) != parseInt(fdate[2])){
                    $('body').append('<div class="date"><p>'+dateShow(date)+'</p></div>');
                }
            }

            if(info[0] == 'alikreznik'){
                if(isValidUrl(info[1])){
                    $('body').append('<div class="messageP2"><a class="P2">'+info[1]+'</a></div>');
                }else{
                    $('body').append('<div class="messageP1"><p class="P1">'+info[1]+'</p></div>');
                }
            }else{
                if(isValidUrl(info[1])){
                    $('body').append('<div class="messageP1"><a class="P1">'+info[1]+'</a></div>');
                }else{
                    $('body').append('<div class="messageP2"><p class="P2">'+info[1]+'</p></div>');
                }
            }
        }
        
    });
});

function dateShow(date){
	return date[0]+'/'+date[1]+'/'+date[2]
}

function isValidUrl(string) {
  try {
    new URL(string);
  } catch (_) {
    return false;  
  }

  return true;
}
