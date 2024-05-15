const express = require('express');
const path = require('path');
const app = express();
const mime = require('mime');
const session = require('express-session');
const crypto = require('crypto');

// Inicijalizacija sjednica
app.use(
  session({
    genid: () => {
      return crypto.randomUUID();
    },
    resave: false,
    saveUninitialized: true,
    secret: '123'
  })
);

// Inicijalizacija odabranih proizvoda
app.use((req, res, next) => {
  if (!req.session.selectedProducts) {
    const data = require('./data/mydata.js');
    let size = 0;
    data.categories.forEach((category) => {
      size += category.products.length;
    });
    req.session.selectedProducts = new Array(size).fill(0);
  }
  next();
});

const homeRouter = require('./routes/home.routes');
const cartRouter = require('./routes/cart.routes');

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));

// Route za js
app.get('/scripts/:filename', (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, 'scripts', filename);
  res.sendFile(filePath);
});

// variabla za linkove
app.use((req, res, next) => {
  const sessionId = req.session.id;
  res.locals.sessionId = sessionId;
  next();
});

app.use('/', homeRouter);
app.use('/cart', cartRouter);

//loadanje proizvoda od korisnika u js
app.get('/getSelectedProducts', (req, res) => {
  const selectedProducts = req.session.selectedProducts;
  res.json({ selectedProducts });
});

//-------------------------------------------

app.listen(3000);
