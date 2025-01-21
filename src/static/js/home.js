
var chosenStrategy = document.getElementById("myStrategieSelector");

var myTemporalitySelector = document.getElementById("myTemporality");
var myIntervalSelector = document.getElementById("myInterval");

myTemporalitySelector.addEventListener(
  "change",
  function(){
    myIntervalSelector.innerHTML = "";

    var myTemporalityOpction1m = document.createElement("option")
    var myTemporalityOpction2m = document.createElement("option")
    var myTemporalityOpction5m = document.createElement("option")
    var myTemporalityOpction15m = document.createElement("option")
    var myTemporalityOpction30m = document.createElement("option")
    var myTemporalityOpction60m = document.createElement("option")
    var myTemporalityOpction90m = document.createElement("option")
    var myTemporalityOpction1h = document.createElement("option")
    var myTemporalityOpction1d = document.createElement("option")
    var myTemporalityOpction5d = document.createElement("option")
    var myTemporalityOpction1wk = document.createElement("option")
    var myTemporalityOpction1mon = document.createElement("option")
    var myTemporalityOpction3mo = document.createElement("option")

    myTemporalityOpction1m.value = "1 minute";
    myTemporalityOpction1m.text = "1 minute";
    myTemporalityOpction2m.value = "2 minutes";
    myTemporalityOpction2m.text = "2 minutes";
    myTemporalityOpction5m.value = "5 minutes";
    myTemporalityOpction5m.text = "5 minutes";
    myTemporalityOpction15m.value = "15 minutes";
    myTemporalityOpction15m.text = "15 minutes";
    myTemporalityOpction30m.value = "30 minutes";
    myTemporalityOpction30m.text = "30 minutes";
    myTemporalityOpction60m.value = "60 minutes";
    myTemporalityOpction60m.text = "60 minutes";
    myTemporalityOpction90m.value = "90 minutes";
    myTemporalityOpction90m.text = "90 minutes";
    myTemporalityOpction1h.value = "1 hour";
    myTemporalityOpction1h.text = "1 hour";
    myTemporalityOpction1d.value = "1 day";
    myTemporalityOpction1d.text = "1 day";
    myTemporalityOpction5d.value = "5 days";
    myTemporalityOpction5d.text = "5 days";
    myTemporalityOpction1wk.value = "1 week";
    myTemporalityOpction1wk.text = "1 week";
    myTemporalityOpction1mon.value = "1 month";
    myTemporalityOpction1mon.text = "1 month";
    myTemporalityOpction3mo.value = "3 months";
    myTemporalityOpction3mo.text = "3 months";

    switch(document.getElementById("myTemporality").value){
      case "1 day":
        myIntervalSelector.add( myTemporalityOpction1m );
        myIntervalSelector.add( myTemporalityOpction2m );
        myIntervalSelector.add( myTemporalityOpction5m );
        myIntervalSelector.add( myTemporalityOpction15m );
        myIntervalSelector.add( myTemporalityOpction30m );
//        myIntervalSelector.add( myTemporalityOpction60m );
        myIntervalSelector.add( myTemporalityOpction1h );
        myIntervalSelector.add( myTemporalityOpction90m );
        break;

      case "5 days":
        myIntervalSelector.add( myTemporalityOpction1m );
        myIntervalSelector.add( myTemporalityOpction2m );
        myIntervalSelector.add( myTemporalityOpction5m );
        myIntervalSelector.add( myTemporalityOpction15m );
        myIntervalSelector.add( myTemporalityOpction30m );
 //       myIntervalSelector.add( myTemporalityOpction60m );
        myIntervalSelector.add( myTemporalityOpction1h );
        myIntervalSelector.add( myTemporalityOpction90m );
        myIntervalSelector.add( myTemporalityOpction1d );
        break;
        
      case "1 month":
        myIntervalSelector.add( myTemporalityOpction2m );
        myIntervalSelector.add( myTemporalityOpction5m );
        myIntervalSelector.add( myTemporalityOpction15m );
        myIntervalSelector.add( myTemporalityOpction30m );
//        myIntervalSelector.add( myTemporalityOpction60m );
        myIntervalSelector.add( myTemporalityOpction1h );
        myIntervalSelector.add( myTemporalityOpction90m );
        myIntervalSelector.add( myTemporalityOpction1d );
        myIntervalSelector.add( myTemporalityOpction1wk );
        break;
      
      case "3 months":
//        myIntervalSelector.add( myTemporalityOpction60m );
        myIntervalSelector.add( myTemporalityOpction1h );
        myIntervalSelector.add( myTemporalityOpction90m );
        myIntervalSelector.add( myTemporalityOpction1d );
        myIntervalSelector.add( myTemporalityOpction1wk );
        myIntervalSelector.add( myTemporalityOpction1mon );
        break;

      case "6 months":
        myIntervalSelector.add( myTemporalityOpction1h );
//        myIntervalSelector.add( myTemporalityOpction90m ); //It is not valid for 6 months en adelante
        myIntervalSelector.add( myTemporalityOpction1d );
        myIntervalSelector.add( myTemporalityOpction5d );
        myIntervalSelector.add( myTemporalityOpction1wk );
        myIntervalSelector.add( myTemporalityOpction1mon );
        myIntervalSelector.add( myTemporalityOpction3mo );
        break;

      case "1 year" || "2 years":
        myIntervalSelector.add( myTemporalityOpction1h );
        myIntervalSelector.add( myTemporalityOpction1d );
        myIntervalSelector.add( myTemporalityOpction5d );
        myIntervalSelector.add( myTemporalityOpction1wk );
        myIntervalSelector.add( myTemporalityOpction1mon );
        myIntervalSelector.add( myTemporalityOpction3mo );
        break;

      default:
        myIntervalSelector.add( myTemporalityOpction1d );
        myIntervalSelector.add( myTemporalityOpction5d );
        myIntervalSelector.add( myTemporalityOpction1wk );
        myIntervalSelector.add( myTemporalityOpction1mon );
        myIntervalSelector.add( myTemporalityOpction3mo );
        break;

    }
  }
);


function findSelectorValue () {
    
    if (chosenStrategy.value=="" || chosenStrategy.value=="Select the strategy" || chosenStrategy.value=="Not-implemented-yet strategy.py") {
        document.getElementById("strategyOptions").classList.add("invisible");
    } else {
        document.getElementById("strategyOptions").classList.remove("invisible");
        document.getElementById("strategyOptions").style.display="block";
    }
}

function myDateValidation() {
    
    if(document.getElementById("myDate1").value != "" && document.getElementById("myDate2").value != "") {

        document.getElementById("myFrequency").classList.remove("invisible");
        document.getElementById("myFrequency").style.display="block";

    }
}
