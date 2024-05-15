var express = require('express');
var router = express.Router();
let err=0;

let { k } = require('./server.js');// djeljena varijabla

router.get('/', function (req, res, next) {// ruta relativna
	res.render('login', {kat : kategorija,k:readData()});
});

router.get('/:kategorija', function (req, res, next) {// ruata + kategorija
	var logdata = req.params.kategorija
	var name = logdata.split(':');
	res.render('login', {trenutno : logdata, ime:name[0], id:name[1], err:0, user:0});
});

router.get('/:kategorija/submit/:user_mail', function (req, res, next) { // ruta +kategorija /subruta +user_mail
	const kategorija = req.params.kategorija;
	var name = kategorija.split(':');
	var id = parseInt(name[1]);//id u int.
	const userPass = req.params.user_mail;
	
	if(contains(k,userPass,id)){
		res.render('login', {trenutno : kategorija, ime:name[0], id:name[1],err:1, user:userPass});
	}
	else{
		k[id].push(userPass);// dodaj u tablicu
		res.redirect('/');// nazad na home
	}
});


function contains(k,userPass,id) {
	for(var i=0;i<k[id].length;i++){
		if(userPass==k[id][i]){
			return true;
		}
	}
return false;
}

module.exports = router;

