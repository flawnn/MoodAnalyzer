var testData = {"mood": -83};
var negativeColorCode = "#ef5350";
var negativePalette = "Reds";
var positiveColorCode = "#66bb6a";
var positivePalette = "Greens";


function getMood(){
  //Get the entered hashtag
  var hashtagInput = document.getElementById("hashtag-input").value;
  //Qualify user input
  if(hashtagInput.replace(" ", "").length>0){
    //Reset percent-circle
    document.getElementById("percent-circle").setAttribute("class", "big c100 p0");
    document.getElementById("percent-span").innerHTML="0%";
    document.getElementById("percent-circle-wrapper").style.display="none";

    //Hide slogan
    document.getElementById("slogan").style.display="none";

    //Display preloader
    document.getElementById("preloader").style.display="block";

    //Placeholder
    setTimeout(function(){receiveServerResponse(testData, "OK")}, 1000);
    //$.post("100.100.219.101/hashtag",{"hashtag":hashtagInput}, receiveServerResponse(data, status));
  }else{
    console.log("Invalid user-input");
  }

}

//Interpretes data from server
function receiveServerResponse(data, status){
  console.log(data);
  document.getElementById("preloader").style.display="none";
  document.getElementById("percent-circle-wrapper").style.display="block";
  var percent=data.mood;
  if(data.mood>0){
    //Set the background to the defined positive color
    document.getElementById("body").style.backgroundColor=positiveColorCode;
    var pattern = Trianglify({
      height: document.body.clientHeight,
      width: document.body.clientWidth,
      x_colors: positivePalette,
      cell_size: 40});
  }else if(data.mood<0){
    //Set the background to the defined negative color
    document.getElementById("body").style.backgroundColor=negativeColorCode;
    var pattern = Trianglify({
      height: document.body.clientHeight,
      width: document.body.clientWidth,
      x_colors: negativePalette,
      cell_size: 40});
    //Invert the mood if it's negative
    percent=percent*(-1);
  }
  document.body.appendChild(pattern.canvas());
  //Start the animation to display the percent
  setPercent(percent);
}

//Temporaty variable, used while animating the mood in percent
var percentToSet=0;

function setPercent(percent){
  percentToSet=percent;
  setPercentRaw();
}

function setPercentRaw(){
  var currentPercent = parseInt(document.getElementById("percent-circle").getAttribute("class").replace("big c100 p", ""));
  if(currentPercent>percentToSet){
    document.getElementById("percent-circle").setAttribute("class", "big c100 p"+(currentPercent-1));
  }else if(currentPercent<percentToSet){
    document.getElementById("percent-circle").setAttribute("class", "big c100 p"+(currentPercent+1));
  }

  document.getElementById("percent-span").innerHTML=currentPercent+"%";

  if(currentPercent==percentToSet){
    console.log("Percent set!");
  }else{
    setTimeout(setPercentRaw, 10);
  }
}
