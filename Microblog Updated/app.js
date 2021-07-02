const express = require('express')
const app = express()
const path = require("path")
const fs = require('fs')
const bodyParser = require('body-parser');

//static files
app.use(express.static('public'))
app.use('/css', express.static(__dirname + 'public/css'))
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

//Set Views
app.set('views', './views')
app.set("view engine", "ejs")

app.get('', (req, res) => {
    res.render('index')
})

app.get('/help', (req, res) => {
    res.render('help')
})

//creating post
app.post('/create', (req, res) => {
    const contents = loadNotes()
    content = {
        title: req.body.title,
        body: req.body.body
    }
    
    contents.push(content)
    const contentsJSON = JSON.stringify(contents)
    fs.writeFileSync("data.json", contentsJSON)
    return res.redirect('/')
    
})

const loadNotes = function () {
    try {
        const dataBuffer = fs.readFileSync("data.json")
        const dataJSON = dataBuffer.toString()
        console.log("Notes Loaded.")
        return JSON.parse(dataJSON)
    } catch (e) {
        return []
    }
}


app.get('/posts', (req, res) => {
    const contents = loadNotes()
    let x = "< h1 > hello pearl</h1> <p>This is an env.</p>"
        
    titleArray = []
    for (i = 0; i < contents.length; i++) {
        titleArray.push(contents[i].title)
    }
    
    res.render("posts", { contents: contents })

})


app.listen(3000)

