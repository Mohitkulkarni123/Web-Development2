const express=require('express')
var app=express();
const port=3000
app.use(express.static("sty"))
var bodyparser=require('body-parser')
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended:true}));

app.get('/',function(req,res){
    res.sendFile(__dirname+'/contact.html');
});
app.post('/',function(req,res){
   console.log(req.body)
})
app.listen(port,function(){
console.log("server is started at 3000")
})