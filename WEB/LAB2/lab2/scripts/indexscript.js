
let productbx= document.getElementById("product_box");





function ispisi(ID){
	addtocart(ID);
}

function loadSite(index, idq) {

  sessionStorage.setItem("scrollPosition", window.pageYOffset);
  var newUrl = "http://localhost:3000/getProducts/" + index + idq;
  window.location.href = newUrl;
}

function scrollToPosition() {
  var scrollPosition = sessionStorage.getItem("scrollPosition");
  if (scrollPosition) {
    window.scrollTo(0, scrollPosition);
    sessionStorage.removeItem("scrollPosition");
    
  }
}

window.addEventListener("load", async function() {
	await dohvat();
	scrollToPosition();
	console.log(productarr);
	updatecartnum();
	//alert("izvrsava");
	updateallitemnum();
});


