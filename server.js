import express from 'express';
import 'dotenv/config';
const app = express();
const port = process.env.PORT || 8000;

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index', { text: 'World'});
})

app.get('/login', (req, res) => {
    res.render('login');
})

app.get('/register', (req, res) => {
    res.render('register');
})

app.listen(port, () => {
    console.log(`Running server on port ${port}!🚀`);
})