"use strict";

function producePositivity(results) {
	document.querySelector("#affirmationDisplay").innerHTML = results;
  }
  
  function positiveWords(evt) {
	fetch("/affirmations")
	  .then((response) => response.text())
	  .then(producePositivity);
  }
  
  document
	.querySelector("#affirmation-btn")
	.addEventListener("click", positiveWords);