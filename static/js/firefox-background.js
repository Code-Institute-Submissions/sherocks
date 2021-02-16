/* This code will fix a bug in Firefox and set another background color for allauth forms */

const firefox = navigator.userAgent.indexOf("Firefox") != -1;
const container = document.getElementsByClassName("content-allauth");

if (firefox){
    for(var i = 0; i < container.length; i++){
		container[i].style.backgroundColor = "rgba(64,29,41, 0.8)";
	}
}