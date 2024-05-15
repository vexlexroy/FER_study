
let productarr='';
let productsStr='';

// rad s podacima za kosaricu
async function dohvat() {
  try {
    const response = await fetch('/getSelectedProducts');
    const data = await response.json();
    const productsStr = data.selectedProducts;
    
    //alert(productsStr);
    productarr = JSON.stringify(productsStr);
    //alert(productarr);
    
  } catch (error) {
    console.error('Error:', error);
  }
  productarr=productarr.replace('[','');
  productarr=productarr.replace(']','');
  productarr=productarr.split(',');
  //alert(productarr);
}
//------------------------------------

function addtocart(ID){
  sessionStorage.setItem("scrollPosition", window.pageYOffset);
  var newUrl = "http://localhost:3000/cart/add/" +ID;
  window.location.href = newUrl;
}

function subtractcart(ID){
	sessionStorage.setItem("scrollPosition", window.pageYOffset);
	var newUrl = "http://localhost:3000/cart/remove/" +ID;
  window.location.href = newUrl;
}

function getfromid(ID){
	//alert("products js ar:"+productarr[ID]);
	return productarr[ID];
}



function sum(array){
    var total =  0;
    for(i=0;i<array.length;i++){                  
			total += parseInt(array[i]);	
    }
    return total;
}

function updatecartnum(){
	var crt = document.getElementById("elementadd_cart");
	if(sum(productarr)>0){
		crt.innerHTML="<div id=\"product_count\"><span id=\"counttxt\">"+sum(productarr)+"</span></div>";
	}else{
		crt.innerHTML="";
	}
	
}
function updateitemnum(ID){
	//alert("unutra uitID");
	var itc=document.getElementById("elementadd_"+ID);
	if(itc != null){
	if(getfromid(ID)>0){
	itc.innerHTML="<div id=\"product_count\"><span id=\"counttxt\">"+getfromid(ID)+"</span></div>";
	}
	else{
	itc.innerHTML="";
	}
	}
}

function updateallitemnum(){
	//alert("unutra");
	//alert(productarr.length);
	for(var i=0; i<productarr.length;i++){
	//alert("unutra for");
	updateitemnum(i);
	}
}

window.onload = async function(){
	await dohvat();
	updatecartnum();
}


