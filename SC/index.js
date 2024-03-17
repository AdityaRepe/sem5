import express from "express";
import mongoose from "mongoose";
import path from "path";

mongoose.connect("mongodb://127.0.0.1:27017",{
    dbname:"backend",
})
.then(c=>console.log("Database connected succesfully"))
.catch((e) => console.log(e));

const messageSchema = new mongoose.Schema({
    name: String,
    email: String
});

const Message = mongoose.model("Message",messageSchema);

const app = express();

const users=[];

app.use(express.static(path.join(path.resolve(),"public")));
app.use(express.urlencoded({ extended: true}));

app.set("view engine","ejs");

app.get("/", (req,res) =>{
    res.render("index",{ name : "Aditya"});
});


app.get("/add", async (req,res) =>{
    await Message.create({name:"Aditya",email:"hello@gmail.com"});
        res.send("Nice");
});

app.get("/success", (req,res) =>{
    res.render("success");
});

app.post("/success", async (req,res) =>{
    // console.log(req.body);
    // users.push({username:req.body.name, email:req.body.email });
    const { name, email } = req.body;
    await Message.create({ name, email })
    res.redirect("/success");
});

app.get("/users", (req,res) =>{
    res.json({
        users,
    });
});

app.listen(5000, () =>{
    console.log("Server is working");
});