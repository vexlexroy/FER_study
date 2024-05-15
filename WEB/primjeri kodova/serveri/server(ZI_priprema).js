const express = require('express');
const app = express();
var path = require('path');

//djeljena variabla
let k = [[],[],[],[],[],[],[],[]];
module.exports.k = k;
//------------------

const route = require('./routes');
const routeLog = require('./logroute');



app.set('views', path.join(__dirname, 'views'));// postavlja put za ejs
app.set('view engine', 'ejs'); // postavlja ejs ko engine
app.use(express.static(path.join(__dirname, 'public'))); // postavlja put za public



app.use('/', route); // postavlja put za ruter
app.use('/login', routeLog); // put za ruter



app.listen(3000);