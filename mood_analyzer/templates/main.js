var testData = {"positive": 1, "negative": 0};
var negativeColorCode = "#ef5350";
var negativePalette = "Reds";

var positiveColorCode = "#66bb6a";
var positivePalette = "Greens";

var currentTheme = "";


function getMood(){
  //Get the entered hashtag
  var hashtagInput = document.getElementById("hashtag-input").value;
  //Qualify user input
  if(hashtagInput.replace(" ", "").length>0){
    //Reset percent-circle
    document.getElementById("percent-circle").setAttribute("class", "big c100 p0");
    document.getElementById("percent-span").childNodes[0].innerHTML="0%";
    document.getElementById("percent-span").childNodes[2].innerHTML="0%";
    document.getElementById("percent-circle-wrapper").style.display="none";

    //Hide slogan
    document.getElementById("slogan").style.display="none";

    //Display preloader
    document.getElementById("preloader").style.display="block";

    //Placeholder
    //setTimeout(function(){receiveServerResponse(testData, "OK")}, 1000);
    currentTheme=hashtagInput;
    //$.post("http://100.100.219.136/hashtag/",{"hashtag":hashtagInput}, receiveServerResponse);
    $.ajax({
        type: 'POST',
        contentType: "application/json",
        url: 'http://100.100.219.136/hashtag/',
        data: JSON.stringify({ "hashtag": hashtagInput , "days": document.getElementById("days").value}),
        success: receiveServerResponse
    });
  }else{
    console.log("Invalid user-input");
  }

}

//Interpretes data from server
function receiveServerResponse(data, status){
  console.log(data);
  document.getElementById("preloader").style.display="none";
  document.getElementById("percent-circle-wrapper").style.display="block";
  var percent=Math.floor(data.positive/(data.positive+data.negative)*100);
  if(percent>49){
    //Set the background to the defined positive color
    document.getElementById("body").style.backgroundColor=positiveColorCode;
    var pattern = Trianglify({
      height: document.body.clientHeight,
      width: document.body.clientWidth,
      x_colors: positivePalette,
      cell_size: 40});
  }else if(percent<50){
    //Set the background to the defined negative color
    document.getElementById("body").style.backgroundColor=negativeColorCode;
    var pattern = Trianglify({
      height: document.body.clientHeight,
      width: document.body.clientWidth,
      x_colors: negativePalette,
      cell_size: 40});
  }
  document.body.appendChild(pattern.canvas());
  //Start the animation to display the percent
  setPercent(percent);
}

//Temporaty variable, used while animating the word_meaning in percent
var percentToSet=0;

function setPercent(percent){
  percentToSet=percent;
  setPercentRaw();
}

function setPercentRaw(){
  var currentPercent = parseInt(document.getElementById("percent-circle").getAttribute("class").replace("big c100 p", ""));

  if(currentPercent>50){
    document.getElementById("fill").setAttribute("style", "border: 0.08em solid #66bb6a !important;");
  }else{
    document.getElementById("fill").setAttribute("style", "");
  }

  if(currentPercent>percentToSet){
    document.getElementById("percent-circle").setAttribute("class", "big c100 p"+(currentPercent-1));
  }else if(currentPercent<percentToSet){
    document.getElementById("percent-circle").setAttribute("class", "big c100 p"+(currentPercent+1));
  }


  document.getElementById("percent-span").childNodes[0].innerHTML=100-currentPercent+"%";
  document.getElementById("percent-span").childNodes[2].innerHTML=currentPercent+"%";

  document.getElementById("negInfoText").childNodes[1].innerHTML=100-currentPercent+"% des Internets sind in negativer Stimmung zum Thema "+currentTheme;
  document.getElementById("posInfoText").childNodes[1].innerHTML=currentPercent+"% des Internets sind in positiver Stimmung zum Thema "+currentTheme;

  if(currentPercent==percentToSet){
    console.log("Percent set!");
  }else{
    setTimeout(setPercentRaw, 10);
  }
}
